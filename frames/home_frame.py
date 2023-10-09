import tkinter as tk
from typing import List

from icecream import ic
from frames.base_frame import BaseFrame
from frames.utility import frame_constants as cdash
from frames.utility import fxns

class HomeFrame(BaseFrame):
    def __init__(self, title="HOME", iconpath="", scr_w_pcnt=.8, scr_h_pcnt=.75,group1 : List[str] = None, group2: List[str] = None, group3: List[str] = None):
        super().__init__(title, iconpath, scr_w_pcnt, scr_h_pcnt)
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        
        self.topleft_frame = self.create_styled_frame(self.root,relx=0,rely=0,relwidth=0.333,relheight=0.5)
        self.topmid_frame = self.create_styled_frame(self.root,relx=0.333,rely=0,relwidth=0.333,relheight=0.5)
        self.topright_frame = self.create_styled_frame(self.root,relx=0.666,rely=0,relwidth=0.334,relheight=0.5)
        self.bottom_frame = self.create_styled_frame(self.root,relx=0,rely=0.5,relwidth=1,relheight=0.5,bg='orange')
        
        self.setup_topleft_frame()
        self.setup_topmid_frame()
        self.setup_topright_frame()
        self.setup_bottom_frame()



        self.root.mainloop()

    def create_styled_frame(self, parent, relx, rely, relwidth, relheight, bg=cdash.BG_COLOR):
        frame = tk.Frame(parent, bg=bg)
        frame.configure(highlightbackground=cdash.FRAMEBORDER_CLR,highlightcolor=cdash.FRAMEBORDER_CLR,highlightthickness=cdash.BORDERWIDTH)
        frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return frame
    
    def addlbl(self,parent,txt: str,location=tk.TOP,font=cdash.FONT,bd=0,relief=None):
        label = tk.Label(parent,text=txt)
        label.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=font,bd=bd,relief=relief)
        label.pack(side=location)
    
    def addbtn(self,parent,txt: str, location=tk.TOP,pady=0,padx=0,fxn=None):
        btn = tk.Button(parent,text=txt)
        btn.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT)
        btn.configure(padx=padx,pady=pady,activebackground=cdash.MY_GREEN)
        btn.configure(command=fxn)
        btn.pack(side=location)

    def addtxt(self,parent,txt: str, location=tk.TOP):
        text_widget = tk.Text(parent, wrap=tk.WORD)
        text_widget.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT)
        text_widget.insert(tk.END, txt)
        text_widget.pack(fill=tk.BOTH,expand=True,side=location)
    
    def setup_topleft_frame(self):
        self.addlbl(self.topleft_frame,txt="Group 01")
        grpstr = fxns.generate_grp_string(group=self.group1)
        self.addtxt(self.topleft_frame,txt=grpstr,location=tk.TOP)
  
    def setup_topmid_frame(self):
        self.addlbl(self.topmid_frame,txt="Group 02")
        grpstr = fxns.generate_grp_string(group=self.group2)
        self.addtxt(self.topmid_frame,txt=grpstr,location=tk.TOP)
    
    def setup_topright_frame(self):
        self.addlbl(self.topright_frame,txt="Group 03")
        grpstr = fxns.generate_grp_string(group=self.group3)
        self.addtxt(self.topright_frame,txt=grpstr,location=tk.TOP)
    
    def setup_bottom_frame(self):
        self.addlbl(self.bottom_frame,txt="",location=tk.TOP,font=cdash.TINYFONT)
        self.addbtn(self.bottom_frame,txt="Generate Teams",location=tk.TOP,
                    pady=12,fxn=self.generate_btn_clicked)

    

    def generate_btn_clicked(self):
        ic()

