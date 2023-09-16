import time
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
from ErrorChecker import ErrorChecker
from EasyAvailability import EasyAvailability as EA
from gui import MyFrame


class Compare:
    """class for comparing team mems"""
    avail_obj = AvailabilityFile
    pri_obj = GroupPriorityFile
    Easy_obj = EA
    list_of_names = list()
    ppl_to_cmp = list()
    keyName_valAvailableMinutes = dict()


    def __init__(self,A_obj,P_obj):
        self.avail_obj = A_obj
        self.pri_obj = P_obj
        self.list_of_names = P_obj.group1 + P_obj.group2 + P_obj.group3
    
    def what2Cmp(self):
        frame = MyFrame()
        frame.drawCmpGUI(self.list_of_names)
        self.ppl_to_cmp = frame.cmp_clk_result
        E_obj = ErrorChecker()
        print(f"okie I'm comparing these peeps :\n {self.ppl_to_cmp} \U0001F914")
    
    def generateDict(self):
        self.Easy_obj = EA(self.avail_obj)
        self.Easy_obj.generateDictionary()
        for name,available_mins in self.Easy_obj.keyName_valAvailableMinutes.items():
            if name not in self.ppl_to_cmp:
                continue
            self.keyName_valAvailableMinutes[name] = available_mins.copy()
