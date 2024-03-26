from tkinter import *
from tkinter.ttk import *
from time import strftime, localtime

root = Tk()
root.title("Clock Project")

def time():
    current_time = strftime('%H:%M:%S-%p')
    current_date = strftime('%d-%m-%Y')
    current_day = strftime('%A')
    string = f'\t{current_time}\t\n\t{current_date}\t\n\t{current_day}\t'
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()

mainloop()