from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
import config


class Compare:
    avail_obj = AvailabilityFile
    pri_obj = GroupPriorityFile
    list_of_names = list()


    def __init__(self,A_obj,P_obj):
        self.avail_obj = A_obj
        self.pri_obj = P_obj
        self.list_of_names = P_obj.group1 + P_obj.group2 + P_obj.group3
    
    def what2Cmp(self):
        for i in range(len(self.list_of_names)):
            print(f"{i}")