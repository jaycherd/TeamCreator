import json
from typing import List,Set,Tuple
from icecream import ic
from itertools import combinations
from collections import Counter


from member.member import Member
from utility import constants as csts



def check_grp3(teams: Set[List[str]], grp3: List[str]) -> List[List[str]]:
    grp3_set = {mem for mem in grp3}
    res = set()

    for team in teams:
        if len(set(team).intersection(grp3_set)) > 1:
            continue
        res.add(team)
    return res


def generate_teams(mems: List[str],grp1: List[str],grp2: List[str],grp3: List[str],team_size: int) -> Set[Tuple[str,...]]:
    teams = set()  
    teams_nonset = []
    leader_combinations = list(combinations(grp1, 1))
    slots_taken = 1

    for other_mems in combinations(grp2+grp3,team_size-slots_taken):
        for leader_comb in leader_combinations:
            team=list(leader_comb) + list(other_mems)
            teams.add(tuple(team))
    teams = check_grp3(teams,grp3)

    return teams

def teamset_is_valid(teamset: Tuple[Tuple[str,...],...],grp3: List[str]) -> bool:
    mem_occs = Counter()
    #look for repeats in teamset
    for team in teamset:
        for mem in team:
            mem_occs[mem] += 1
            if mem_occs[mem] == 2:
                return False #repeat invalid
    #next lets check that grp3 has at most one member in the set
    grp3_set = {mem for mem in grp3}
    grp3_mems = 0
    for team in teamset:
        #count grp3 mems += length of the current team intersected by grp3_set
        #bcs of way we generated teams before, there will be at most one grp3 member
        #on a team, so this is really checking if any grp3 mems if yes then grp3 count 
        #in the current set is incremented by one
        grp3_mems += len(set(team).intersection(grp3_set))
        if grp3_mems > 1:
            return False
    return True

def write_sets_to_json(fname: str, var: any) -> None:
    try:
        with open(fname,'w',encoding='UTF-8') as file:
            json.dump(var,file,indent=4)
    except FileNotFoundError:
        print("the teamsets.json file does not exist..?")
    except UnicodeEncodeError:
        print("error with teamset.json file")

def generate_sets_of_teams(teams: Set[Tuple[str,...]],grp1: List[str],grp2: List[str], grp3: List[str],num_teams: int) -> Set[Tuple[Tuple[str,...],...]]:
    sets_of_teams = set()
    # logic doesnt seem right below, take a look at old code
    for teamset in combinations(teams,num_teams):
        if teamset_is_valid(teamset=teamset,grp3=grp3):
            sets_of_teams.add(teamset)
    write_sets_to_json(fname=csts.JSON_TEAMSETS_FNAME,var=list(sets_of_teams))
    # ic(len(sets_of_teams))
    # print(sets_of_teams)
    return sets_of_teams

def find_teams_with_olap(teams: Set[Tuple[Tuple[str,...],...]],numteams: str, memsper: str, olap: str, members: List[Member]) -> List[List[List[str]]]:
    ic()
    



        

