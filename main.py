from typing import List,Optional

from icecream import ic
from member.member import Member
from utility import fxns as utils
from frames.home_frame import HomeFrame



def main():
    names,avails,priorities = utils.initialize_mems()
    # ic(names,avails,priorities)
    avails = utils.trim_availabilities(avails)
    # ic(avails)
    members: List[Optional[Member]] = [None for _ in range(len(names))]
    prl_ptr = 0
    while prl_ptr < len(names):
        member = Member(name=names[prl_ptr],avail_matrix=avails[prl_ptr],priority=priorities[prl_ptr])
        members[prl_ptr] = member
        prl_ptr += 1
    
    for member in members:
        member.print_member_attributes()
    group1, group2, group3 = utils.groups_from_mems(members)
    utils.json_from_mems(members)

    homefr = HomeFrame(members=members,group1=group1,group2=group2,group3=group3)
    



    ic()








if __name__ == "__main__":
    main()
