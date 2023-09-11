import json

from ComboHolder import ComboHolder


def writeValidSets(fname,combos : ComboHolder):
    with open(fname,"w+",encoding="utf-8") as my_json:
        json.dump(combos.set_of_combos,my_json)
