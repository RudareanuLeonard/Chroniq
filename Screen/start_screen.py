import tkinter as tk
from tkinter import ttk
from Screen.screen import Screen

class StartScreen(Screen):
    def __init__(self, width, height, app_name):
        super().__init__(width, height, app_name)

    def create_screen(self):
        root = tk.Tk()

        frame_style = ttk.Style()
        frame_style.configure("Frame.TFrame", background='#188FBE')

        frame = ttk.Frame(root, padding=150, style="Frame.TFrame")
        frame.grid()

        ttk.Label(frame, text = self.app_name, padding=20).grid(column=0,row=1)

        ttk.Button(frame, text="TEST").grid(column=0,row=2)
        root.configure(background='#000000')
        root.mainloop()