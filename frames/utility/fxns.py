from typing import List,Tuple,Optional,Dict
from member.member import Member


def generate_grp_string(group: List[str],mems_dict: Dict[int,Member]) -> str:
    res = ""
    for i in range(len(group)):
        if i != 0:
            res += ", "
        mem = mems_dict.get(int(group[i])) #get name by looking up mem id
        res += mem.name
    return res

#second int in tuple, is the error code
def homeframe_inputs_isvalid(numteams: str, memsper: str, olap: str) -> Tuple[bool,int,Optional[Tuple[int,int,float]]]:
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
    return True,-1,(numteams_int,memsper_int,olap_flt)

    