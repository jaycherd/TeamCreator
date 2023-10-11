import csv
import json
from typing import List,Tuple

from icecream import ic
from utility import constants as csts
from member.member import Member

def get_names_prl(avail_data: List[List[str]]) -> List[str]:
    names = []
    for inner_lst in avail_data:
        names.append(inner_lst[0])
    return names

def get_pri_prl(pri_data: List[List[str]],names: List[str]) -> List[str]:
    priorities = []
    for i,inner_list in enumerate(pri_data):
        for name in inner_list:
            if name in names:
                priorities.append(i+1)
    return priorities

def get_avails_prl(avail_data: List[List[int]],names: List[str]) -> List[List[str]]:
    """
    rtype: List of Lists of Avails, indexed by day
    """
    res_avails = [[]*i for i in range(len(names))]
    header = avail_data[0]
    availabilities = avail_data[1:]
    invalid_set = {'N/A','','Nan',None,'NA','na','Na','None','none','unnavailable'}
    #idea: iterate through avail inner lists with a pointer at both header and curr list
    for i,inner_list in enumerate(availabilities):
        prl_ptr = 1#start at one to skip the names
        this_mems_matrix = [] #unsure of size here, probably 7 days to rep week, but user could enter avails for only five days or something like that
        curr_day_lst = []
        for j in range(len(inner_list)-1):#-1 because we discarding first item (name), thus this makes us end at end even tho range() is exclusive
            if j != 0 and header[prl_ptr] not in invalid_set:
                this_mems_matrix.append(curr_day_lst.copy())
                curr_day_lst.clear()
            curr_day_lst.append(inner_list[prl_ptr])
            prl_ptr += 1
        this_mems_matrix.append(curr_day_lst.copy())
        curr_day_lst.clear()
        res_avails[i] = this_mems_matrix

            

    return res_avails



def initialize_mems(avail_fname=csts.csv_avail_fname,priority_fname=csts.csv_pri_fname) -> Tuple[List[str],List[List[List[str]]],List[str]]:
    """
    create three lists - parallel
    1. name
    2. avail string
    3. priority
    returns as Tuple in order specified above
    NOTE: avail contains header, pri does not
    """
    with open(avail_fname,'r',encoding='UTF-8') as file:
        reader = csv.reader(file)
        avail_data = list(reader) # creates List[List[availabilities: str]] - List[List[0]] = name, List[0] = header
    names = get_names_prl(avail_data=avail_data[1:])
    with open(priority_fname,'r',encoding='UTF-8') as file:
        reader = csv.reader(file)
        pri_data = list(reader)
    priorities = get_pri_prl(pri_data=pri_data,names=names)
    avails = get_avails_prl(avail_data=avail_data,names=names)
    return ((names,avails,priorities))


def trim_availabilities(avails: List[List[List[str]]]) -> List[List[List[str]]]:
    invalid_set = {'N/A','na','n/a','None','none','unnavailable','Nan','NA'}
    for lstoflstofstr in avails:
        for lstofstr in lstoflstofstr:
            i = 0
            while i < len(lstofstr):
                lstofstr[i] = lstofstr[i].strip()
                if lstofstr[i] == '' or lstofstr[i] in invalid_set:
                    lstofstr.pop(i)
                else:
                    i += 1
    return avails

def groups_from_mems(mems: List[Member]) -> Tuple[List[str],List[str],List[str]]:
    group1,group2,group3 = [],[],[]
    for mem in mems:
        if mem.priority == 1:
            group1.append(str(mem.member_id)) #quick fix, to make things easier later, sort groups by mem_id and use mem_id in general instead of name
        elif mem.priority == 2:
            group2.append(str(mem.member_id))
        else:
            group3.append(str(mem.member_id))
    return (group1,group2,group3)

def json_from_mems(mems: List[Member],fname=csts.json_mem_fname) -> None:
    res = {}
    for i,mem in enumerate(mems):
        tmplst = []
        tmplst = [mem.name,mem.priority,mem.avail_matrix]
        res[mem.member_id] = tmplst
    with open(fname,'w',encoding='UTF-8') as file:
        json.dump(res,file,indent=4)

    