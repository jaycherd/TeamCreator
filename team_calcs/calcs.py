from typing import List,Set
from icecream import ic
from itertools import combinations


from member.member import Member



def check_grp3(teams: Set[List[str]], grp3: List[str]) -> List[List[str]]:
    grp3_set = {mem for mem in grp3}
    ic(grp3_set)
    res = set()

    for team in teams:
        if len(set(team).intersection(grp3_set)) > 1:
            continue
        res.add(team)
    return res


def generate_teams(mems: List[str],grp1: List[str],grp2: List[str],grp3: List[str],team_size: int) -> List[List[str]]:
    ic()
    teams = set()  
    teams_nonset = []
    leader_combinations = list(combinations(grp1, 1))
    ic(leader_combinations)
    ic(type(leader_combinations))
    slots_taken = 1

    for other_mems in combinations(grp2+grp3,team_size-slots_taken):
        for leader_comb in leader_combinations:
            team=list(leader_comb) + list(other_mems)
            teams.add(tuple(team)) #check too many grp3 mems
    
    teams = check_grp3(teams,grp3)
    

    # for team in combinations(grp1+grp2+grp3,team_size):
    #     teams.add(team)
    #     teams_nonset.append(team)
    ic(len(teams))
    ic(teams)
    ic(len(teams_nonset))
    ic(teams_nonset)

    
    # for leader_comb in leader_combinations:
    #     temp_teams = [list(leader_comb)]
        
    #     remaining_slots = 2 * len(leader_comb)
    #     regular_combinations = combinations(grp2, remaining_slots)
        
    #     for reg_comb in regular_combinations:
    #         temp_teams_with_regulars = temp_teams.copy()
    #         temp_teams_with_regulars.extend([list(reg_comb[i:i+2]) for i in range(0, len(reg_comb), 2)])
            
    #         low_priority_members_used = []
    #         if len(grp3) > 0:
    #             for i, team in enumerate(temp_teams_with_regulars):
    #                 if len(team) < 3:
    #                     for low_member in grp3:
    #                         if low_member not in low_priority_members_used:
    #                             team.append(low_member)
    #                             low_priority_members_used.append(low_member)
    #                             break
                        
    #         if all(len(team) == 3 for team in temp_teams_with_regulars):
    #             sorted_teams = tuple(tuple(sorted(team)) for team in temp_teams_with_regulars)
    #             teams.add(sorted_teams)
    return [list(team) for team in teams]


        

