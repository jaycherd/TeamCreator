from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
from ErrorChecker import ErrorChecker
from EasyAvailability import EasyAvailability as EA
import config


class Compare:
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
        for i in range(len(self.list_of_names)):
            out_str = (f"{i} : {self.list_of_names[i]}")
            print(out_str.ljust(20,' '),end="\t")
            if((i+1) % 4 == 0):
                print()
        people_to_compare_str = input(f"\ninput who you want to compare, as numbers (comma separated)\U0001f600\n")
        self.ppl_to_cmp = (people_to_compare_str.split(','))
        E_obj = ErrorChecker()
        E_obj.checkCompare(self.ppl_to_cmp,self.list_of_names)
        tmp = list()
        for val in self.ppl_to_cmp:
            tmp.append(int(val))
        tmp.sort()
        self.ppl_to_cmp = tmp.copy()
        tmp.clear()
        for val in self.ppl_to_cmp:
            tmp.append(self.list_of_names[val])
        self.ppl_to_cmp = tmp.copy()
        print(self.ppl_to_cmp)
    
    def generateDict(self):
        self.Easy_obj = EA(self.avail_obj)
        self.Easy_obj.generateDictionary()
        for name,available_mins in self.Easy_obj.keyName_valAvailableMinutes.items():
            if name not in self.ppl_to_cmp:
                continue
            self.keyName_valAvailableMinutes[name] = available_mins.copy()
    



