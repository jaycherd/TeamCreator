import sys
import matplotlib.pyplot as plt

import config

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


class MyFrame:
    """gui"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title("Team Creator")
        self.WIDTH = 6
        self.FONTSIZE = 12
        self.hrs = 0
        self.sz = 0
        self.tms = 0
        self.avail_fn = ""
        self.grp_p_fn = ""

        tmpvar1 = tk.StringVar(self.root)
        tmpvar1.set(config.MIN_HOURS_OVRLAP)
        self.spin_minhrs = tk.Spinbox(self.root,from_=0,to=24,width=self.WIDTH,textvariable=tmpvar1)

        tmpvar2 = tk.StringVar(self.root)
        tmpvar2.set(config.TEAM_SIZE)
        self.spin_tm_sz = tk.Spinbox(self.root,from_=0,to=24,width=self.WIDTH,textvariable=tmpvar2)

        tmpvar3 = tk.StringVar(self.root)
        tmpvar3.set(config.NUMBER_OF_TEAMS)
        self.spin_num_tms = tk.Spinbox(self.root,from_=0,to=24,width=self.WIDTH,textvariable=tmpvar3)

        self.txt_avail_csv = tk.Entry(self.root,width=self.WIDTH * 4)
        self.txt_grp_csv = tk.Entry(self.root,width=self.WIDTH * 4)
        # frame = tk.Frame(root,padx=10,pady=10)
        # frame.grid()
        # label = tk.Label(frame, text="Hellodood")
        # button = tk.Button(frame,text="Quit",command=root.destroy)
        # label.pack()
        # button.pack()
        # root.mainloop()
    
    def drawConfig(self):
        minhours_str  = "Min Hours Overlap "
        team_size_str = "Members Per Team "
        num_of_tm_str = "How many teams "
        avail_f_str   = "Name of Avail csv "
        grp_p_f_str   = "Name grp pri csv "

        lbl_minhrs = tk.Label(self.root, text = minhours_str, font = ("Arial",self.FONTSIZE))
        lbl_minhrs.grid(column = 0, row = 0)
        self.spin_minhrs.grid(column = 1, row = 0)

        lbl_tm_sz = tk.Label(self.root, text = team_size_str, font = ("Arial",self.FONTSIZE))
        lbl_tm_sz.grid(column=0,row=1)
        self.spin_tm_sz.grid(column=1,row=1)

        lbl_numtms = tk.Label(self.root, text = num_of_tm_str, font = ("Arial",self.FONTSIZE))
        lbl_numtms.grid(column=0,row=2)
        self.spin_num_tms.grid(column=1,row=2)

        lbl_avail_csv = tk.Label(self.root, text = avail_f_str, font = ("Arial",self.FONTSIZE))
        lbl_avail_csv.grid(column=0,row=3)
        self.txt_avail_csv.insert(0,config.CSV_AVAILABILITY_FNAME)
        self.txt_avail_csv.grid(column=1,row=3)

        lbl_grp_csv = tk.Label(self.root, text = grp_p_f_str, font = ("Arial",self.FONTSIZE))
        lbl_grp_csv.grid(column=0,row=4)
        self.txt_grp_csv.insert(0,config.CSV_GRP_PRIORITY_FNAME)
        self.txt_grp_csv.grid(column=1,row=4)

        btn = tk.Button(self.root, text = "Accept", bg = "white", fg = "blue", command = self.clicked, font = ("Arial",16))
        btn.grid(column = 0, row = 7)

        self.root.mainloop()

    def clicked(self):
        self.hrs = self.spin_minhrs.get()
        self.sz = self.spin_tm_sz.get()
        self.tms = self.spin_num_tms.get()
        self.avail_fn = self.txt_avail_csv.get()
        self.grp_p_fn = self.txt_grp_csv.get()
        try:
            self.hrs = int(self.hrs)
            self.sz = int(self.sz)
            self.tms = int(self.tms)
        except ValueError:
            print("ERROR: A val (hours/size/number of teams) could not be converted to a number!")

        config.MIN_HOURS_OVRLAP = self.hrs
        config.TEAM_SIZE = self.sz
        config.NUMBER_OF_TEAMS = self.tms
        config.CSV_AVAILABILITY_FNAME = self.avail_fn
        config.CSV_GRP_PRIORITY_FNAME = self.grp_p_fn
        self.root.destroy()
