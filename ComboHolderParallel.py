from itertools import combinations
import multiprocessing as mp
import copy




class ComboHolder:
    combos = list(list())
    set_of_combos = list(list())
    set_of_combos_checked = list(list())
    set_of_combos_split = list(list()) #split up version for parallelization
    team_size = int
    number_of_teams = int
    group1 = list()
    group2 = list()
    group3 = list()
    grp1_empty_flag = bool()
    grp2_empty_flag = bool()
    grp3_empty_flag = bool()

    all_results = list(list()) #for use with parallel procs
    list_repeats_dict = list() #need sep list for each process running

# 


    def __init__(self,team_size,number_of_teams,group1,group2,group3) -> None:
        self.team_size = team_size
        self.number_of_teams = number_of_teams
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.grp1_empty_flag = (len(group1) == 0)
        self.grp2_empty_flag = (len(group2) == 0)
        self.grp3_empty_flag = (len(group3) == 0)
        self.all_members = group1 + group2 + group3
        if self.grp2_empty_flag:
            raise Exception("Make sure there are members in group2, all other groups may be empty except for regular members group  :)")
        
        #for parallel
        self.pool = mp.Pool(mp.cpu_count())
        self.num_cpus = mp.cpu_count()
        print(f"Your computer has {self.num_cpus} cpus")
        emptyDict = dict()
        for i in range(self.num_cpus):
            for member in self.all_members:
                emptyDict[member] = 0
            self.list_repeats_dict.append(emptyDict) #a dictionary to calc repeats, in each cpu separately
        

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
        out_str = (f"\nnumber combos before checks is ")
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.combos))
        checkCombos()
        out_str = (f"\nnumber combos before checks is ")
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.combos))
    

    def createSets(self) -> None:
        ########################################################################################################################
        #### start #### inner #### functions
        ########################################################################################################################
        def checkSets(startindex, endindex, cpu_num) -> list:#note ends are start + length of array, range excludes stop val, so no need to alter by doing end_index - 1, just LEAVE IT
            all_members_arr = (self.group1 + self.group2 + self.group3)
            result = list(list())
            tmp = list(list())
            emptyDict = dict()
            for member in self.all_members:
                emptyDict[member] = 0
            # first check for repeats, will eliminate a lot of the sets
            for team_combo in self.set_of_combos[startindex:endindex]:
                self.list_repeats_dict[cpu_num] = emptyDict.copy() # this will increment based on the person that we come across, if any index increases past 1 then its a repeat
                add_this_combo = True
                for team in team_combo:
                    for member in team:
                        self.list_repeats_dict[cpu_num][member] += 1
                        if (self.list_repeats_dict[cpu_num][member] == 2):
                            add_this_combo = False
                            break
                    if(add_this_combo == False):
                        break
                if(add_this_combo == True):
                    tmp.append(team_combo)
            # self.set_of_combos = tmp.copy()
            result = tmp.copy()
            tmp.clear()
            # next check for more than one group 3 member if its not an empty list
            if(self.grp3_empty_flag == False or len(self.group3 == 1) == True): #then do grp3 checks, again only one member should be chosen, thus two should NOT be on same team
                for team_combo in self.set_of_combos[startindex:endindex]:
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
                # self.set_of_combos = tmp.copy()
                result = tmp.copy()
                tmp.clear()
            return result
        def collectResults(result):
            self.all_results.append(result)
        def split_list(input_list, num_parts):
            avg_part_size = len(input_list) // num_parts
            remainder = len(input_list) % num_parts

            split_lists = [input_list[i * avg_part_size:(i + 1) * avg_part_size] for i in range(num_parts)]
            
            # Distribute the remainder items among the split_lists
            for i in range(remainder):
                split_lists[i].append(input_list[num_parts * avg_part_size + i])

            return split_lists
        ########################################################################################################################
        #### end #### inner #### functions
        ########################################################################################################################    
        for team_combo in combinations(self.combos,self.number_of_teams):
            self.set_of_combos.append(team_combo)
        out_str = (f"\nnumber sets before checks is ")
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.set_of_combos))

        #split big list into (num cpus) equal parts
        self.set_of_combos_split = split_list(self.set_of_combos,self.num_cpus)

        #next git the starts and ends
        parallel_start_vals = list()
        parallel_end_vals = list()
        sum_index = 0
        i = 0
        for inner_list in self.set_of_combos_split:
            parallel_start_vals.append(sum_index)
            sum_index += len(inner_list)
            parallel_end_vals.append(sum_index)
            print(f"list #{i} has {len(inner_list)} items in it")
            i+=1

        if (len(parallel_start_vals) != len(parallel_end_vals)):
            print("ERROR parallel arrays dont align!!!!!!!")
        for i in range(len(parallel_start_vals)):
            print(f"start : {parallel_start_vals[i]}, end : {parallel_end_vals[i]}")

        cpu_num = 0
        for start,end in zip(parallel_start_vals,parallel_end_vals):#zip lets you iterate through two lists same time
            self.pool.apply_async(func=checkSets, args=(start,end,cpu_num), callback=collectResults)
            cpu_num += 1
        self.pool.close()
        self.pool.join()
        self.set_of_combos_checked = self.all_results

        out_str = (f"\nnumber sets after checks is ")
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.set_of_combos_checked))






    
