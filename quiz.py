import random
import tkinter as tk
from tkinter import messagebox
import os

# Question and Answer Handling:
questions = [ 
    { 
        "question": "1. What is the correct file extension for Python files?", 
        "options": [".py", ".pt", ".pyt", ".p"], 
        "answer": ".py" 
    }, 
    { 
        "question": "2. How do you create a variable with the numeric value 5?", 
        "options": ["x = int(5)", "x = 5", "int x = 5", "x <- 5"], 
        "answer": "x = 5" 
    }, 
    { 
        "question": "3. Which of the following is a correct syntax to output 'Hello World' in Python?", 
        "options": ["echo 'Hello World'", "print('Hello World')", "p('Hello World')", "printf('Hello World')"], 
        "answer": "print('Hello World')" 
    }, 
    { 
        "question": "4. What is the correct way to create a function in Python?", 
        "options": ["function myFunction():", "create myFunction():", "def myFunction():", "myFunction():"], 
        "answer": "def myFunction():" 
    }, 
    { 
        "question": "5. Which method can be used to remove any whitespace from both the beginning and the end of a string?", 
        "options": ["strip()", "trim()", "stripped()", "len()"], 
        "answer": "strip()" 
    }, 
    { 
        "question": "6. Which of the following statements is used to create an empty set?", 
        "options": ["set = {}", "set = []", "set = set()", "set = ()"], 
        "answer": "set = set()" 
    }, 
    { 
        "question": "7. Which operator is used to multiply numbers in Python?", 
        "options": ["%", "*", "#", "&"], 
        "answer": "*" 
    }, 
    { 
        "question": "8. How do you insert COMMENTS in Python code?", 
        "options": ["/* This is a comment */", "// This is a comment", "# This is a comment", "-- This is a comment"], 
        "answer": "# This is a comment" 
    }, 
    { 
        "question": "9. What is the correct way to write a list in Python?", 
        "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "<1, 2, 3>"], 
        "answer": "[1, 2, 3]" 
    }, 
    { 
        "question": "10. What is a correct syntax to return the first character in a string?", 
        "options": ["x = sub('Hello', 0, 1)", "x = 'Hello'.sub(0, 1)", "x = 'Hello'[0]", "x = substring('Hello', 0, 1)"], 
        "answer": "x = 'Hello'[0]" 
    }
]

# Function to shuffle questions 
def shuffle_questions(questions):
    random.shuffle(questions)

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

# Initialize variables 
score = 0 
current_question_index = 0 
shuffle_questions(questions)

def submit():
    global current_question_index, score
    selected_option = var.get()
    correct_answer = questions[current_question_index]['answer']

    if selected_option == correct_answer:
        score += 1
        feedback_label.config(text="Correct! Well done.")
    else:
        feedback_label.config(text=f"Oops, that's not quite right. The correct answer is: {correct_answer}")

    current_question_index += 1

    if current_question_index < len(questions):
        next_question()
    else:
        show_final_score()

def mark_question_failed():
    global current_question_index
    feedback_label.config(text=f"Time's up! The correct answer is: {questions[current_question_index]['answer']}")
    current_question_index += 1

    if current_question_index < len(questions):
        next_question()
    else:
        show_final_score()

def next_question():
    global current_question_index
    var.set("")
    
    if current_question_index < len(questions):
        question_label.config(text=questions[current_question_index]['question'])
        
        for i, option in enumerate(questions[current_question_index]['options']):
            option_buttons[i].config(text=option, value=option)
        
        feedback_label.config(text="")
        countdown(10, timer_label, mark_question_failed)  # Pass the mark_question_failed function as a callback
    else:
        show_final_score()

def show_final_score():
    question_label.pack_forget()
    
    for option in option_buttons:
        option.pack_forget()
    
    submit_button.pack_forget()
    feedback_label.config(text=f"Your final score is: {score}/{len(questions)}")
    messagebox.showinfo("Quiz Completed", f"Thanks for participating! Your final score is: {score}/{len(questions)}")
    update_high_score(score)

def update_high_score(score):
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    else:
        high_score = 0
    
    if score > high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))
        messagebox.showinfo("New High Score!", f"Congratulations! You have a new high score of {score}/{len(questions)}")
    else:
        messagebox.showinfo("High Score", f"Your score: {score}/{len(questions)}\nHigh score: {high_score}/{len(questions)}")

# Main window
root = tk.Tk()
root.title("Python Quiz")
root.geometry("400x300")

question_label = tk.Label(root, text=questions[current_question_index]['question'])
question_label.pack(pady=20)

var = tk.StringVar()
option_buttons = []

for option in questions[current_question_index]['options']:
    radio = tk.Radiobutton(root, text=option, variable=var, value=option)
    radio.pack(anchor=tk.W)
    option_buttons.append(radio)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

feedback_label = tk.Label(root, text="")
feedback_label.pack()

timer_label = tk.Label(root, text="")
timer_label.pack()

# Show welcome message
messagebox.showinfo("Welcome", "Welcome to the Python Quiz game! Brace yourself and get ready to test your knowledge.")

next_question()  # Start the quiz

root.mainloop()