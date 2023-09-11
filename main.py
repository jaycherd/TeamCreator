import sys

import config
from AvailabilityFile import AvailabilityFile
from FileWrite import writeValidSets
from GroupPriorityFile import GroupPriorityFile
from ComboHolder import ComboHolder
from SetFinder import SetFinder
from DataBase import DataBase
from EasyAvailability import EasyAvailability
from ErrorChecker import ErrorChecker
from Performance import Performance
import CommandLineArgs as cla
import Utility

SETS_FNAME = "sets.csv"
LASTRUN_NAMES_FNAME = "lastrun_groups.csv"



def main():
    prf_flag = False
    calcsets_flag = False
    if len(sys.argv) > 1:
        results = cla.argCheck(sys.argv[1:])
        prf_flag = results[0]
        calcsets_flag = results[1]
    

    prf_obj = Performance() ##keep this at the beginning
    prf_obj.start()

    e_check = ErrorChecker()

    # get availability file info
    avail_obj = AvailabilityFile(config.csv_availability_filename)
    e_check.checkAvail(avail_obj)
    # get priority file info
    pri_obj = GroupPriorityFile(config.csv_priority_filename)
    e_check.checkGroupPri(pri_obj)
    #if user made changes to group csv we should recalculate sets!
    calcsets_flag2 = Utility.groupsCSVsChanged(config.csv_priority_filename,LASTRUN_NAMES_FNAME)

    if calcsets_flag or calcsets_flag2:
        prf_obj.startCombo()
        # next generate a list of every possible combination and set of combos in the combo object
        combo_obj = ComboHolder(config.team_size,config.number_of_teams,\
            pri_obj.group1,pri_obj.group2,pri_obj.group3,True)
        combo_obj.createCombos()
        combo_obj.createSets()
        prf_obj.endCombo()
        writeValidSets(SETS_FNAME,combo_obj)
    else:
        prf_obj.startCombo()
        # next generate a list of every possible combination and set of combos in the combo object
        combo_obj = ComboHolder(config.team_size,config.number_of_teams,\
            pri_obj.group1,pri_obj.group2,pri_obj.group3,True)
        combo_obj.createSetsFromFile(SETS_FNAME)
        prf_obj.endCombo()


    prf_obj.startEA()
    easyavail_obj = EasyAvailability(avail_obj)
    prf_obj.endEA()
    prf_obj.startEAGD()
    easyavail_obj.generateDictionary()
    prf_obj.endEAGD()

    prf_obj.startSetFinder()
    setfinder_obj = SetFinder(combo_obj,easyavail_obj)
    prf_obj.startSFCMOD()
    setfinder_obj.createMinuteOverlapDic(config.minHoursOverlap)
    prf_obj.endSFCMOD()
    prf_obj.startSFCSD()
    setfinder_obj.createSortedDic()
    prf_obj.endSFCSD()
    prf_obj.startSFCCD()
    setfinder_obj.createCompressedDic()
    prf_obj.endSFCCD()
    prf_obj.startSFDGS()
    setfinder_obj.drawGoodSets()
    prf_obj.endSFDGS()
    prf_obj.endSetFinder()

    db_obj = DataBase()
    db_obj.generateValidSetDatabase(sets=combo_obj,sfinder=setfinder_obj,easy=easyavail_obj)

    Utility.createLastRunGroupsCSV(config.csv_priority_filename,LASTRUN_NAMES_FNAME)

    #keep this at the end - for performance measuring purposes
    prf_obj.end()
    if prf_flag:
        prf_obj.drawPerformance()



if __name__ == "__main__":
    main()
    