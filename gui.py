import sys
import matplotlib.pyplot as plt

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

class MyFrame:
    """gui"""
    def __init__(self):
        root = tk.Tk()
        root.geometry('350x200')
        root.title("Team Creator")
        frame = tk.Frame(root,padx=10,pady=10)
        frame.grid()
        label = tk.Label(frame, text="Hellodood")
        button = tk.Button(frame,text="Quit",command=root.destroy)
        label.pack()
        button.pack()
        root.mainloop()
