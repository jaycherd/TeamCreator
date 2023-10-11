import json
from typing import List,Set,Tuple,Dict
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

def find_teams_with_olap(teamsets: Set[Tuple[Tuple[str,...],...]],numteams: str, memsper: str, olap: str, members: List[Member],mems_dict: Dict[int,Member]) -> List[List[List[str]]]:
    def getkey(team: Tuple[str,...]) -> str:
        currkey = ""
        for mem in team:
            currkey += mem
        return currkey
    ic()
    #okay so members now have an additional attribute --> a set, the set is of every single minute that that person is available
    #gotten by turning their start and end times into avail minutes
    #idea: use that set, and perform intersection on members,
    #optimization: intersection between two mems that result in zero common time, should not be performed again, maybe as i am
    #performing intersection, i should store in a map, the result of two mems getting intersected
    #then before intersecting two mems, check if its been done yet if has then just
    #use that value rather than intersecting it again
    #initially an easier intersection may be if two mems, have ZERO common time, then store them in a zero_common_map and if you come across
    #then break and dont do any calcs, this optimization might be worth finding in the beginning which mems have no common
    #altho i do think be better to find this as we go through the calcs
    #a lot to think about, how can this be impl...
    teamset_id = -1
    teamsets_w_ovrlap = set()
    team_intersected = {} #key is str(mem_id) + str(mem_id of other mems) val is result of intersection
    ic(teamsets)
    for teamset in teamsets:
        teamset_id += 1
        for team in teamset:
            sets = []#will be a list of sets
            teamkey = getkey(team)
            shortcut_flag = False
            if teamkey in team_intersected:
                intersection_res = team_intersected[teamkey]
                shortcut_flag = True
            else:
                for mem in team:
                    member = mems_dict.get(int(mem))
                    sets.append(member.available_minutes)
                intersection_res = set.intersection(*sets) #should intersect all the sets in the list at once! lit
                team_intersected[teamkey] = intersection_res
    ic(len(team_intersected))
    ic(team_intersected)
    #next probs check if the intersection creates a valid amount of overlapping minutes, could probs just divide by 60 and check whether this float is 
    #greater than user input float
    #maybe some checking that its working and what not first
    #if this works good, maybe ill just keep as is, and have teamkeys map to an intersection of the minutes overlap,
    #that way, i can later iterate through the team_intersected map to check whether intersections make a valid team or not..?
    #swag yeah that seemed to work, so lets do it like that, also i noticed that there were five empty sets, this will help with shortcutting
    #now i can call another function, with the map team_intersected, actually lets return the map, to the gui, the from homeframe
    #call another fxn with that returned map, and that fxn will find all the sets with valid overlap and return them.. wait so the other fxn
    #will also ned the teamsets.. then do the same shortcut via my map, except this time, every teamkey should be in the map, so we can lookup
    #all the vals without doing any intersecting of giant sets..



        

