import sqlite3 as sql3
from SetFinder import SetFinder
from ComboHolder import ComboHolder
from EasyAvailability import EasyAvailability

def createMinuteOverlapDic(min_overlap,sets,easy_avail_obj) -> dict:
        keyteamsetid_val5minutesoverlap = {}
        team_set_id = -1
        for teams in sets:
            valid_set = True #as long as this is true keep making checks, once its false
            # recursively break from the inner loops
            tmp_common_times_arr = []
            for team in teams: #check for times overlap in each team within each set of
                # teamS - emphasis on the S here cus multiple teams :)
                # sum_minutes_overlap = 0
                common_times = set()
                for i in range(len(team)-1):#team[i] will be current member
                    # """new idea: create an available minutes dictionary from the dictionary i
                    #  already have, and do this in the EasyAvailability.py that way
                    # i dont have to keep generating this giant dictionary, instead i do it once
                    #  then access the values in the dictionary here, and check for overlaps"""
                    # use python set intersection, compare current member avail mins to next
                    # member avail mins
                    curr_member = team[i]
                    next_member = team[i+1]
                    if i == 0:#first iteration
                        common_times = easy_avail_obj.keyName_valAvailableMinutes.\
                            get(curr_member).intersection(easy_avail_obj.\
                            keyName_valAvailableMinutes.get(next_member))
                    else:
                        common_times = common_times.intersection\
                            (easy_avail_obj.keyName_valAvailableMinutes.get(next_member))
                if len(common_times) < min_overlap:
                    valid_set = False
                    break #will stop tmp_common_times arr from appending the common times too
                tmp_common_times_arr.append(common_times.copy())
            team_set_id += 1
            if valid_set:
                keyteamsetid_val5minutesoverlap[team_set_id] = tmp_common_times_arr.copy()
            else:
                continue
        out_str = f"\n# sets w/min {min_overlap*5} minutes overlap is:"
        print(out_str.ljust(34,'-'),end="> ")
        print(len(keyteamsetid_val5minutesoverlap.values()))
        return keyteamsetid_val5minutesoverlap







class DataBase:
    """making database for storing program info"""
    def __init__(self):
        self.conxn = sql3.connect("mydatabase.db")
        self.crsr = self.conxn.cursor()
    
    def generateValidSetDatabase(self,sets: ComboHolder, sfinder: SetFinder,easy: EasyAvailability):
        # print(sets.keyTeamSetID_val5minutesoverlap_sorted)
        # How to org table primary key = team set id, the team(s) which makes up the set (varies, based on how many teams they say to use)
        # get the len of overlap, problem here is that rightnow the dictionary contains times where a team mem may share a start/end but no other time in the hour
        # so need to fix this before anything... whoops seems that the combo obj has all the sets, then the SetFinder figures out if it valid
        # print(sets.set_of_combos)
        ## first i think i need to make a dictionary for different overlaps, depending on how much time overlap
        ## starting with 5 minutes overlap, then 10,15,20,25,30, etc.
        #NOTE: rn getting it to work, could be optimized by only checking the sets which were calculated to be valid by the previous iteration

        create_table_query = """CREATE TABLE IF NOT EXISTS validsets(
        id integer PRIMARY KEY,

        )"""



        i = 1
        while True:
            curr_dic = createMinuteOverlapDic(min_overlap=i,sets=sets.set_of_combos,easy_avail_obj=easy)
            if len(curr_dic) == 0:
                break
            for set_id,minutes_overlap_arrs in curr_dic.items():
                pass




            i += 1
