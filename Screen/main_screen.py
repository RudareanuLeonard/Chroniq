import tkinter as tk
from tkinter import ttk
from Screen.screen import Screen

class MainScreen(Screen):
    def __init__(self, width, height, app_name):
        super().__init__(width, height, app_name)
        self.task_count = 0 

    def create_screen(self):
        root = tk.Tk()
        root.geometry(f"{self.width}x{self.height}")
        root.configure(background="#188FBE")

        frame_style = ttk.Style()
        frame_style.configure("Frame.TFrame", background='#188FBE')

        welcome_label = ttk.Label(root,
                                  font=("Times New Roman", 20),
                                  text="Welcome!"
                                  )
        
        welcome_label.pack(padx=10, pady=10)

        add_task_button = ttk.Button(root,
                                     text="+",
                                     command=self.add_task)

        add_task_button.pack(padx=100, pady=100)

        tasks_container = ttk.Frame(root)
        tasks_container.pack(fill="both", padx=10, pady=10, expand=True) #fill both - container stretch both horizontally and vertically; expand=True - take extra space in case of window resizing

        tasks_canvas = tk.Canvas(tasks_container, background="white") #we use canvas cuz it's scrollable... a frame its not
        scrollbar = ttk.Scrollbar(tasks_container, orient="vertical", command=tasks_canvas.yview)

        root.mainloop()

    def add_task(self):
        print("TASK ADDED")