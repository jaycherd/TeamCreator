from ComboHolder import ComboHolder
from AvailabilityFile import AvailabilityFile


class SetFinder:
    combo_obj = ComboHolder
    avail_obj = AvailabilityFile
    goodSets = list()

    def __init__(self, combo_obj,avail_obj) -> None:
        self.combo_obj = combo_obj
        self.avail_obj = avail_obj

    def findGoodSets(self,min_hours,min_days) -> None:
        tmp = list()
        for teams in self.combo_obj.set_of_combos:
            for team in teams: #check for times overlap in each team within each set of teamS - emphasis on the S here cus multiple teams :)
                pass

        self.goodSets = tmp.copy()

    def drawGoodSets(self):
        pass
