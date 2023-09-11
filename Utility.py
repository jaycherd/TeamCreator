import shutil
import csv
import json
import pickle


# from AvailabilityFile import AvailabilityFile


def createLastRunGroupsCSV(fname_copy,fname_write):
    shutil.copy(fname_copy,fname_write)

def groupsCSVsChanged(curr_groups_fname,lastrun_groups_fname)->bool:
    #first check if group pri file has even been generated, if not, return True
    with open(curr_groups_fname,'r',encoding='utf-8') as read_file:
        lst1 = list(csv.reader(read_file,delimiter=','))
    with open(lastrun_groups_fname,'r',encoding='utf-8') as read_file:
        lst2 = list(csv.reader(read_file,delimiter=','))
    if lst1 == lst2:
        return False
    return True

def writeToJSON(fname,obj):
    with open(fname,"w+",encoding="utf-8") as my_json:
        json.dump(obj,my_json)

def writeToPickle(fname,obj):
    with open(fname,"wb") as my_pickle_lol:
        pickle.dump(obj,my_pickle_lol)

def getObjFromPickle(fname):#returns obj
    with open(fname,"rb") as mepickle_r_file:
        return pickle.load(mepickle_r_file)
