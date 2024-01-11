from typing import List,Tuple,Optional,Dict
from member.member import Member

from icecream import ic


def generate_grp_string(group: List[str],mems_dict: Dict[int,Member]) -> str:
    res = ""
    for i in range(len(group)):
        if i != 0:
            res += ", "
        mem = mems_dict.get(int(group[i])) #get name by looking up mem id
        res += mem.name
    return res

#second int in tuple, is the error code
def homeframe_inputs_isvalid(numteams: str, memsper: str, olap: str, memsdict: Dict[int,Member],numleaders: int) -> Tuple[bool,int,Optional[Tuple[int,int,float]]]:
    try:
        numteams_int = int(numteams)
        if numteams_int < 1:
            return False,0,None
    except ValueError:
        return False,0,None
    try:
        memsper_int = int(memsper)
        if memsper_int < 1:
            return False,1,None
    except ValueError:
        return False,1,None
    try:
        olap_flt = float(olap)
        if olap_flt < 0:
            return False,2,None
        if not (olap_flt*4).is_integer():
            return False,2,None
    except ValueError:
        return False,2,None
    
    num_mems = len(memsdict)
    if numteams_int * memsper_int > num_mems:
        return False,3,None
    if numteams_int > numleaders:
        return False,4,None

    return (True,-1,(numteams_int,memsper_int,olap_flt))

def get_names_from_memids_tup(mem_ids: Tuple[Tuple[str]], mems_dict: Dict[int,Member]) -> List[str]:
    teams_strs = []
    for team in mem_ids:
        team_str = ""
        for i,mem_id in enumerate(team):
            if i != 0:
                team_str += ', '
            mem = mems_dict.get(int(mem_id))
            team_str += mem.name
        teams_strs.append(team_str)
    return teams_strs

def get_day(daynum: str) -> str:
    switcher = {
        '0': "Mon",
        '1': "Tues",
        '2': "Wed",
        '3': "Thur",
        '4': "Fri",
        '5': "Sat",
        '6': "Sun"
    }
    return switcher.get(daynum, "Invalid day number")

def draw_start_end(start_end_prl: Tuple[Tuple[str]]) -> str:
    res = ""
    for i in range(len(start_end_prl[0])):
        if i != 0:
            res += '\n'
        day = get_day(daynum=start_end_prl[0][i].split('-')[1])
        res += f"{day} from {start_end_prl[0][i].split('-')[0]} to {start_end_prl[1][i].split('-')[0]}"
    return res

    