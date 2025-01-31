import tkinter as tk  # this is use for GUI
from time import strftime  #use for time function
root = tk.Tk()          #making root window
root.title("Digital Clock")  #this is for set title 

def time():             #this functon for deside time 
    string = strftime("%H:%M:%S %p\n %D")  #this is for time format
    label.config(text=string)           #This is for text to striiing label attribute
    label.after(100,time) #this call time 1000 second
label = tk.Label(root, font=('calibri', 50, 'bold'), background="yellow", foreground="black")
label.pack(anchor="center") #label object window pack with 

time()

root.mainloop() #root object set main loop
