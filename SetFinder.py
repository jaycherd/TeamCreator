from ComboHolder import ComboHolder
from EasyAvailability import EasyAvailability


class SetFinder:
    combo_obj = ComboHolder
    easy_avail_obj = EasyAvailability
    goodSets = list()
    keyTeamSetID_valMinutesOverlap = dict()

    def __init__(self, combo_obj,easy_avail_obj) -> None:
        self.combo_obj = combo_obj
        self.easy_avail_obj = easy_avail_obj

    def findGoodSets(self,min_hours,min_days) -> None:
        tmp = list()
        team_set_id = 0
        for teams in self.combo_obj.set_of_combos:
            valid_set = True #as long as this is true keep making checks, once its false break from the inner loops
            for team in teams: #check for times overlap in each team within each set of teamS - emphasis on the S here cus multiple teams :)
                sum_minutes_overlap = 0
                common_times = list()
                for i in range(len(team)-1):#team[i] will be current member
                    """new idea: create an available minutes dictionary from the dictionary i already have, and do this in the EasyAvailability.py that way
                    i dont have to keep generating this giant dictionary, instead i do it once then access the values in the dictionary here, and check for overlaps"""
                    # use python set intersection, compare current member avail mins to next member avail mins
                    curr_member = team[i]
                    next_member = team[i+1]
                    common_times = set(self.easy_avail_obj.keyName_valAvailableMinutes.get(curr_member)).intersection(self.easy_avail_obj.keyName_valAvailableMinutes.get(next_member))
                    common_times = list(common_times)
                    break
                break
            break
        print(f"common times: {common_times}")
        self.goodSets = tmp.copy()


    def drawGoodSets(self):
        pass
