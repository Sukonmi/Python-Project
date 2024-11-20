# 🎯WHAT I AIMED FOR.
The Interactive Python Quiz Game is a text-based application that presents a series of multiple-choice questions to the user. The game provides instant feedback on each answer and keeps track of the user's score throughout the quiz. This project can be further enhanced with additional features such as random question order, a timer for each question, high score tracking, and a graphical user interface (GUI) using libraries like tkinter.

# ℹ️Instructions

- Question and Answer Handling:
  - Display multiple-choice questions to the user.
  - Capture and validate user inputs.
  - Provide immediate feedback on the correctness of answers.
  - Score Tracking:

- Keep track of the user's score throughout the quiz.
  - Display the final score at the end of the quiz.

- Randomization:
  -Randomly shuffle the order of questions for each game session to enhance replayability.
  - User Interaction:

- Simple and intuitive user prompts to navigate through the quiz.

- Optional Enhancements:
  - Implement a timer for each question to add a time-based challenge.
  - Store and display high scores from previous sessions.
  - Develop a graphical user interface (GUI) using tkinter for a more interactive experience.

# 🛠️TOOLS USED.
- VSCode.
- GitHub.
- Git.
- Python.
- Google.
- YouTube.

```
import random
import tkinter as tk
from tkinter import messagebox
import os

def countdown(seconds, label, callback):
    def update_timer():
        nonlocal seconds
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            label.config(text=time_str)
            seconds -= 1
            root.after(1000, update_timer)
        else:
            label.config(text="Time's up!")
            callback()  # Invoke the callback function when time is up
    update_timer()
```
