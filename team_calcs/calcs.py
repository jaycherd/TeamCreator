import json
import math
from typing import List,Set,Tuple,Dict
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

def convert_intersection(intrsxn: Set[str]) -> Tuple[Tuple[str]]:
    sorted_intrsxn = sort_intrsxn(intrsxn=intrsxn)
    compressed_intrsxn = compress_intrsxn(sorted_intrsxn)
    return compressed_intrsxn

    # team_intersected = {} #key is str(mem_id) + str(mem_id of other mems) val is result of intersection
    # for teamset in teamsets:
    #     for team in teamset:
    #         sets = []#will be a list of sets
    #         teamkey = getkey(team)
    #         if teamkey in team_intersected:
    #             intersection_res = team_intersected[teamkey]
    #         else:
    #             for mem in team:
    #                 member = mems_dict.get(int(mem))
    #                 sets.append(member.available_minutes)
    #             intersection_res = set.intersection(*sets) #should intersect all the sets in the list at once! lit
    #             team_intersected[teamkey] = intersection_res
    # return team_intersected
def sort_intrsxn(intrsxn: Set[str]) -> Tuple[str]:
    sorted_intrsxn = list(intrsxn)
    sorted_intrsxn.sort(key=lambda time: (int(time.split('-')[1]),int(time.split(':')[0]),int(time.split(':')[1].split('-')[0])))
    #dope fxn above does this: sort by day, then by hour, then by minute! sick
    return tuple(sorted_intrsxn)

def getkey(team: Tuple[str,...]) -> str:
        currkey = ""
        for mem in team:
            currkey += mem
        return currkey

def generate_teams(mems: List[str],grp1: List[str],grp2: List[str],grp3: List[str],
                   team_size: int,mems_dict: Dict[int,Member],olap: float) -> Tuple[Set[Tuple[str,...]],Dict[Tuple[str,...],Tuple[str,...]]]:
    teams_intersected : Dict[Tuple[str,...],Set[str]] = {}
    def check_team(team: Tuple[str,...],mems_dict: Dict[int,Member],olap: float) -> bool:
        # Collect the sets of available minutes for each team member
        sets_of_avails : List[Set[str]] = [mems_dict[int(mem_id)].available_minutes for mem_id in team]
        # Use set.intersection to find the common availability
        common_avails : Set[str] = set.intersection(*sets_of_avails)
        if len(common_avails) < olap*60:
            return False
        nonlocal teams_intersected
        teams_intersected[getkey(team)] = convert_intersection(common_avails)
        return True
    teams = set()
    grp2_and_grp3 = grp2 + grp3

    # Generate teams with at most one member from grp3
    for leader in grp1:
        for other_members in combinations(grp2_and_grp3, team_size - 1):
            team = (leader,) + other_members
            if sum(member in grp3 for member in other_members) <= 1 and check_team(team,mems_dict,olap):
                teams.add((leader,) + other_members)

    print(f"generated {len(teams)} teams")
    return (teams, teams_intersected)

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
    num_sets_gen = 0
    def add_team_to_set(current_set, remaining_teams):
        nonlocal num_sets_gen
        if len(current_set) == num_teams:
            sets_of_teams.add(current_set)
            num_sets_gen += 1
            if num_sets_gen == csts.NUM_SETS_TO_GEN:
                raise StopIteration
            return
        
        for team in remaining_teams:
            new_set = current_set + (team,)
            if teamset_is_valid(new_set, grp3):
                next_teams = remaining_teams - {team}
                try:
                    add_team_to_set(new_set, next_teams)
                except StopIteration:
                    raise StopIteration
                if num_sets_gen == csts.NUM_SETS_TO_GEN:
                    break
    
    all_teams = set(teams)
    try:
        add_team_to_set(tuple(), all_teams)
    except StopIteration:
        worst_case = math.comb(len(teams),num_teams)
        print(f"Team permutations generated was restricted by " +
              "utility/constants.py variable -> NUM_SETS_TO_GEN," +
              f" set to {csts.NUM_SETS_TO_GEN},\nNOTE: worst case" +
              f" {len(teams)} teams could make {worst_case}" +
              " permutations, which could take a long time" +
              ", consider increasing overlap")
    
    print(f"permutations of teams -> {len(sets_of_teams)}")
    return sets_of_teams


def find_teams_w_olap(teams_intersected_map: Dict[str,Set[str]],mems_dict: Dict[int,Member],teamsets: Tuple[Tuple[Tuple[str,...],...]],olap: float) -> Tuple[int]:
    #rtype: List[int] -> nums correspond to teamset_ids found to be valid
    val_teamsets = []
    teamset_id = -1
    for teamset in teamsets:
        teamset_id += 1
        continueflag = False
        for team in teamset:
            teamkey = getkey(team=team)
            avail_mins_common = teams_intersected_map[teamkey]
            if len(avail_mins_common) < olap*60:
                continueflag = True
                break
        if continueflag:
            continue
        val_teamsets.append(teamset_id)
    return tuple(val_teamsets)

