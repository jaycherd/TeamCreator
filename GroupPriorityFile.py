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
        tmp1 = df.loc[0,1:].values.flatten().tolist()
        tmp2 = df.loc[1,1:].values.flatten().tolist()
        tmp3 = df.loc[2,1:].values.flatten().tolist()
        for member in tmp1:
            if pd.isna(member):
                continue
            self.group1.append(member)
        for member in tmp2:
            if pd.isna(member):
                continue
            self.group2.append(member)
        for member in tmp3:
            if pd.isna(member):
                continue
            self.group3.append(member)
        # printGroups(self.group1,self.group2,self.group3)
        


