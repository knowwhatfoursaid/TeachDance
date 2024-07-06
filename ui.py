import tkinter as tk
from tkinter import messagebox
from player import Player
from lessons import create_lessons

class DanceApp:
    def __init__(self):
        self.player = Player("Dancer")
        self.lessons = create_lessons()
        self.current_lesson = None

    def run(self):
        self.root = tk.Tk()
        self.root.title("TeachDance")

        self.label = tk.Label(self.root, text="Welcome to TeachDance!")
        self.label.pack()

        self.lesson_listbox = tk.Listbox(self.root)
        for lesson in self.lessons:
            self.lesson_listbox.insert(tk.END, lesson.dance.name)
        self.lesson_listbox.pack()

        self.start_button = tk.Button(self.root, text="Start Lesson", command=self.start_lesson)
        self.start_button.pack()

        self.root.mainloop()

    def start_lesson(self):
        selected_index = self.lesson_listbox.curselection()
        if selected_index:
            self.current_lesson = self.lessons[selected_index[0]]
            messagebox.showinfo("Lesson Info", f"Starting {self.current_lesson.dance.name}")
            # 这里可以加入播放视频的功能

