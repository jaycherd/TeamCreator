################################################################################################################################
# Default values at app startup
# Specify the team size
team_size = 3
number_of_teams = 3
# min num days youd like the team members to have in common
minDaysOverlap = 1
# the min num hours of overlap
MIN_HRS_OLAP = 2

# the value to stop generating new sets
# helps keep program from running super long
NUM_SETS_TO_GEN = 150

# the name of the csv file
csv_avail_fname = 'resources/availability.csv'
csv_pri_fname = 'resources/group_priority.csv'
json_mem_fname = 'utility/mems.json'
JSON_TEAMSETS_FNAME = 'utility/teamsets.json'
# # to see some extra info for debugging purposes make this var True
debug = False
################################################################################################################################