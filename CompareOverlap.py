class CompareOverlap:
    keyName_valAvailableMinutes = dict()
    ppl_to_cmp = list()
    overlap = list()

    def __init__(self,dc) -> None:
        self.keyName_valAvailableMinutes = dc
        self.ppl_to_cmp = list(dc.keys())
    
    def findOverlap(self) -> None:
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

    def drawOverlap(self) -> None:
        if len(self.overlap) == 0:
            print(f"this team has no common time!")
            return
        







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