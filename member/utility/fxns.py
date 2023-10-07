from datetime import datetime
from typing import List
from icecream import ic


def check_avail_matrix(matrix: List[List[str]]) -> bool:
    for day in matrix:
        for time in day:
            try:
                datetime.strptime(time,'%H:%M')
            except ValueError:
                return False
    return True