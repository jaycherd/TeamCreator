import tkinter as tk
from tkinter import messagebox
from typing import List,Optional,Dict
from threading import Thread
from icecream import ic

from utility import constants as csts
from frames.base_frame import BaseFrame
from frames.utility import frame_constants as cdash
from frames.utility import fxns
from member.member import Member
from team_calcs import calcs

class HomeFrame(BaseFrame):
    def __init__(self,members: List[Member], title="HOME", iconpath="", scr_w_pcnt=.8, scr_h_pcnt=.75,group1 : List[str] = None, group2: List[str] = None, group3: List[str] = None,mem_dict = Dict[int,Member]):
        super().__init__(title, iconpath, scr_w_pcnt, scr_h_pcnt)
        self.members = members
        self.mems_dict = mem_dict
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.team_size = csts.team_size
        self.teams = None
        self.sets_of_teams = None
        self.teamsets_tuple = None #when order does matter, convert to tuple for no funny business
        self.numteams_strvar = Optional[tk.StringVar]
        self.memsper_strvar = Optional[tk.StringVar]
        self.hrolap_strvar = Optional[tk.StringVar]
        
        self.topleft_frame = self.create_styled_frame(self.root,relx=0,rely=0,relwidth=0.333,relheight=0.5)
        self.topmid_frame = self.create_styled_frame(self.root,relx=0.333,rely=0,relwidth=0.333,relheight=0.5)
        self.topright_frame = self.create_styled_frame(self.root,relx=0.666,rely=0,relwidth=0.334,relheight=0.5)
        self.bottom_frame = self.create_styled_frame(self.root,relx=0,rely=0.5,relwidth=1,relheight=0.5)
        
        self.setup_topleft_frame()
        self.setup_topmid_frame()
        self.setup_topright_frame()
        self.setup_bottom_frame()

        # thread = Thread(target=self.generate_teams_and_sets)
        # thread.start()

        self.root.mainloop()

    # def generate_teams_and_sets(self):
    #     self.teams = calcs.generate_teams(mems=self.members,grp1=self.group1,grp2=self.group2,
    #                          grp3=self.group3,team_size=self.team_size)
    #     self.sets_of_teams = calcs.generate_sets_of_teams(teams=self.teams,grp1=self.group1,
    #                                                  grp2=self.group2,
    #                                                  grp3=self.group3,
    #                                                  num_teams=csts.number_of_teams)
        # ic(len(self.sets_of_teams))

    def make_modal_window(self,title):
        modal_win = tk.Toplevel(self.root)
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Calculate window width and height as a fraction of screen width and height
        window_width = int(.6 * screen_width)
        window_height = int(.6 * screen_height)
        # Position the window in the center of the screen
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        # Set the window size and position
        modal_win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        modal_win.configure(bg=cdash.BG_COLOR)
        modal_win.resizable(width=True,height=True)
        modal_win.title(title)
        modal_win.grab_set() #makes it modal, aka cant alter home frame until user closes window
        return modal_win
    
    def create_styled_frame(self, parent, relx, rely, relwidth, relheight, bg=cdash.BG_COLOR):
        frame = tk.Frame(parent, bg=bg)
        frame.configure(highlightbackground=cdash.FRAMEBORDER_CLR,highlightcolor=cdash.FRAMEBORDER_CLR,highlightthickness=cdash.BORDERWIDTH)
        frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return frame
    
    def addlbl(self,parent,txt: str,location=tk.TOP,font=cdash.FONT,bd=0,relief=None,style='pack',row=0,col=0,sticky='E',padx=2,pady=2):
        label = tk.Label(parent,text=txt)
        label.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=font,bd=bd,relief=relief)
        if style == 'pack':
            label.pack(side=location)
        else:
            label.grid(row=row,column=col,sticky=sticky,padx=padx,pady=pady)

    def addbtn(self,parent,txt: str, location=tk.TOP,pady=0,padx=2,fxn=None,style='pack',row=0,col=0,sticky='E',width=20):
        btn = tk.Button(parent,text=txt)
        btn.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT)
        btn.configure(padx=padx,pady=pady,activebackground=cdash.MY_GREEN)
        btn.configure(command=fxn)
        if style == 'pack':
            btn.pack(side=location)
        else:
            btn.grid(row=row,column=col,sticky=sticky,padx=padx)

    def addtxt(self,parent,txt: str="", location=tk.TOP,yscrlcmd=None):
        text_widget = tk.Text(parent, wrap=tk.WORD)
        text_widget.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT)
        text_widget.configure(yscrollcommand=yscrlcmd)
        text_widget.config(font=cdash.FONT)
        text_widget.insert(tk.END, txt)
        text_widget.pack(fill=tk.BOTH,expand=True,side=location)
        return text_widget
    
    def addspinbox(self,parent,location=tk.TOP,pady=0,padx=0,fxn=None,style='pack',row=0,col=0,sticky='E',min=0,maks=100,incr=0.25,format='%.2f',stvar=0):
        spin_box = tk.Spinbox(parent,from_=min,to=maks,increment=incr,format=format,textvariable=stvar)
        spin_box.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT,width=cdash.SB_W)
        spin_box.grid(row=row,column=col,sticky=sticky)
    
    def addscrollbar(self,parent):
        scrollbar = tk.Scrollbar(parent)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        return scrollbar

    def setup_topleft_frame(self):
        self.addlbl(self.topleft_frame,txt="Group 01")
        grpstr = fxns.generate_grp_string(group=self.group1,mems_dict = self.mems_dict)
        self.addtxt(self.topleft_frame,txt=grpstr,location=tk.TOP)
  
    def setup_topmid_frame(self):
        self.addlbl(self.topmid_frame,txt="Group 02")
        grpstr = fxns.generate_grp_string(group=self.group2,mems_dict = self.mems_dict)
        self.addtxt(self.topmid_frame,txt=grpstr,location=tk.TOP)
    
    def setup_topright_frame(self):
        self.addlbl(self.topright_frame,txt="Group 03")
        grpstr = fxns.generate_grp_string(group=self.group3,mems_dict = self.mems_dict)
        self.addtxt(self.topright_frame,txt=grpstr,location=tk.TOP)
    
    def setup_bottom_frame(self):
        self.addlbl(self.bottom_frame,txt="",location=tk.TOP,font=cdash.TINYFONT,style='grid',row=0,col=0)
        self.addbtn(self.bottom_frame,txt="Generate Sets",location=tk.TOP,
                    pady=12,fxn=self.generate_btn_clicked,style='grid',row=1,col=0,sticky='W')

        num_teams_str     = "Number of teams:                        "
        self.addlbl(self.bottom_frame,txt=num_teams_str,font=cdash.FONT,style='grid',row=2,col=0,sticky='W')
        self.numteams_strvar = tk.StringVar(self.bottom_frame)
        self.numteams_strvar.set(csts.number_of_teams)
        self.addspinbox(self.bottom_frame,style='grid',row=2,col=1,sticky='E',min=0,maks=100,incr=1,format='%.0f',stvar=self.numteams_strvar)

        mems_per_team_str = "How many members will be on each team:  "
        self.addlbl(self.bottom_frame,txt=mems_per_team_str,font=cdash.FONT,style='grid',row=3,col=0,sticky='W')
        self.memsper_strvar = tk.StringVar(self.bottom_frame)
        self.memsper_strvar.set(csts.team_size)
        self.addspinbox(self.bottom_frame,style='grid',row=3,col=1,sticky='E',min=0,maks=100,incr=1,format='%.0f',stvar=self.memsper_strvar)

        hr_olap_txt       = "Hrs overlap to be a valid set of teams: "
        self.addlbl(self.bottom_frame,txt=hr_olap_txt,location=tk.TOP,font=cdash.FONT,style='grid',row=4,col=0,sticky='W')
        self.hrolap_strvar = tk.StringVar(self.bottom_frame)
        self.hrolap_strvar.set(csts.MIN_HRS_OLAP)
        self.addspinbox(self.bottom_frame,style='grid',row=4,col=1,sticky='E',min=0,maks=100,incr=0.25,format='%.2f',stvar=self.hrolap_strvar)
    

    def generate_btn_clicked(self):
        numteams = self.numteams_strvar.get()
        memsper = self.memsper_strvar.get()
        olap = self.hrolap_strvar.get()
        res = fxns.homeframe_inputs_isvalid(numteams=numteams,memsper=memsper,olap=olap,memsdict=self.mems_dict)
        if res[0]:
            ### portion between these #### could be threaded, lots of calcs, need to be done ###################################################
            numteams,memsper,olap = res[2]
            
            self.teams = calcs.generate_teams(mems=self.members,grp1=self.group1,grp2=self.group2,
                             grp3=self.group3,team_size=memsper)
            self.sets_of_teams = calcs.generate_sets_of_teams(teams=self.teams,grp1=self.group1,
                                                     grp2=self.group2,
                                                     grp3=self.group3,
                                                     num_teams=numteams)

            team_intersection_map = calcs.intersect_team_avail_mins(teamsets=self.sets_of_teams,numteams=numteams,memsper=memsper,olap=olap,members=self.members,mems_dict=self.mems_dict)
            self.teamsets_tuple = tuple(self.sets_of_teams)
            id_teamsets_w_val_olap = calcs.find_teams_w_olap(teams_intersected_map=team_intersection_map,mems_dict=self.mems_dict,teamsets=self.teamsets_tuple,olap=olap)
            teamset_to_startend_map = calcs.convert_team_intersections(teams_intersected_map=team_intersection_map,mems_dict=self.mems_dict,teamsets=self.teamsets_tuple,teamset_ids=id_teamsets_w_val_olap)
            self.view_teams_modal_window(teamset_to_startend_map,olap)
            ######################################################################################################################################
            
        else:
            if res[1] == 0:
                messagebox.showerror("Error", "make sure the number of teams is a valid number, ie: 1, 2, 3, 4, 5, 6, etc...")
            elif res[1] == 1:
                messagebox.showerror("Error", "make sure the members per team is a valid number, ie: 1, 2, 3, 4, 5, 6, etc...")
            elif res[1] == 2:
                messagebox.showerror("Error", "make sure that the hrs of overlap is a valid number, ie: 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, etc...")
            elif res[1] == 3:
                messagebox.showerror("Error", "invalid number of teams and members per team combo make sure number of teams * mems per <= total members")


    def view_teams_modal_window(self,teamset_to_startend_map,olap):
        modal_win = self.make_modal_window(title="Teams")
        scrollbar = self.addscrollbar(modal_win)
        txtwidget = self.addtxt(modal_win,location=tk.LEFT,yscrlcmd=scrollbar.set)

        txt = f"Found {len(teamset_to_startend_map)} team sets with {olap} hours in common\n"
        txtwidget.insert(tk.END,txt)

        counter = 1
        #next have to fill txt widget with teams and their common time
        for key,val in teamset_to_startend_map.items():
            team_mems_strs = fxns.get_names_from_memids_tup(self.teamsets_tuple[key],self.mems_dict)
            txt = f"\nTeamSet {counter}\n"
            counter += 1
            txtwidget.insert(tk.END,txt)

            for i,team_mems_str in enumerate(team_mems_strs):
                if i != 0:
                    txtwidget.insert(tk.END,'\n')
                txt2 = f"[{team_mems_str}]:\n{fxns.draw_start_end(val[i])}"
                txtwidget.insert(tk.END,txt2)
            txtwidget.insert(tk.END,'\n')

        

        