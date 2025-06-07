#Pomodoro App code for Pythonista 3
import time
#import sound
import datetime as dt

import tkinter as tk
from tkinter import messagebox, ttk
import winsound

class PomodoroTimer:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='pomodoro_icon.png'))
        self.root.resizable(True, True)

        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure('TNotebook.Tab', background='#f0f0f0', foreground='black', padding=[10, 5] , font=('Helvetica', 16))
        self.s.configure('TButton', font=('Helvetica', 12))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(expand=True, fill='both', padx=10, pady=10)

        self.tab1= ttk.Frame(self.tabs, width=300, height=200)
        self.tab2 = ttk.Frame(self.tabs, width=300, height=200)
        self.tab3 = ttk.Frame(self.tabs, width=300, height=200)
        
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=('Helvetica', 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break = ttk.Label(self.tab2, text="05:00", font=('Helvetica', 48))
        self.short_break.pack(pady=20)

        self.long_break = ttk.Label(self.tab3, text="15:00", font=('Helvetica', 48))
        self.long_break.pack(pady=20)
        
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(expand=True, padx=10, pady=10)
        self.stop_button = ttk.Button(self.grid_layout, text="Stop", command=self.stop_timer)
        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer)
        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_timer)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)
        self.reset_button.grid(row=0, column=2, padx=5, pady=5)
        
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoro Counter: 0", font=('Helvetica', 16), anchor='center')
        self.pomodoro_counter_label.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='ShortBreak')
        self.tabs.add(self.tab3, text='LongBreak')

        self.pomodoro_counter = 0
        self.pomodoro_duration = 25 * 60  # 25 minutes in seconds
        self.short_break_duration = 5 * 60  # 5 minutes in seconds
        self.long_break_duration = 15 * 60  # 15 minutes in seconds
        self.current_timer = None
        self.stopped = False
        
        self.root.mainloop()

        
    def start_timer(self):
       self.stopped = False
       timer_id = self.tabs.index(self.tabs.select()) + 1
       
       if timer_id == 1:  # Pomodoro
           full_seconds = self.pomodoro_duration
           while full_seconds > 0 and not self.stopped:
               minutes, seconds = divmod(full_seconds, 60)
               self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
               self.root.update()
               time.sleep(1)
               full_seconds -= 1
           if not self.stopped:
               self.current_timer = None
               self.pomodoro_counter += 1
               self.pomodoro_counter_label.config(text=f"Pomodoro Counter: {self.pomodoro_counter}")
               self.show_message("Pomodoro Complete", "Time for a break!")
               self.play_sound()
               if self.pomodoro_counter % 4 == 0:
                   self.tabs.select(self.tab3)
                   self.start_timer()  # Start Long Break
               else:
                    self.tabs.select(self.tab2)
                    self.start_timer()  # Start Short Break

       elif timer_id == 2:  # Short Break
           full_seconds = self.short_break_duration
           while full_seconds > 0 and not self.stopped:
               minutes, seconds = divmod(full_seconds, 60)
               self.short_break.config(text=f"{minutes:02d}:{seconds:02d}")
               self.root.update()
               time.sleep(1)
               full_seconds -= 1
           
           if not self.stopped:
               self.current_timer = None
               self.show_message("Short Break Complete", "Time to get back to work!")
               self.play_sound()
               self.tabs.select(self.tab1)
               self.start_timer()  # Start Pomodoro

       elif timer_id == 3:  # Long Break
           full_seconds = self.long_break_duration
           while full_seconds > 0 and not self.stopped:
               minutes, seconds = divmod(full_seconds, 60)
               self.long_break.config(text=f"{minutes:02d}:{seconds:02d}")
               self.root.update()
               time.sleep(1)
               full_seconds -= 1

           if not self.stopped:
               self.current_timer = None
               self.show_message("Long Break Complete", "Time to get back to work!")
               self.play_sound()
               self.tabs.select(self.tab1)
               self.start_timer()  # Start Pomodoro
               

    def stop_timer(self):
        self.stopped = True

    def reset_timer(self):
        self.stopped = True
        self.pomodoro_duration = 25 * 60
        self.short_break_duration = 5 * 60
        self.long_break_duration = 15 * 60
        self.current_timer = None
        self.stopped = False
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break.config(text="05:00")
        self.long_break.config(text="15:00")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    
    def play_sound(self):
        # Play a sound using winsound aesthetic
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)


PomodoroTimer()