import sys
import matplotlib.pyplot as plt
from typing import List
from typing import Type

import config

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk




class MyFrame:
    """For creating custom tkinter frame"""
    FONT_SIZE = 12
    WIDTH = 6
    PADX = 10
    PADY = 4

    """gui"""
    def __init__(self):
        self.root = tk.Tk()

    def drawConfig(self):
        self.root.title("Team Creator - Config")

        tmp1 = tk.StringVar(self.root)
        tmp1.set(config.MIN_HOURS_OVRLAP)
        spin_minhrs = tk.Spinbox(self.root,from_=0,to=24,width=self.WIDTH,textvariable=tmp1)

        tmp2 = tk.StringVar(self.root)
        tmp2.set(config.TEAM_SIZE)
        spin_tm_sz = tk.Spinbox(self.root,from_=0,to=24,width=self.WIDTH,textvariable=tmp2)

        tmp3 = tk.StringVar(self.root)
        tmp3.set(config.NUMBER_OF_TEAMS)
        spin_num_tms = tk.Spinbox(self.root,from_=0,to=24,width=self.WIDTH,textvariable=tmp3)

        txt_avail_csv = tk.Entry(self.root,width=self.WIDTH * 4)
        txt_grp_csv = tk.Entry(self.root,width=self.WIDTH * 4)

        minhours_str  = "Min Hours Overlap\t"
        team_size_str = "Members Per Team \t"
        num_of_tm_str = "How many teams   \t"
        avail_f_str   = "Name of Avail csv\t"
        grp_p_f_str   = "Name grp pri csv \t"

        lbl_minhrs = tk.Label(self.root, text = minhours_str, font = ("Arial",self.FONT_SIZE),\
                              justify="left",anchor='w')
        lbl_minhrs.grid(column = 0, row = 0,sticky=tk.W,padx=self.PADX,pady=self.PADY)
        spin_minhrs.grid(column = 1, row = 0,sticky=tk.W,padx=self.PADX,pady=self.PADY)

        lbl_tm_sz = tk.Label(self.root, text = team_size_str, font = ("Arial",self.FONT_SIZE),\
                             justify="left",anchor='w')
        lbl_tm_sz.grid(column=0,row=1,sticky=tk.W,padx=self.PADX,pady=self.PADY)
        spin_tm_sz.grid(column=1,row=1,sticky=tk.W,padx=self.PADX,pady=self.PADY)

        lbl_numtms = tk.Label(self.root, text = num_of_tm_str, font = ("Arial",self.FONT_SIZE),\
                              justify="left",anchor='w')
        lbl_numtms.grid(column=0,row=2,sticky=tk.W,padx=self.PADX,pady=self.PADY)
        spin_num_tms.grid(column=1,row=2,sticky=tk.W,padx=self.PADX,pady=self.PADY)

        lbl_avail_csv = tk.Label(self.root, text = avail_f_str, font = ("Arial",self.FONT_SIZE),\
                                 justify="left",anchor='w')
        lbl_avail_csv.grid(column=0,row=3,sticky=tk.W,padx=self.PADX,pady=self.PADY)
        txt_avail_csv.insert(0,config.CSV_AVAILABILITY_FNAME)
        txt_avail_csv.grid(column=1,row=3,sticky=tk.W,padx=self.PADX,pady=self.PADY)

        lbl_grp_csv = tk.Label(self.root, text = grp_p_f_str, font = ("Arial",self.FONT_SIZE),\
                               justify="left",anchor='w')
        lbl_grp_csv.grid(column=0,row=4,sticky=tk.W,padx=self.PADX,pady=self.PADY)
        txt_grp_csv.insert(0,config.CSV_GRP_PRIORITY_FNAME)
        txt_grp_csv.grid(column=1,row=4,sticky=tk.W,padx=self.PADX,pady=self.PADY)

        spins = [spin_minhrs,spin_tm_sz,spin_num_tms]
        entries = [txt_avail_csv,txt_grp_csv]

        btn = tk.Button(self.root, text = "Accept", bg = "white", fg = "blue",\
                        command = lambda: self.configClicked(spins,entries), font = ("Arial",12))
        btn.grid(column = 0, row = 7,padx=self.PADX,pady=self.PADY)

        self.root.mainloop()

    def configClicked(self,spins,entries):
        hrs = spins[0].get()
        sz = spins[1].get()
        tms = spins[2].get()
        avail_fn = entries[0].get()
        grp_p_fn = entries[1].get()
        try:
            hrs = int(hrs)
            sz = int(sz)
            tms = int(tms)
        except ValueError:
            print("ERROR: A val (hours/size/number of teams) could not be converted to a number!")

        config.MIN_HOURS_OVRLAP = hrs
        config.TEAM_SIZE = sz
        config.NUMBER_OF_TEAMS = tms
        config.CSV_AVAILABILITY_FNAME = avail_fn
        config.CSV_GRP_PRIORITY_FNAME = grp_p_fn
        self.root.destroy()

    def drawCmpGUI(self,lst_mems) -> list:
        '''lets user choose who to compare'''
        res = []
        self.root.title("Team Creator - Cmp Mem Avails")
        frame1 = tk.Frame(self.root)
        frame1.pack()
        frame2 = tk.Frame(self.root)
        frame2.pack()
        lbltxt = "Which members do you want to compare?"
        label = tk.Label(frame1, text = lbltxt, font = ("Arial",self.FONT_SIZE),\
                              justify="left",anchor='w')
        label.pack()

        chkbtns = []
        varlst = [] #will use to hold btn state
        for i,mem in enumerate(lst_mems):
            varlst.append(tk.IntVar(value=0))
            chkbtns.append(tk.Checkbutton(frame2,text=mem,variable=varlst[i]))
            chkbtns[i].grid(row=1 + i//4,column=i%4,padx=self.PADX,pady=self.PADY)
        self.cmp_clk_result = []
        btn = tk.Button(self.root, text = "Accept", bg = "white", fg = "blue",\
                        command = lambda: self.cmpClicked(varlst,lst_mems), font = ("Arial",12))
        btn.pack(padx=self.PADX,pady=self.PADY)

        self.root.mainloop()

    def cmpClicked(self,varlst,lst_mems):
        mems_chosen = []
        for i,var in enumerate(varlst):#check which checkboxes have been checked
            if var.get() != 1:
                continue
            mems_chosen.append(lst_mems[i])
        self.cmp_clk_result = mems_chosen
        self.root.destroy()
        
