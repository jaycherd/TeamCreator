from Compare import Compare
from ErrorChecker import ErrorChecker
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
from CompareOverlap import CompareOverlap as CO
import config



def main():
    e_check = ErrorChecker()

    # get availability file info
    avail_obj = AvailabilityFile(config.CSV_AVAILABILITY_FNAME)
    e_check.checkAvail(avail_obj)

    # get priority file info
    pri_obj = GroupPriorityFile(config.CSV_GRP_PRIORITY_FNAME)
    e_check.checkGroupPri(pri_obj)

    cmp_obj = Compare(avail_obj,pri_obj)
    cmp_obj.what2Cmp()
    cmp_obj.generateDict()

    ovrlap_obj = CO(cmp_obj.keyName_valAvailableMinutes)
    ovrlap_obj.findOverlap()
    ovrlap_obj.drawOverlap()




