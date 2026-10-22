# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|65     |"Too high" hint    |"Go Higher" Hint | None
|New Game| Game restart     |No game restart  | None
|Enter  |Submit Guess       |Nothing happens  | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example that Claude suggested that was correct was that the logic behind the Higher/Lower hint message was
flipped which in turn would show the wrong message to the user. During my initial tests of the application this
was one of the issues I had observed so the AI mentioning it wasnt much of a surprise to me.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
One example of an AI suggestion I did not accept was that it stated the tests of the first bug would show 3 failures and that those issues would need to be fixed through another portion of the code. I decided against this and continued solely with the current fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was truly fixed after it was tested in the full application environment, and not
after the pytest case was ran and confirmed. Testing in the full environment showed that when
including all of the surrounding code it still worked.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One of the test ran was to verify the Higher/Lower hint message it ran a series of guesses showing
each of them passed with the correct message stating whether or not the guess should be higher or
lower.

- Did AI help you design or understand any tests? How?
Yes AI helped me design and understand the test for the first bug with the enter key to submit
the guess. It did so by helping me understand how that could be tested without doing so in the full application
environment.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain it as a straight-forward experience, with the pytest it runs directly in the terminal which makes debugging quite simple. This prevents you from having to cross reference changes/fixes in the application itself speeding up the process.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I would definitely use the strategy of understanding the logic behind the bug, as this gives me a general understanding of what causes the issue and then allowing me to recognize future issues of similar natures.

- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently would be to try and implement the fix along side the AI assistant to see if I understand the general scope of the issue so that it feels more collaborative instead of prompted.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This changed the way I think about AI generated code because of the message in the application stating that a generative AI believed the code was ready for deployment but after determining the bugs I now know that wasnt true and it needed to be fact checked first.
