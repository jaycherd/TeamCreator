class CompareOverlap:
    keyName_valAvailableMinutes = dict()
    ppl_to_cmp = list()
    overlap = list()
    sorted_overlap = list()
    cmprsd_overlap = list()

    def __init__(self,dc) -> None:
        self.keyName_valAvailableMinutes = dc
        self.ppl_to_cmp = list(dc.keys())
    
    def findOverlap(self) -> None:
        #####################################################inner fxns#########################################################
        ########################################################################################################################
        def sortOverlap(arr):
            def key_to_sort_by(str):
                return(int(str[0:1]))
            def key_to_sort_by_tiebreak(str):
                return(int(str[2:4]))
            def key_to_sort_by_tiebreak2(str):
                return(int(str[5:]))
            res = list(arr)
            res.sort(key=lambda x : (key_to_sort_by(x),key_to_sort_by_tiebreak(x),key_to_sort_by_tiebreak2(x)))
            return res.copy()
        def compressDictionary(arr):
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
        ########################################################################################################################
        ########################################################################################################################
        common_times = list()
        for i in range(len(self.ppl_to_cmp) - 1):
            curr_mem = self.ppl_to_cmp[i]
            next_mem = self.ppl_to_cmp[i+1]
            if (i == 0): #continuously intersect sets to remove uncommon times in O(n)
                common_times = set(self.keyName_valAvailableMinutes.get(curr_mem)).intersection(self.keyName_valAvailableMinutes.get(next_mem))
            else:
                common_times = set(common_times).intersection(self.keyName_valAvailableMinutes.get(next_mem))
        tmp = list(common_times)
        self.overlap = tmp.copy()
        self.sorted_overlap = sortOverlap(self.overlap.copy())
        self.cmprsd_overlap = compressDictionary(self.sorted_overlap.copy())


    def drawOverlap(self) -> None:
        #####################################################inner fxns#########################################################
        ########################################################################################################################
        def convertNum2Day(str) -> str:
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
        ########################################################################################################################
        ########################################################################################################################
        if len(self.overlap) == 0:
            print(f"this team has no common time!")
            return

        for i in range(len(self.cmprsd_overlap[0])):
            print(f"{convertNum2Day(self.cmprsd_overlap[0][i])} to {(self.cmprsd_overlap[1][i])[2:]}")

                 
        







#         for i in range(len(team)-1):#team[i] will be current member
#             """new idea: create an available minutes dictionary from the dictionary i already have, and do this in the EasyAvailability.py that way
#             i dont have to keep generating this giant dictionary, instead i do it once then access the values in the dictionary here, and check for overlaps"""
#             # use python set intersection, compare current member avail mins to next member avail mins
#             curr_member = team[i]
#             next_member = team[i+1]
#             if(i == 0):#first iteration
#                 common_times = set(self.easy_avail_obj.keyName_valAvailableMinutes.get(curr_member)).intersection(self.easy_avail_obj.keyName_valAvailableMinutes.get(next_member))
#             else:
#                 common_times = set(common_times).intersection(self.easy_avail_obj.keyName_valAvailableMinutes.get(next_member))
#         if(len(common_times) < min_hours*60):
#             valid_set = False
#             break #will stop tmp_common_times arr from appending the common times too
#         tmp_common_times_arr.append(common_times.copy())
#     team_set_id += 1
#     if valid_set:
#         self.keyTeamSetID_valMinutesOverlap[team_set_id] = tmp_common_times_arr.copy()
#     else:
#         continue
# out_str = (f"\n# sets w/min {min_hours} hour(s) overlap ")
# print(out_str.ljust(34,'-'),end="> ")
# print(len(self.keyTeamSetID_valMinutesOverlap.values()))