def compress_intrsxn(sorted_intrsxn: Tuple[str]) -> Tuple[Tuple[str]]:
    starts,ends = [], []
    starts.append(sorted_intrsxn[0])
    #next find the first end
    for i in range(len(sorted_intrsxn)-1):
        curr_str = sorted_intrsxn[i]
        curr_day = int(curr_str.split('-')[1])
        curr_hour = int(curr_str.split(':')[0])
        curr_min = int(curr_str.split(':')[1].split('-')[0]) + (curr_hour * 60)
        next_str = sorted_intrsxn[i+1]
        next_day = int(next_str.split('-')[1])
        next_hour = int(next_str.split(':')[0])
        next_min = int(next_str.split(':')[1].split('-')[0]) + (next_hour * 60)
        if curr_day != next_day or next_min != curr_min + 1:
            ends.append(curr_str)
            starts.append(next_str)
    ends.append(sorted_intrsxn[-1])
    return (tuple(starts),tuple(ends))

def convert_team_intersections(teams_intersected_map: Dict[str,Set[str]],mems_dict: Dict[int,Member], teamsets: Tuple[Tuple[Tuple[str,...],...]]) -> Dict[int,Tuple[Tuple[str]]]:
    #rtype: Dict[key=teamset_id,val=List[List[str]] = the common start,end avails, row = day, evencols = start olap, oddcols = end olap]
    # res_dict = {}
    # for i,(k,v) in enumerate(teams_intersected_map.items()):
    #     start_end_tups = []
    #     for team in v:
    #         # print(f"k -> {k}, type k is -> {type(k)}")
    #         # print(f"v -> {v}, type v is {type(v)}")
    #         start_end_tup = convert_intersection(teams_intersected_map[k])
    #         start_end_tups.append(start_end_tup)
    #     res_dict[i] = tuple(start_end_tups)
    # return res_dict
    
    
    # res_dict = {}
    # for perm in teamsets:
    #     start_end_tups = []
    #     for team in perm:
    #         start_end_tup = convert_intersection(team)
    #         start_end_tups.append(start_end_tup)
    #     res_dict[team] = tuple(start_end_tups)
    # return res_dict

    
    # print(teamsets)
    # print(teamset_ids)
    res_dict = {}
    for i,teamset in enumerate(teamsets):
        start_end_tups = []
        for team in teamset:
            teamkey = getkey(team)
            intersxn = teams_intersected_map[teamkey]
            start_end_tup = intersxn
            start_end_tups.append(start_end_tup)
        res_dict[i] = tuple(start_end_tups)
    return res_dict
    # res_dict = {}
    # for teamset_id in teamset_ids:
    #     teams = teamsets[teamset_id]
    #     start_end_tups = []
    #     for team in teams:
    #         teamkey = getkey(team=team)
    #         intersxn = teams_intersected_map[teamkey]
    #         start_end_tup = convert_intersection(intrsxn=intersxn)
    #         start_end_tups.append(start_end_tup)
    #     res_dict[teamset_id] = tuple(start_end_tups)
    # # print(res_dict)
    # return res_dict

"""0 = success, 1 = error"""
def check_cmp_input(input: str,valid_names: Set[str]) -> Tuple[int,str]:
    #first convert the input to a list
    input_lst = input.replace(' ','').split(',')
    for name in input_lst:
        if name == '':
            return (-2,'')
        if name not in valid_names:
            return (-1,name)
    return 0,'' #success

def convert_names2id(names: List[str], mems: List[Member]) -> List[int]:
    res = []
    for name in names:
        for mem in mems:
            if mem.name == name:
                res.append(mem.member_id)
                break
    return res

def find_cmp_olap(ids: List[int], mems_dict: Dict[int,Member]) -> Set[str]:
    sets = []#will be a list of sets
    for id in ids:
        member = mems_dict.get(int(id))
        sets.append(member.available_minutes)
    return set.intersection(*sets) #should intersect all the sets in the list at once! lit


# deprecated
# this is now done during generation of teams to avoid creating teams that dont have valid overlap
# decreasing time by stopping generation of unneccessary sets
# def intersect_team_avail_mins(teamsets: Set[Tuple[Tuple[str,...],...]],numteams: str, memsper: str, olap: str, members: List[Member],mems_dict: Dict[int,Member]) -> Dict[str,Set[str]]:
#     #okay so members now have an additional attribute --> a set, the set is of every single minute that that person is available
#     #gotten by turning their start and end times into avail minutes
#     team_intersected = {} #key = str(mem_id) + str(mem_id of other mems), val = result of intersection
#     for teamset in teamsets:
#         for team in teamset:
#             sets = []#will be a list of sets
#             teamkey = getkey(team)
#             if teamkey in team_intersected:
#                 intersection_res = team_intersected[teamkey]
#             else:
#                 for mem in team:
#                     member = mems_dict.get(int(mem))
#                     sets.append(member.available_minutes)
#                 intersection_res = set.intersection(*sets) #should intersect all the sets in the list at once! lit
#                 team_intersected[teamkey] = intersection_res
#     return team_intersected