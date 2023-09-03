from itertools import combinations
import multiprocessing as mp
import copy

lock = mp.Lock()

results_glob = []

def checkSets(set_of_combos_to_check, cpu_num, all_members_arr, grp3_empty_flag, grp1_empty_flag, group1, group3, list_repeats_dict) -> list:#note ends are start + length of array, range excludes stop val, so no need to alter by doing end_index - 1, just LEAVE IT
    cpu_num = mp.current_process()._identity[0]-1
    print(f"cpu {cpu_num} successfully entered checksets fxn")
    res = []
    tmp = []
    emptyDict = {member : 0 for member in all_members_arr}
    for member in all_members_arr:
        emptyDict[member] = 0
    # first check for repeats, will eliminate a lot of the sets
    for team_combo in set_of_combos_to_check:
        list_repeats_dict[cpu_num] = emptyDict.copy() # this will increment based on the person that we come across, if any index increases past 1 then its a repeat
        add_this_combo = True
        for team in team_combo:
            for member in team:
                list_repeats_dict[cpu_num][member] += 1
                if (list_repeats_dict[cpu_num][member] == 2):
                    add_this_combo = False
                    break
            if(add_this_combo == False):
                break
        if(add_this_combo == True):
            tmp.append(team_combo)
    # self.set_of_combos = tmp.copy()
    res = tmp[:]
    tmp.clear()
    # next check for more than one group 3 member if its not an empty list
    if((grp3_empty_flag == False) and (len(group3) != 1)): #then do grp3 checks, again only one member should be chosen, thus two should NOT be on same team
        for team_combo in res:
            group3_count_in_set = 0
            add_this_combo = True
            for team in team_combo:
                for member in team:
                    if(member in group3):
                        group3_count_in_set += 1
                    if(group3_count_in_set == 2):
                        add_this_combo = False
                        break
                if(add_this_combo == False):
                    break
            if(add_this_combo):
                tmp.append(team_combo)
        # self.set_of_combos = tmp.copy()
        result = tmp[:]
        tmp.clear()
    else:
        result = res
    # print(f"from checks:cpu {cpu_num} eliminated {repeat_elim_count} because of repeats, and eliminated {group3_elim_count} bcs group3")
    return result
def custom_error_callback(error):
    print(error,flush=True)
def collectResults(result):
    # print(f"result is adding : {len(result)} items")
    global results_glob
    results_glob.append(result)



class ComboHolder:
    results = list(list())
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
        num_cpus = mp.cpu_count()
        self.set_of_combos_split = split_list(self.set_of_combos,num_cpus)
        
        emptyDict = dict()
        list_repeats_dict = list()
        for i in range(num_cpus):
            for member in self.all_members:
                emptyDict[member] = 0
            list_repeats_dict.append(emptyDict) #a dictionary to calc repeats, in each cpu separately

        pool = mp.Pool(mp.cpu_count())
        
        print(f"----------------------------------------------------------------")
        print(f"Parallel Process info: \nYour computer has {num_cpus} cpus\npool : {pool}")
        print(f"----------------------------------------------------------------")
        cpu_num = 0
        for combos_to_check in self.set_of_combos_split:
            results = pool.apply_async(
                checkSets, 
                args=(combos_to_check,cpu_num,self.all_members.copy(),self.grp3_empty_flag,self.grp1_empty_flag,self.group1.copy(),self.group3.copy(),list_repeats_dict.copy()),
                callback=collectResults, 
                error_callback=custom_error_callback
                )
            cpu_num += 1
        pool.close()
        pool.join()            
        tmp = results_glob
        i = 0
        for inner in tmp:#get inner list as thats how they were appended
            # print(f"process which finished in place {i} had : {len(inner)} items")
            i += 1
            for item in inner:#doing this to flatten list into a single list of sets, rather than cpu_num lists of a list of sets
                self.set_of_combos_checked.append(item)

        out_str = (f"number sets after checks is ")
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.set_of_combos_checked))
