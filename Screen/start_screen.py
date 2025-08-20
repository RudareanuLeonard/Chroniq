import tkinter as tk
from tkinter import ttk
from Screen.screen import Screen

class StartScreen(Screen):
    def __init__(self, width, height, app_name):
        super().__init__(width, height, app_name)

    def create_screen(self):
        root = tk.Tk()
        root.geometry(f"{self.width}x{self.height}")
        root.configure(background="#188FBE")

        frame_style = ttk.Style()
        frame_style.configure("Frame.TFrame", background='#188FBE')

        frame = ttk.Frame(root, style="Frame.TFrame")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=self.app_name, padding=20).pack(pady=20)
        ttk.Button(frame, text="TEST").pack()

        root.mainloop()
