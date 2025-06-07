#Pomodoro App code for Pythonista 3
import time
#import sound
import datetime as dt

import tkinter as tk
from tkinter import messagebox
import winsound

class PomodoroTimer:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='pomodoro_icon.png'))
        self.root.resizable(True, True)
        self.timer_running = False
        self.root.mainloop()
        
        self.s = tk.ttk.Style()
        self.s.theme_use('clam')
        self.s.configure('TNotebook.Tab', background='#f0f0f0', foreground='black', padding=[10, 5] , font=('Helvetica', 16))
        self.s.configure('TButton', padding=6, relief='flat', background='#4CAF50', foreground='white')
        self.s.configure('TButton', font=('Helvetica', 12))
        
        #function for starting the timer
        #self.start_button = tkinter.Button(self.root, text="Start Timer", command=self.start_timer)
        #self.start_button.pack(pady=10)

    def start_timer(self):
        pass
    
    def stop_timer(self):
        pass
    
    def reset_timer(self):
        pass
    
    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    
    def play_sound(self):
        # Play a sound using winsound
        winsound.Beep(440, 1000)


PomodoroTimer()