import pandas as pd

def printGroups(lst1,lst2,lst3):
    print(f"group1: {lst1}\ngroup2: {lst2}\ngroup3: {lst3}")


class GroupPriorityFile:
    filename = str
    group1 = list()
    group2 = list()
    group3 = list()

    def __init__(self,filename) -> None:
        self.filename = filename
        df = pd.read_csv(self.filename,header=None)
        self.group1 = df.loc[0,1:].values.flatten().tolist()
        self.group2 = df.loc[1,1:].values.flatten().tolist()
        self.group3 = df.loc[2,1:].values.flatten().tolist()


