import config
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile
from ComboHolder import ComboHolder

import pandas as pd

# get availability file info
avail_obj = AvailabilityFile(config.csv_availability_filename)
# get priority file info
pri_obj = GroupPriorityFile(config.csv_priority_filename)

# next generate a list of every possible combination and set of combos in the combo object
combo_obj = ComboHolder(config.team_size,config.number_of_teams,pri_obj.group1,pri_obj.group2,pri_obj.group3)
combo_obj.createCombos()
combo_obj.createSets()

