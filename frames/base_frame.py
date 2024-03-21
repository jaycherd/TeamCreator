import tkinter as tk

from frames.utility import frame_constants as csts




class BaseFrame():
    def __init__(self,title="DEFAULT TITLE",iconpath="",scr_w_pcnt=0,scr_h_pcnt=0):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.config(bg=csts.BG_COLOR)
        self.root.resizable(width=True,height=True)
        if iconpath != "":#if not an empty string, otherwise just let it stay as default
            self.root.iconbitmap(iconpath)
        if scr_h_pcnt != 0 and scr_w_pcnt != 0:
            # Get the screen width and height
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            # Calculate window width and height as a fraction of screen width and height
            window_width = int(scr_w_pcnt * screen_width)
            window_height = int(scr_h_pcnt * screen_height)
            # Position the window in the center of the screen
            x_position = int((screen_width - window_width) / 2)
            y_position = int((screen_height - window_height) / 2)
            # Set the window size and position
            self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


        


