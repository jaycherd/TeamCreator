import config
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
from ComboHolderParallel import ComboHolder
from SetFinderParallel import SetFinder
from EasyAvailability import EasyAvailability
from ErrorChecker import ErrorChecker
from Performance import Performance

def main(prf_flag = False):
    prf_obj = Performance()##keep at the start
    prf_obj.start()

    e_check = ErrorChecker()

    # get availability file info
    avail_obj = AvailabilityFile(config.csv_availability_filename)
    e_check.checkAvail(avail_obj)
    # get priority file info
    pri_obj = GroupPriorityFile(config.csv_priority_filename)
    e_check.checkGroupPri(pri_obj)


    # next generate a list of every possible combination and set of combos in the combo object
    # note in this version ComboHolder (same name) is calling different combo holder, parallel version
    prf_obj.startCombo()
    combo_obj_prl = ComboHolder(config.team_size,config.number_of_teams,pri_obj.group1,pri_obj.group2,pri_obj.group3)
    combo_obj_prl.createCombos()
    combo_obj_prl.createSets()
    prf_obj.endCombo()

    easyAvail_obj = EasyAvailability(avail_obj)
    easyAvail_obj.generateDictionary()


    prf_obj.startSetFinder()
    setFinder_obj = SetFinder(combo_obj_prl,easyAvail_obj)
    setFinder_obj.createMinuteOverlapDic(config.minHoursOverlap)
    setFinder_obj.createSortedDic()
    setFinder_obj.createCompressedDic()
    setFinder_obj.drawGoodSets()
    prf_obj.endSetFinder()






    ##keep at end
    prf_obj.end()

    if(prf_flag):
        prf_obj.drawPerformance()