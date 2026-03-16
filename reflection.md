# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran the game, it showed a number guessing game where the player guesses a number between 1 and 100. It had an input box to enter a guess, a submit guess button, and a new Game button. There was also a setting panel on the left showing the difficulty dropdown, range, and attempts allowed. It also had a developer debug section that displayed information like the secret number, attempts, and score. Overall, the interface looked clean and functional when it first loaded.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
One bug I noticed was that the hints were incorrect. If the answer was 22, the game showed go higher for 25 and go lower for 19, which is backwards. 
Another issue was on launch in the debugger section, the attempt value is set to 1 but new game sets it to 0. 
The correct guess behavior worked properly, but the game accepted values greater than 100 even though the range was 1–100. 
I also noticed that the difficulty ranges seemed wrong, easy was 1–20 as expected, but normal and hard seemed reversed (normal was 1–100 and hard was 1–50).
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
ChatGPT, copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct suggestion from the AI was to fix the existing test cases that were failing. After making the suggested changes, I ran the test cases again and confirmed that they passed. I also reviewed the logic to understand why the issue occurred and verified that the fix addressed the root cause. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One misleading suggestion was when the AI moved the get_range_for_difficulty function to logic_utils for better testing but did not remove the original implementation in app.py. This created redundant code. I noticed the duplication while reviewing the files and asked the AI to fix it. It then removed the duplicate code from app.py and added the correct import from logic_utils. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I restarted the game and manually tested the behavior again. I checked that the range values were correct for the difficulty levels, with 1–50 for normal mode and 1–100 for hard mode. I also verified that the hints were working properly, meaning the game now shows “go higher” for a lower guess and “go lower” for a higher guess.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran the tests using pytest. The tests confirmed that the fixes I made worked as expected and that the game logic was now behaving correctly. This helped verify that the bug fixes.

- Did AI help you design or understand any tests? How?
Yes, AI helped generate test cases for the bugs I fixed. It also explained how the tests worked and what conditions they were checking. This helped me better understand how the tests verified the correct game behavior.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
