from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression tests for the "Enter key doesn't submit" bug ---
# Pressing Enter in a Streamlit text_input only reruns the script; it never
# clicks a plain st.button, so the `if submit:` block was skipped. Inside an
# st.form, Enter triggers the form's submit button instead.
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def _submit_button(at):
    return next(b for b in at.button if b.proto.is_form_submitter)


def test_guess_input_and_submit_button_share_a_form():
    # Enter only submits if the input and a form_submit_button live in the same form
    at = AppTest.from_file(APP_PATH).run()
    guess_input = at.text_input[0]
    submit = _submit_button(at)

    assert guess_input.form_id != ""
    assert submit.proto.form_id == guess_input.form_id


def test_submitting_guess_form_processes_the_guess():
    # Submitting the form (what Enter does) should count the attempt and record the guess
    at = AppTest.from_file(APP_PATH).run()
    attempts_before = at.session_state.attempts

    at.text_input[0].input("42")
    _submit_button(at).click().run()

    assert at.session_state.attempts == attempts_before + 1
    assert at.session_state.history == [42]


# --- Regression tests for the "hint points the wrong way" bug ---
# check_guess had its hint messages swapped ("Too High" said "Go HIGHER!"), and
# on even attempts app.py passed the secret as a str, so the fallback compared
# strings alphabetically ("9" > "50" is True). Both are covered below: each
# case submits two guesses in a row so it hits an odd and an even attempt.
import pytest

SECRET = 50


def _hints_for_two_guesses(guess):
    at = AppTest.from_file(APP_PATH)
    at.session_state["secret"] = SECRET
    at.run()

    hints = []
    for _ in range(2):
        at.text_input[0].input(str(guess))
        _submit_button(at).click().run()
        hints.append(at.warning[0].value)
    return hints


@pytest.mark.parametrize(
    "guess, expected_hint",
    [
        (9, "Go HIGHER!"),   # alphabetically "9" > "50", numerically 9 < 50
        (40, "Go HIGHER!"),
        (60, "Go LOWER!"),
        (100, "Go LOWER!"),  # alphabetically "100" < "50", numerically 100 > 50
    ],
)
def test_hint_points_toward_secret_on_every_attempt(guess, expected_hint):
    for hint in _hints_for_two_guesses(guess):
        assert expected_hint in hint
