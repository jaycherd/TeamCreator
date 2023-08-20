import pandas as pd
import numpy as np
import re



def drawMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=", ")
        print("\n")

def drawDictionary(dic):
    print(f"the dictionary contents are: ", end = "")
    for k,v in dic.items():
        print(f"{k} : {v}", end=", ")
    print("\n")

def drawAvailMatrix(matrix):
    print(f"the avail matrix is: \n")
    for row in matrix:
        i = -1
        print(f"\n\n{row[0]}")
        for col in row:
            i += 1
            if(i == 0): continue
            print(col, end = "\t")
            if i % 2 == 0 : print()
    print()    
    




class AvailabilityFile:
    filename = str
    names = list #parallel to the matrix
    name_avail_matrix = list(list()) #as a matrix -> row lines up with the person, col with day of week
    day_index_arr = list()



    def __init__(self,filename) -> None:
        self.filename = filename
        df = pd.read_csv(self.filename)
        name_column = df.columns[0]
        names = df[name_column]
        self.names = list(names)

        #first an array, holding indexes of each day of the week
        day_arr_index = 0
        for col in df.columns:
            if(re.search('na',col.lower()) != None): #this will ignore the name column, and any columns which are un'na'med, which is defualt val to dataframe by pandas
                day_arr_index += 1
                continue
            self.day_index_arr.append(day_arr_index)    
            day_arr_index += 1


        # next create name/availabilities matrix
        for index, row in df.iterrows():
            tmp_list = pd.to_datetime(list(df.iloc[index][1:]),errors='coerce',format='%H:%M')
            tmp_list2 = list()
            curr_day = 0
            day_offset = -1
            i = 0
            #below can be optimized found solution on stack overflow, use strftime('%H:%M').tolist()")
            for item in tmp_list: #have to do this cus without this loop the types are weird, this makes a list of timestamp/NaT types if cant be converted
                i += 1 #starting at one cus the name gets added later and i wanna account for that so it is parallel with the dictionary
                if curr_day <= len(self.day_index_arr) - 1 and i >= self.day_index_arr[curr_day]: # using day index array gets the correct day offset for corresponding day
                    day_offset += 1
                    curr_day += 1
                if pd.isnull(item) == True: # if its NaT which is what pandas makes stuff when it wont convert to datetime, then do nothing
                    tmp_list2.append(item)
                    continue
                tmp_list2.append(item + pd.DateOffset(days=day_offset)) #append the current item to a tmp list, but with the addition of the curr day offset
            tmp_list2.insert(0,self.names[index]) #insert the name of the person the avails correspond to at the beginning of the list
            self.name_avail_matrix.append(tmp_list2) # finally append the tmp list to the matrix for the priority file object

        # drawAvailMatrix(self.name_avail_matrix)      
    

        






