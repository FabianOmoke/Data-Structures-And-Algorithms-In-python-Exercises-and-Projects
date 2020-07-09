import tkinter as tk
from tkinter import simpledialog, messagebox

applicationWindow = tk.Tk()

prompt = messagebox.askokcancel("Briefing","We are going to Calculate Your Target fat-Burning Heart Rate", parent=applicationWindow)
smoker = simpledialog.askstring("SmokingHabits", "Do you Smoke? yes or no: ", parent = applicationWindow)

if smoker == 'no' or  None:
    print("Oh, You are not a Smoker. Wow! Keep it up!")
else:
    print("Uh Oh! Might be tricky but we can work on it")

age = simpledialog.askinteger("Your Age", "How Old Are you?", parent=applicationWindow)

if age is not None:
    ageConfirm = messagebox.askokcancel("Age Confirmation",f'Are you {age} Years Old?')
    max_heart_rate = 206.9 - (0.67 * age)
    target = max_heart_rate * 0.65
    messagebox.showinfo("Target Fat Burning Rate", f'Your Target Fat-Burning Rate is {target}')






