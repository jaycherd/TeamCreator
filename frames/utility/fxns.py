from typing import List


def generate_grp_string(group: List[str]) -> str:
    res = ""
    for i in range(len(group)):
        if i != 0:
            res += ", "
        res += group[i]
    return res