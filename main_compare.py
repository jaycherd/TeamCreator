from Compare import Compare
from ErrorChecker import ErrorChecker
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
import config



def main():
    e_check = ErrorChecker()
    # get availability file info
    avail_obj = AvailabilityFile(config.csv_availability_filename)
    e_check.checkAvail(avail_obj)
    # get priority file info
    pri_obj = GroupPriorityFile(config.csv_priority_filename)
    e_check.checkGroupPri(pri_obj)
    cmp_obj = Compare(avail_obj,pri_obj)
    cmp_obj.what2Cmp()