import sys
from typing import List,Optional

from member.member import Member
from utility import fxns as utils
from frames.home_frame import HomeFrame



def main():
    names,avails,priorities,pri_map = utils.initialize_mems()
    # print(f"names: {names}\n\navails: {avails}\n\npriorities: {priorities}")
    # sys.exit()
    # ic(names,avails,priorities)
    avails = utils.trim_availabilities(avails)
    # ic(avails)
    members: List[Optional[Member]] = [None for _ in range(len(names))]
    prl_ptr = 0
    while prl_ptr < len(names):
        member = Member(name=names[prl_ptr],avail_matrix=avails[prl_ptr],priority=pri_map[names[prl_ptr]])
        members[prl_ptr] = member
        prl_ptr += 1
    members_dict = {member.member_id: member for member in members}
    # for mem in members:
    #     print(f"name -> {mem.name}\npriority -> {mem.priority}")
    # exit()
    # for member in members:
    #     member.print_member_attributes()
    group1, group2, group3 = utils.groups_from_mems(members)
    utils.json_from_mems(members)

    homefr = HomeFrame(members=members,group1=group1,group2=group2,group3=group3,mem_dict=members_dict)





if __name__ == "__main__":
    main()
