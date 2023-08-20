from AvailabilityFile import AvailabilityFile

import pandas as pd


def drawDictionary(dic):
    for k,v in dic.items():
        print(f"key: {k}, val: {v}\n")




"""Purpose of this object will be to make doing comparisons between people and their availabilities easier, the object will accomplish this
by creating a dictionary, where the key is the name of the person, and the value is going to be two arrays(Parallel) having start and end times
error checking: if start times not equal to end times"""
class EasyAvailability:
    keyName_valStartTimeEndTimeParallelArrs = dict()
    availFile_obj = AvailabilityFile

    def __init__(self,availFile_obj) -> None:
        self.availFile_obj = availFile_obj

    def generateDictionary(self):
        for innerArr in self.availFile_obj.name_avail_matrix:
            parallel_arr_start_end = list()
            tmp_start = list()
            tmp_end = list()
            #get rid of the NaT's so that we can do error checking, otherwise check will not work
            for val in innerArr[1::2]:
                if pd.isnull(val):
                    continue
                tmp_start.append(val)
            for val in innerArr[2::2]:
                if pd.isnull(val):
                    continue
                tmp_end.append(val)

            assert(len(tmp_start) == len(tmp_end)), "your start and end times arent lining up, make sure that you have the same # start and end times, thanks :)"#then diff num start and end times
            parallel_arr_start_end.append(tmp_start.copy())
            parallel_arr_start_end.append(tmp_end.copy())

            self.keyName_valStartTimeEndTimeParallelArrs[innerArr[0]] = parallel_arr_start_end
        drawDictionary(self.keyName_valStartTimeEndTimeParallelArrs)