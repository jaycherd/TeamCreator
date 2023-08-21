from itertools import combinations
import copy

class ComboHolder:
    combos = list(list())
    set_of_combos = list(list())
    team_size = int
    number_of_teams = int
    group1 = list()
    group2 = list()
    group3 = list()
    grp1_empty_flag = bool()
    grp2_empty_flag = bool()
    grp3_empty_flag = bool()



    def __init__(self,team_size,number_of_teams,group1,group2,group3) -> None:
        self.team_size = team_size
        self.number_of_teams = number_of_teams
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.grp1_empty_flag = (len(group1) == 0)
        self.grp2_empty_flag = (len(group2) == 0)
        self.grp3_empty_flag = (len(group3) == 0)
        if self.grp2_empty_flag:
            raise Exception("Make sure there are members in group2, all other groups may be empty except for regular members group  :)")

    def createCombos(self) -> None:
        ########################################################################################################################
        #### start #### inner #### functions
        ########################################################################################################################
        def checkCombos() -> None:
            tmp = list(list())
            if(self.grp1_empty_flag == False or len(self.group1 == 1) == True): #then do grp1 checks
                for team in self.combos:
                    grp1_count_in_team = 0
                    add_this_team = True
                    for member in team:
                        if member in self.group1:
                            grp1_count_in_team += 1
                        if grp1_count_in_team == 2:
                            add_this_team = False
                            break
                    if(add_this_team):
                        tmp.append(team)
                self.combos = tmp.copy() #python makes two lists point to same data, use copy to get around this, that way when we clear, self.combos won't also clear
                tmp.clear()
            if(self.grp3_empty_flag == False or len(self.group3 == 1) == True): #then do grp3 checks, again only one member should be chosen, thus two should NOT be on same team
                tmp.clear()
                for team in self.combos:
                    grp3_count_in_team = 0
                    add_this_team = True
                    for member in team:
                        if member in self.group3:
                            grp3_count_in_team += 1
                        if grp3_count_in_team == 2:
                            add_this_team = False
                            break
                    if(add_this_team):
                        tmp.append(team)
                self.combos = tmp.copy()
                tmp.clear()
        ########################################################################################################################
        #### end #### inner #### functions
        ########################################################################################################################
        for team in combinations(self.group1 + self.group2 + self.group3,self.team_size):
            self.combos.append(team)
        print(f"\nnumber combos before checks is\t{len(self.combos)}")
        checkCombos()
        print(f"\nnumber combos after checks is\t{len(self.combos)}")
    

    def createSets(self) -> None:
        ########################################################################################################################
        #### start #### inner #### functions
        ########################################################################################################################
        def checkSets() -> None:
            emptyDict = dict()
            all_members_arr = (self.group1 + self.group2 + self.group3)
            tmp = list(list())
            for member in all_members_arr:
                emptyDict[member] = 0
            # first check for repeats, will eliminate a lot of the sets
            for team_combo in self.set_of_combos:
                num_repeats_dict = emptyDict.copy() # this will increment based on the person that we come across, if any index increases past 1 then its a repeat
                add_this_combo = True
                for team in team_combo:
                    for member in team:
                        num_repeats_dict[member] += 1
                        if (num_repeats_dict[member] == 2):
                            add_this_combo = False
                            break
                    if(add_this_combo == False):
                        break
                if(add_this_combo == True):
                    tmp.append(team_combo)
            self.set_of_combos = tmp.copy()
            tmp.clear()
            # next check for more than one group 3 member if its not an empty list
            if(self.grp3_empty_flag == False or len(self.group3 == 1) == True): #then do grp3 checks, again only one member should be chosen, thus two should NOT be on same team
                for team_combo in self.set_of_combos:
                    group3_count_in_set = 0
                    add_this_combo = True
                    for team in team_combo:
                        for member in team:
                            if(member in self.group3):
                                group3_count_in_set += 1
                            if(group3_count_in_set == 2):
                                add_this_combo = False
                                break
                        if(add_this_combo == False):
                            break
                    if(add_this_combo):
                        tmp.append(team_combo)
                self.set_of_combos = tmp.copy()
                tmp.clear()
        ########################################################################################################################
        #### end #### inner #### functions
        ########################################################################################################################    
        for team_combo in combinations(self.combos,self.number_of_teams):
            self.set_of_combos.append(team_combo)
        print(f"\nnumber sets before checks is\t{len(self.set_of_combos)}")
        checkSets()
        print(f"\nnumber sets after checks is\t{len(self.set_of_combos)}")


    
