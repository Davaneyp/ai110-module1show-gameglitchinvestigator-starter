# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [The purpose of this game was to have the user enter a number between a range and with hints get closer to the secret number until they guess correctly or run out of guesses.] Describe the game's purpose.
- [I found several bugs, the first one being the enter key did not actually submit the guess, the second was that the Higher/Lower hint messages were flipped, and third the game would not actually reset when the new game button was pressed.] Detail which bugs you found.
- [I applied two fixes, the enter key submition fix was fixed by putting the input and button inside an st.form. The hint message was fixed by swapping the two messages within the code.] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User types a guess of 40
2. User presses enter to submit instead of clicking the submit button
3. Game returns "Too High" message
4. User guess a lower number
5. Game sends the correct hint message
6. Game ends when the correct number is entered/or if guesses run out.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
