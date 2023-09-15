import config
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile

class ErrorChecker:
    HELPSTR = "Please read the README if you are still having trouble to see how csv should be formatted and other helpful stuffs  \U0001F44D"
    av_obj = AvailabilityFile
    def __init__(self) -> None:
        pass

    def checkAvail(self,avail_obj):
        self.av_obj = avail_obj
        if len(avail_obj.names) < config.NUMBER_OF_TEAMS * config.TEAM_SIZE:
            print(f"ERROR: you asked to create {config.NUMBER_OF_TEAMS} teams of {config.TEAM_SIZE} members which requires at least", end = " ")
            print(f"{config.NUMBER_OF_TEAMS * config.TEAM_SIZE} members but there were only {len(avail_obj.names)} members provided in your csv")
            print(self.HELPSTR)
            exit()
    
    def checkGroupPri(self,gp_obj = GroupPriorityFile):
        gp_names = gp_obj.group1 + gp_obj.group2 + gp_obj.group3
        if len(gp_names) != len(self.av_obj.names):
            print(f"ERROR: the number of members read from the group priority csv file was {len(gp_names)}",end=" ")
            print(f" which does not match with the number of members read from the availability csv {len(self.av_obj.names)}")
            print(self.HELPSTR)
            exit()
        if (len(gp_obj.group2) == 0):
            print(f"ERROR: group2 must not be empty bru")
            print(self.HELPSTR)
            exit()

    def checkCompare(self,cmp_lst,mem_list):
        max_num = len(mem_list)-1
        for num in cmp_lst:
            if str(num).isnumeric() == False:
                print(f"ERROR: please only enter numbers  \U0001F611")
                print(f"Also make sure you're only entering numbers and commas, no comma at the end, no spaces, thanks bro")
                print(self.HELPSTR)
                exit()
            if int(num) > max_num:
                print(f"ERROR: number ({num}) is greater than the max allowed value of {max_num}")
                print(self.HELPSTR)
                exit()
            if int(num) < 0:
                print(f"ERROR: no negative nums pls")
                print(self.HELPSTR)
                exit()

        
        
