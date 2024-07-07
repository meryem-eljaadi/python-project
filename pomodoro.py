from tkinter import *
from PIL import Image, ImageTk

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("700x700")

        # Maticha image
        self.maticha_image = Image.open('maticha.png')
        self.maticha_photo = ImageTk.PhotoImage(self.maticha_image)

        self.label = Label(root, image=self.maticha_photo) 
        self.label.pack(pady=5)
        
        self.button_frame = Frame(root)
        self.button_frame.pack(pady=20)

        # The timer label
        self.timer_label = Label(root, text="25:00", font=("Arial", 24))
        self.timer_label.place(relx=0.5, rely=0.5, anchor="center")

        # Create buttons
        self.start_button = Button(self.button_frame, text="Start", command=self.start_timer, font=("Arial", 12))
        self.start_button.pack(side=LEFT, padx=10, pady=10)

        self.short_break_button = Button(self.button_frame, text="Short Break", command=self.short_break, font=("Arial", 12))
        self.short_break_button.pack(side=LEFT, padx=10, pady=10)

        self.long_break_button = Button(self.button_frame, text="Long Break", command=self.long_break, font=("Arial", 12))
        self.long_break_button.pack(side=LEFT, padx=10, pady=10)

        self.pause_button = Button(self.button_frame, text="Pause", command=self.pause_timer, font=("Arial", 12))
        self.pause_button.pack(side=LEFT, padx=10, pady=10)

        # Messages
        self.message_label = Label(root,font=("Arial", 12))
        self.message_label.pack(pady=20)

        # Timer variables
        self.timer_running = False
        self.timer_seconds = 0

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_seconds = 60 * 25  
            self.message_label.config(text="Work session started!")
            self.update_timer()

    def short_break(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_seconds = 60 * 5 
            self.message_label.config(text="Short break started!")
            self.update_timer()

    def long_break(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_seconds = 60 * 15 
            self.message_label.config(text="Long break started!")
            self.update_timer()

    def pause_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.message_label.config(text="Timer paused.")
        else:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            minutes, seconds = divmod(self.timer_seconds, 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")  
            self.timer_seconds -= 1
            if self.timer_seconds > 0:
                self.root.after(1000, self.update_timer)
            else:
                self._finish_timer()

    def _finish_timer(self):
        self.timer_running = False
        self.message_label.config(text="Timer finished!")

root = Tk()
my_timer = PomodoroTimer(root)
root.mainloop()