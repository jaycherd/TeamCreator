import time
import tkinter as tk
import time
from tkinter import messagebox
from typing import List,Optional,Dict
from threading import Thread

from utility import constants as csts
from frames.base_frame import BaseFrame
from frames.utility import frame_constants as cdash
from frames.utility import fxns
from member.member import Member
from team_calcs import calcs

class HomeFrame(BaseFrame):
    def __init__(self,members: List[Member], title="HOME", iconpath="", scr_w_pcnt=.8, scr_h_pcnt=.75,group1 : List[str] = None, group2: List[str] = None, group3: List[str] = None,mem_dict = Dict[int,Member]):
        super().__init__(title, iconpath, scr_w_pcnt, scr_h_pcnt)
        self.root.configure(bg=cdash.FRAMEBORDER_CLR)
        self.members = members
        self.mems_dict = mem_dict
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.team_size = csts.team_size
        self.teams = None
        self.sets_of_teams = None
        self.teamsets_tuple = None #when order does matter, convert to tuple for no funny business
        self.numteams_strvar : Optional[tk.StringVar] = None
        self.memsper_strvar : Optional[tk.StringVar] = None
        self.hrolap_strvar : Optional[tk.StringVar] = None
        self.cmp_txt_strvar : Optional[tk.StringVar] = None
        self.cmp_txt_widget : Optional[tk.Text] = None
        
        self.topleft_frame = self.create_styled_frame(self.root,relx=0,rely=0.003,relwidth=0.333,relheight=0.5)
        self.topmid_frame = self.create_styled_frame(self.root,relx=0.333,rely=0.003,relwidth=0.333,relheight=0.5)
        self.topright_frame = self.create_styled_frame(self.root,relx=0.666,rely=0.003,relwidth=0.334,relheight=0.5)
        self.bottomleft_frame = self.create_styled_frame(self.root,relx=0,rely=0.5,relwidth=0.333,relheight=0.5)
        self.bottommid_frame = self.create_styled_frame(self.root,relx=0.333,rely=0.5,relwidth=0.667,relheight=0.5)
        #below are two frames to go within bottom mid, bcs top managed by grid, bottom by pack
        self.bottommid_innertop_frame = None
        self.bottommid_innerbot_frame = None 
        
        self.setup_topleft_frame()
        self.setup_topmid_frame()
        self.setup_topright_frame()
        self.setup_bottomleft_frame()
        self.setup_bottommid_frame()

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
    
    def create_styled_frame(self, parent, relx, rely, relwidth, relheight, bg=cdash.BG_COLOR,border=True,place=True):
        frame = tk.Frame(parent, bg=bg)
        if border:
            frame.configure(highlightbackground=cdash.FRAMEBORDER_CLR,highlightcolor=cdash.FRAMEBORDER_CLR,highlightthickness=cdash.BORDERWIDTH)
        if place:
            frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return frame
    
    def addlbl(self,parent,txt: str,location=tk.TOP,font=cdash.FONT,bd=0,relief=None,style='pack',row=0,col=0,sticky='E',padx=2,pady=2,wrap=False):
        label = tk.Label(parent,text=txt)
        label.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=font,bd=bd,relief=relief)
        if wrap:
            label.config(justify=tk.LEFT,wraplength=self.root.winfo_width()/3)
            label.grid(row=row,column=col,padx=padx)
        elif style == 'pack':
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

    def addtxt(self,parent,txt: str="", location=tk.TOP,yscrlcmd=None,style='pack',row=0,col=0,stickto='E',disable=True):
        text_widget = tk.Text(parent, wrap=tk.WORD)
        text_widget.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT)
        text_widget.configure(yscrollcommand=yscrlcmd)
        text_widget.config(font=cdash.FONT)
        text_widget.insert(tk.END, txt)
        if disable:
            text_widget.config(state=tk.DISABLED) #must be changed later if you want add txt
        if style == 'pack':
            text_widget.pack(fill=tk.BOTH,expand=True,side=location)
        elif style == 'grid':
            text_widget.grid(row=row,column=col,sticky=stickto)
        return text_widget
    
    def addspinbox(self,parent,location=tk.TOP,pady=0,padx=0,fxn=None,style='pack',row=0,col=0,sticky='E',min=0,maks=100,incr=0.25,format='%.2f',stvar=0):
        spin_box = tk.Spinbox(parent,from_=min,to=maks,increment=incr,format=format,textvariable=stvar)
        spin_box.configure(bg=cdash.BG_COLOR,fg=cdash.FG_COLOR,font=cdash.FONT,width=cdash.SB_W)
        spin_box.grid(row=row,column=col,sticky=sticky)
    
    def addscrollbar(self,parent,style='pack',row=0,col=0):
        scrollbar = tk.Scrollbar(parent)
        if style == 'pack':
            scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        else:
            scrollbar.configure(orient=tk.VERTICAL)
            scrollbar.grid(row=row,column=col,sticky=tk.N+tk.S)
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
    
    def setup_bottomleft_frame(self):
        self.addlbl(self.bottomleft_frame,txt="",location=tk.TOP,font=cdash.TINYFONT,style='grid',row=0,col=0,padx=cdash.PADX)
        self.addbtn(self.bottomleft_frame,txt="Generate Sets",location=tk.TOP,padx=cdash.PADX,
                    pady=cdash.PADY,fxn=self.generate_btn_clicked,style='grid',row=1,col=0,sticky='W')

        num_teams_str     = "Num teams:  "
        self.addlbl(self.bottomleft_frame,txt=num_teams_str,font=cdash.FONT,style='grid',row=2,col=0,sticky='W',padx=cdash.PADX)
        self.numteams_strvar = tk.StringVar(self.bottomleft_frame)
        self.numteams_strvar.set(csts.number_of_teams)
        self.addspinbox(self.bottomleft_frame,style='grid',row=2,col=1,sticky='E',min=0,maks=100,incr=1,format='%.0f',stvar=self.numteams_strvar)

        mems_per_team_str = "Mems/team:  "
        self.addlbl(self.bottomleft_frame,txt=mems_per_team_str,font=cdash.FONT,style='grid',row=3,col=0,sticky='W',padx=cdash.PADX)
        self.memsper_strvar = tk.StringVar(self.bottomleft_frame)
        self.memsper_strvar.set(csts.team_size)
        self.addspinbox(self.bottomleft_frame,style='grid',row=3,col=1,sticky='E',min=0,maks=100,incr=1,format='%.0f',stvar=self.memsper_strvar)

        hr_olap_txt       = "Hrs overlap:"
        self.addlbl(self.bottomleft_frame,txt=hr_olap_txt,location=tk.TOP,font=cdash.FONT,style='grid',row=4,col=0,sticky='W',padx=cdash.PADX)
        self.hrolap_strvar = tk.StringVar(self.bottomleft_frame)
        self.hrolap_strvar.set(csts.MIN_HRS_OLAP)
        self.addspinbox(self.bottomleft_frame,style='grid',row=4,col=1,sticky='E',min=0,maks=100,incr=0.25,format='%.2f',stvar=self.hrolap_strvar)
    
    def setup_bottommid_frame(self):
        self.bottommid_innertop_frame = self.create_styled_frame(self.bottommid_frame,relx=0,rely=0,relwidth=1,relheight=.65,border=False,place=False)
        self.bottommid_innerbot_frame = self.create_styled_frame(self.bottommid_frame,relx=0,rely=.65,relwidth=1,relheight=.45,border=False,place=False)
        self.bottommid_innertop_frame.grid(row=0,sticky='W')
        self.bottommid_innerbot_frame.grid(row=1,sticky='W')
        self.setup_bottommid_innertop_frame()
        self.setup_bottommid_innerbot_frame()
      
    def setup_bottommid_innertop_frame(self):
        self.addlbl(self.bottommid_innertop_frame,txt="",location=tk.TOP,font=cdash.TINYFONT,style='grid',row=0,col=0,padx=cdash.PADX)
        self.addbtn(self.bottommid_innertop_frame,txt="Compare Members",location=tk.TOP,padx=cdash.PADX,
                    pady=cdash.PADY,fxn=self.compare_button_clicked,style='grid',row=1,col=0,sticky='W')
        txt = "Enter mems to compare (comma separated):\nCan enter 1 or more mems"
        self.bottommid_frame.update_idletasks()
        self.addlbl(self.bottommid_innertop_frame,txt=txt,location=tk.TOP,font=cdash.FONT,style='grid',row=2,col=0,padx=cdash.PADX,wrap=True)
    
    def setup_bottommid_innerbot_frame(self):
        scrollbar = self.addscrollbar(self.bottommid_innerbot_frame)
        txt = "Member1 , Member2 , Member3[optional] , ..."
        self.cmp_txt_widget = self.addtxt(self.bottommid_innerbot_frame,location=tk.LEFT,yscrlcmd=scrollbar.set,txt=txt)
        self.cmp_txt_widget.config(state=tk.NORMAL)
    

    def generate_btn_clicked(self):
        numteams = self.numteams_strvar.get()
        memsper = self.memsper_strvar.get()
        olap = self.hrolap_strvar.get()
        res = fxns.homeframe_inputs_isvalid(numteams=numteams,memsper=memsper,olap=olap,memsdict=self.mems_dict,numleaders=len(self.group1))
        if res[0]:
            ### portion between these #### could be threaded, lots of calcs, need to be done ###################################################
            numteams,memsper,olap = res[2]
            
            start_time = time.perf_counter() #tmp
            self.teams,self.teamstr_to_startend_intersection_map = calcs.generate_teams(mems=self.members,grp1=self.group1,grp2=self.group2,
                             grp3=self.group3,team_size=memsper,mems_dict=self.mems_dict,olap=olap)
            self.sets_of_teams = calcs.generate_sets_of_teams(teams=self.teams,grp1=self.group1,
                                                     grp2=self.group2,
                                                     grp3=self.group3,
                                                     num_teams=numteams)
            
            end_time = time.perf_counter() #tmp
            print(f"team/set generation took {end_time - start_time} seconds")

            # self.teamstr_to_startend_intersection_map = calcs.intersect_team_avail_mins(teamsets=self.sets_of_teams,numteams=numteams,memsper=memsper,olap=olap,members=self.members,mems_dict=self.mems_dict)
            self.teamsets_tuple = tuple(self.sets_of_teams)            

            # print(f"\n\n\nteam intersection map -> {self.teamstr_to_startend_intersection_map}")

            """this indexes the dictionary which should no longer be necessary as all the teams that we determine
            to be valid will automatically be valid at this point because when we generate sets we only use valid teams\
            and we delete duplicates so no more checking needs to happen and we should probs skip this all together"""
            teamset_to_startend_map = calcs.convert_team_intersections(teams_intersected_map=self.teamstr_to_startend_intersection_map,mems_dict=self.mems_dict,teamsets=self.teamsets_tuple)
            # print(f"\n\nteamset to startend map -> {teamset_to_startend_map}")

            end_time_overall = time.perf_counter() #tmp
            print(f"all set generation fxns took {end_time_overall - start_time} seconds")

            self.view_teams_modal_window(teamset_to_startend_map,olap)
            
            
            ######################################################################################################################################            
        else:
            if res[1] == 0:
                messagebox.showerror("Error", "make sure the number of teams is a valid number, ie: 1, 2, 3, 4, 5, 6, etc...")
            elif res[1] == 1:
                messagebox.showerror("Error", "make sure the members per team is a valid number, ie: 1, 2, 3, 4, 5, 6, etc...")
            elif res[1] == 2:
                messagebox.showerror("Error", "make sure that the hrs of overlap is a valid number, ie: 0.00, 0.01, 0.02, 0.03, etc...")
            elif res[1] == 3:
                messagebox.showerror("Error", "invalid number of teams and members per team combo make sure number of teams * mems per <= total members")
            elif res[1] == 4:
                messagebox.showerror("Error",f"Too many teams, not enough leaders")
    
    def compare_button_clicked(self):
        valid_names = set()
        for member in self.members:
            valid_names.add(member.name)
        cmp_input_str = self.cmp_txt_widget.get('1.0',tk.END).rstrip('\n')
        chk_res = calcs.check_cmp_input(cmp_input_str,valid_names=valid_names)
        if chk_res[0] == -1:
            messagebox.showerror("Error",f"Name '{chk_res[1]}' not found," +
                                 "check your input files make sure you input name exactly same" +
                                 ", and make sure names match!")
        elif chk_res[0] == -2:
            messagebox.showerror("Error","Remove Trailing Comma PLEEEEAAAASE")
        else:#the input was valid
            cmp_input_lst = cmp_input_str.replace(' ','').split(',')
            mem_ids = calcs.convert_names2id(cmp_input_lst,self.members)
            common_times = calcs.find_cmp_olap(ids=mem_ids,mems_dict=self.mems_dict)
            compressed_common_times = tuple()
            if common_times:
                compressed_common_times = calcs.convert_intersection(common_times)
            self.view_cmp_olap_modal_window(compressed_common_times,cmp_input_lst)
            # ic(compressed_common_times)
            



    def view_teams_modal_window(self,teamstr_to_startend_map,olap):
        modal_win = self.make_modal_window(title="Teams")
        scrollbar = self.addscrollbar(modal_win)
        txt = f"Found {len(teamstr_to_startend_map)} team sets with {olap} hours in common\n"
        txtwidget = self.addtxt(modal_win,txt=txt,location=tk.LEFT,yscrlcmd=scrollbar.set,disable=False)

        counter = 1
        #next have to fill txt widget with teams and their common time
        for key,val in teamstr_to_startend_map.items():
            team_mems_strs = fxns.get_names_from_memids_tup(self.teamsets_tuple[int(key)],self.mems_dict)
            txt = f"\nTeamSet {counter}\n"
            counter += 1
            txtwidget.insert(tk.END,txt)

            for i,team_mems_str in enumerate(team_mems_strs):
                if i != 0:
                    txtwidget.insert(tk.END,'\n')
                # print(f"\nteam mems str -> {team_mems_str}\nval -> {val[i]}\nval -> {val}" +
                #       f"\nkey -> {key}")
                txt2 = f"[{team_mems_str}]:\n{fxns.draw_start_end(val[i])}"
                txtwidget.insert(tk.END,txt2)
            txtwidget.insert(tk.END,'\n')

    def view_cmp_olap_modal_window(self,start_end_tups,cmp_lst):#[Tuple[starts],Tuple[ends]]
        modal_win = self.make_modal_window(title="Availability Comparison")
        scrollbar = self.addscrollbar(modal_win)
        txt = ','.join(cmp_lst) + ':'
        txtwidget = self.addtxt(modal_win,txt=txt,location=tk.LEFT,yscrlcmd=scrollbar.set,disable=False)
        if not start_end_tups:
            txt2 = "\nNo common time was found between these mems"
        else:
            txt2 = f"\n{fxns.draw_start_end(start_end_tups)}"
        txtwidget.insert(tk.END,txt2)
        txtwidget.insert(tk.END,'\n')

        

        