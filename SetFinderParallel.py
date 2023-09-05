from ComboHolderParallel import ComboHolder
from EasyAvailability import EasyAvailability

import pandas as pd
import datetime as dt


class SetFinder:
    combo_obj = ComboHolder
    easy_avail_obj = EasyAvailability
    goodSets = list()
    keyTeamSetID_valMinutesOverlap = dict()
    keyTeamSetID_valMinutesOverlap_sorted = dict()
    keyTeamSetID_valMinutesOverlap_comp = dict()

    def __init__(self, combo_obj,easy_avail_obj) -> None:
        self.combo_obj = combo_obj
        self.easy_avail_obj = easy_avail_obj

    def createMinuteOverlapDic(self,min_hours) -> None:
        tmp = list()
        team_set_id = -1
        for teams in self.combo_obj.set_of_combos_checked:
            valid_set = True #as long as this is true keep making checks, once its false break from the inner loops
            tmp_common_times_arr = list(list())
            for team in teams: #check for times overlap in each team within each set of teamS - emphasis on the S here cus multiple teams :)
                sum_minutes_overlap = 0
                common_times = list()
                for i in range(len(team)-1):#team[i] will be current member
                    """new idea: create an available minutes dictionary from the dictionary i already have, and do this in the EasyAvailability.py that way
                    i dont have to keep generating this giant dictionary, instead i do it once then access the values in the dictionary here, and check for overlaps"""
                    # use python set intersection, compare current member avail mins to next member avail mins
                    curr_member = team[i]
                    next_member = team[i+1]
                    if(i == 0):#first iteration
                        common_times = set(self.easy_avail_obj.keyName_valAvailableMinutes.get(curr_member)).intersection(self.easy_avail_obj.keyName_valAvailableMinutes.get(next_member))
                    else:
                        common_times = set(common_times).intersection(self.easy_avail_obj.keyName_valAvailableMinutes.get(next_member))
                if(len(common_times) < min_hours*60):
                    valid_set = False
                    break #will stop tmp_common_times arr from appending the common times too
                tmp_common_times_arr.append(common_times.copy())
            team_set_id += 1
            if valid_set:
                self.keyTeamSetID_valMinutesOverlap[team_set_id] = tmp_common_times_arr.copy()
            else:
                continue
        out_str = (f"\n# sets w/min {min_hours} hour(s) overlap ")
        print(out_str.ljust(34,'-'),end="> ")
        print(len(self.keyTeamSetID_valMinutesOverlap.values()))

    """convert the common times to datetime, sort them, then get start and end times for the possible meet times"""
    def createSortedDic(self):
        def customSort(arr):
            def key_to_sort_by(str):
                return(int(str[0:1]))
            def key_to_sort_by_tiebreak(str):
                return(int(str[2:4]))
            def key_to_sort_by_tiebreak2(str):
                return(int(str[5:]))
            res = list(arr)
            res.sort(key=lambda x : (key_to_sort_by(x),key_to_sort_by_tiebreak(x),key_to_sort_by_tiebreak2(x)))
            return res.copy()

        
        for set_id,common_times_arr2d in self.keyTeamSetID_valMinutesOverlap.items():
            tmp_2d = list(list())
            for common_times in common_times_arr2d:
                tmp_sort = (customSort(common_times)).copy()
                tmp_2d.append(tmp_sort.copy())
            self.keyTeamSetID_valMinutesOverlap_sorted[set_id] = tmp_2d

        ## below for error checking the dictionaries
        # for k,v in self.keyTeamSetID_valMinutesOverlap_sorted.items():
        #     print(f"\n\nkey: {k}\t val : {v}")
        #     for inner_list in v:
        #         print(f"inner list: {inner_list}")
        # for k,v in self.keyTeamSetID_valMinutesOverlap.items():
        #     print(f"\n\nkey: {k}\t val : {v}")
        #     for inner_list in v:
        #         print(f"inner list: {inner_list}")


    """purpose: create yet another dictionary, in this case the dictionary will hold set of arrays running parallel
    the key will be the team set id number, and the value will be the pair of arrays, array at val[0][0] will be an array
    holding all the start times for the teams overlap, and val[0][1] will be an array of the corresponding end time, to find
    this i will use the logic that all times should be contiguous, that is, if there is a common time of 10:00 then there should also be
    10:01 for that time to be contiguous, which i can check using the sorted dic i made, and once you come across a time where the next minute does
    not exist, you know that the previous time was the end time, so first val = start, and last val is end, add those both to the arrays, and do this
    until you just have start and end times that each set id is having in common, note that each set is made up of multiple teams, so the vals will actually
    be an array of parallel arrays, so index 0 will be for teams[0] in teams, thus val[0][0] is the start times that the first team in the set of teams have 
    in common"""
    def createCompressedDic(self):
        def getStartsEnds(arr):
            starts = list()
            ends = list()
            starts.append(arr[0])
            for i in range(len(arr)-1):#time format %w %H:%M
                curr_str = arr[i]
                curr_day = int(curr_str[0:1])
                curr_hour = int(curr_str[2:4])
                curr_min = int(curr_str[5:]) + (curr_hour*60)
                next_str = arr[i+1]
                next_day = int(next_str[0:1])
                next_hour = int(next_str[2:4])
                next_min = int(next_str[5:]) + (next_hour*60)
                if(curr_day != next_day or next_min != curr_min + 1):
                    ends.append(curr_str)
                    starts.append(next_str)
            ends.append(arr[-1])
            res = list()
            res.append(starts)
            res.append(ends)
            return res
                

        for set_id,common_times_arr2d in self.keyTeamSetID_valMinutesOverlap_sorted.items():
            starts_ends_2d = list(list())
            for common_times in common_times_arr2d:
                starts_ends_2d.append(getStartsEnds(common_times).copy())
            self.keyTeamSetID_valMinutesOverlap_comp[set_id] = starts_ends_2d


        # for k,v in self.keyTeamSetID_valMinutesOverlap_comp.items():
        #     print(f"\n\nkey: {k}\t val : {v}")
        #     for inner_list in v:
        #         print(f"inner list: {inner_list}")


    def drawGoodSets(self):
        def convertNum2Day(str):
            day_of_week = str[0:1]
            if(day_of_week == '0'):
                return 'Mon - ' + str[2:]
            elif(day_of_week == '1'):
                return 'Tue - ' + str[2:]
            elif(day_of_week == '2'):
                return 'Wed - ' + str[2:]
            elif(day_of_week == '3'):
                return 'Thr - ' + str[2:]
            elif(day_of_week == '4'):
                return 'Fri - ' + str[2:]
            elif(day_of_week == '5'):
                return 'Sat - ' + str[2:]
            elif(day_of_week == '6'):
                return 'Sun - ' + str[2:]
            return str
        

        for set_id,common_times_arr2d in self.keyTeamSetID_valMinutesOverlap_comp.items():
            print(f"\nSet {set_id}: {self.combo_obj.set_of_combos[set_id]}")
            for i in range(len(common_times_arr2d)):
                print(f"Team {i+1}: {self.combo_obj.set_of_combos[set_id][i]}",end="->")
                for j in range(len(common_times_arr2d[i][0])):
                    print(f"{convertNum2Day(common_times_arr2d[i][0][j])} to {(common_times_arr2d[i][1][j])[2:]}",end=", ")
                print()

