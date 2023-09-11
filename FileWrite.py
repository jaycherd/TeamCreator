import sys
import csv
import json
import re

from ComboHolder import ComboHolder




def writeValidSets(fname,combos : ComboHolder):
    # if re.search('win',sys.platform):
    #     os_dependent_var = ''
    # else:
    #     os_dependent_var = '\n'
    # with open(fname,"w+",newline=os_dependent_var,encoding="utf-8") as my_csv:
    #     csv_writer = csv.writer(my_csv,delimiter=',')
    #     csv_writer.writerow(combos.set_of_combos)
    tmp = fname[0:-3] + 'json'
    print(tmp)
    with open(tmp,"w+",encoding="utf-8") as my_json:
        json.dump(combos.set_of_combos,my_json)

