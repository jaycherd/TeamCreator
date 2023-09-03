"""Module for eficient combination calculations"""
from itertools import combinations

class ComboHolder:
    """"class to create/check team combinations and sets"""
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

    def __init__(self,team_size,number_of_teams,group1,group2,group3,prf_flag=False) -> None:
        self.prf_flag = prf_flag
        self.team_size = team_size
        self.number_of_teams = number_of_teams
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.grp1_empty_flag = len(group1) == 0
        self.grp2_empty_flag = len(group2) == 0
        self.grp3_empty_flag = len(group3) == 0
        if self.grp2_empty_flag:
            raise ValueError("Make sure there are members in group2, all other groups may be empty except for regular members group  :)")

    def createCombos(self) -> None:
        ########################################################################################################################
        #### start #### inner #### functions
        ########################################################################################################################
        def checkCombos() -> None:
            tmp = []
            if self.grp1_empty_flag is False or len(self.group1) != 1: #then do grp1 checks
                for team in self.combos:
                    grp1_count_in_team = 0
                    add_this_team = True
                    for member in team:
                        if member in self.group1:
                            grp1_count_in_team += 1
                        if grp1_count_in_team == 2:
                            add_this_team = False
                            break
                    if add_this_team:
                        tmp.append(team)
                #python makes two lists point to same data, use copy to get around this
                self.combos = tmp.copy()
                tmp.clear()
            #then do grp3 checks, again only one mem should be chosen
            if(self.grp3_empty_flag is False or len(self.group3 != 1)):
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
                    if add_this_team:
                        tmp.append(team)
                self.combos = tmp.copy()
                tmp.clear()
        #######################################################
        #### end #### inner #### functions
        #######################################################
        for team in combinations(self.group1 + self.group2 + self.group3,self.team_size):
            self.combos.append(team)
        out_str = "\nnumber combos before checks is "
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.combos))
        checkCombos()
        out_str = "\nnumber combos before checks is "
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.combos))

    def createSets(self) -> None:
        """Function for set creation and checking"""
        ########################################################
        #### start #### inner #### functions
        ########################################################
        def checkSets() -> None:
            empty_dict = {}
            all_members_arr = self.group1 + self.group2 + self.group3
            tmp = []
            for member in all_members_arr:
                empty_dict[member] = 0
            # first check for repeats, will eliminate a lot of the sets
            for team_combo in self.set_of_combos:
                #incrmnt based on person we come across, if any index incrs past 1 then its repeat
                num_repeats_dict = empty_dict.copy()
                add_this_combo = True
                for team in team_combo:
                    for member in team:
                        num_repeats_dict[member] += 1
                        if num_repeats_dict[member] == 2:
                            add_this_combo = False
                            break
                    if add_this_combo is False:
                        break
                if add_this_combo is True:
                    tmp.append(team_combo)
            self.set_of_combos = tmp.copy()
            tmp.clear()
            # next check for more than one group 3 member if its not an empty list
            #then do grp3 checks, again only one mem should be chosen, two NOT be on same team
            if self.grp3_empty_flag is False or len(self.group3) != 1:
                for team_combo in self.set_of_combos:
                    group3_count_in_set = 0
                    add_this_combo = True
                    for team in team_combo:
                        for member in team:
                            if member in self.group3:
                                group3_count_in_set += 1
                            if group3_count_in_set == 2:
                                add_this_combo = False
                                break
                        if add_this_combo is False :
                            break
                    if add_this_combo:
                        tmp.append(team_combo)
                self.set_of_combos = tmp.copy()
                tmp.clear()
        ########################################################
        #### end #### inner #### functions
        ########################################################   
        for team_combo in combinations(self.combos,self.number_of_teams):
            self.set_of_combos.append(team_combo)
        out_str = "\nnumber sets before checks is "
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.set_of_combos))
        checkSets()
        out_str = "\nnumber sets after checks is "
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.set_of_combos))
