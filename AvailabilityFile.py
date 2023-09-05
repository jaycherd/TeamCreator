import re
import pandas as pd


def drawMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=", ")
        print("\n")

def drawDictionary(dic):
    print("the dictionary contents are: ", end = "")
    for k,v in dic.items():
        print(f"{k} : {v}", end=", ")
    print("\n")

def drawAvailMatrix(matrix):
    print("the avail matrix is: \n")
    for row in matrix:
        i = -1
        print(f"\n\n{row[0]}")
        for col in row:
            i += 1
            if i == 0:
                continue
            print(col, end = "\t")
            if i % 2 == 0 :
                print()
    print()




class AvailabilityFile:
    """Read/extract info from Avail File CSV"""
    filename = str
    names = list #parallel to the matrix
    name_avail_matrix = [] #as matrix -> row - person, col - day of week
    day_index_arr = []
    DEFAULTDAYS = 4



    def __init__(self,filename) -> None:
        self.filename = filename
        df = pd.read_csv(self.filename)
        name_column = df.columns[0]
        names = df[name_column]
        self.names = list(names)

        #first an array, holding indexes of each day of the week
        day_arr_index = 0
        for col in df.columns:
            #will ignore name col/any cols which are un'na'med, which defualt val dframe by pandas
            if re.search('na',col.lower()) is not None:
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
            #below can be optimized found sol on stack overflow, use strftime('%H:%M').tolist()")
            #have to do cus w/out loop types are weird, makes list of timestamp
            # NaT types if cant be converted
            for item in tmp_list:
                i += 1 #strt at one cus name added later/wanna accnt for that so it prl w/dict
                 # using day index array gets the correct day offset for corresponding day
                if curr_day <= len(self.day_index_arr) - 1 and i >= self.day_index_arr[curr_day]:
                    day_offset += 1
                    curr_day += 1
                # if NaT which is what pandas does when wont convert to datetime, then do nothing
                if pd.isnull(item) is True:
                    tmp_list2.append(item)
                    continue
                #append current item to a tmp list, but with the addition of the curr day offset
                tmp_list2.append(item + pd.DateOffset(days=day_offset))
            #insert the name of the person the avails correspond to at the beginning of the list
            tmp_list2.insert(0,self.names[index])
            # finally append the tmp list to the matrix for the priority file object
            self.name_avail_matrix.append(tmp_list2)

        # drawAvailMatrix(self.name_avail_matrix)
