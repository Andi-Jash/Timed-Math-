import random
import time
import tkinter as tk
from tkinter import messagebox

Operators = [
    "+", "-", "*"
]
min_operand = 3
max_operand = 12
total_problems = 10

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Game")

        self.problem_label = tk.Label(
            root,
            text = "Press 'Start' to begin",
            font ="Arial 16"
        )
        self.problem_label.pack(pady=20)

        self.answer_entry = tk.Entry(
            root,
            font= "Arial 16"
        )
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(
            root,
            text = "Submit",
            command= self.check_answer,
            font = "Arial 16"
        )
        self.submit_button.pack(pady=10)

        self.start_button = tk.Button(
            root,
            text = "Start",
            command= self.start_quiz,
            font="Arial 16"
        )
        self.start_button.pack(pady=20)

        self.result_label = tk.Label(
            root,
            text = "",
            font = "Arial 16"
        )
        self.result_label.pack(pady=20)

        self.current_problem = None
        self.current_answer = None
        self.problem_count = 0
        self.wrong_count = 0
        self.start_time = None

    def generate_problem(self):
        left = random.randint(min_operand, max_operand)
        right = random.randint(min_operand, max_operand)
        operator = random.choice(Operators)

        expr = f"{left} {operator} {right}"
        answer = eval(expr)
        return expr, answer
    
    def start_quiz(self):
        self.problem_count = 0
        self.wrong_count = 0
        self.start_time = time.time()
        self.next_problem()

    def next_problem(self):
        if self.problem_count >= total_problems:
            self.end_quiz()
            return
        
        self.problem_count += 1
        self.current_problem, self.current_answer = self.generate_problem()
        self.problem_label.config(text=f"Problem #{self.problem_count}: {self.current_problem} = ")

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.current_answer:
                self.answer_entry.delete(0, tk.END)
                self.next_problem()
            else:
                self.wrong_count += 1
                messagebox.showerror("INCORRECT", "TRY AGAIN")
        except ValueError:
            messagebox.showerror("INVALID INPUT", "IT NEEDS TO BE A NUMBER HOW DUMB CAN U BE")

    def end_quiz(self):
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        result_message = f"Nice work you finished in {total_time} seconds! You got {self.wrong_count} wrong."
        self.result_label.config(text = result_message)
        self.problem_label.config(text = "Press 'Start' to begin again")


root = tk.Tk()
app = MathQuizApp(root)
root.mainloop()