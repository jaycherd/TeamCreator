import config
from AvailabilityFile import AvailabilityFile
from GroupPriorityFile import GroupPriorityFile

import pandas as pd

avail_obj = AvailabilityFile(config.csv_availability_filename)
pri_obj = GroupPriorityFile(config.csv_priority_filename)



