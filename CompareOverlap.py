class CompareOverlap:
    keyName_valAvailableMinutes = {}
    ppl_to_cmp = []
    overlap = []
    sorted_overlap = []
    cmprsd_overlap = []

    def __init__(self,dc) -> None:
        self.keyName_valAvailableMinutes = dc
        self.ppl_to_cmp = list(dc.keys())

    def findOverlap(self) -> None:
        #####################################################inner fxns#######################
        ######################################################################################
        def sortOverlap(arr):
            def key2SortBy(strng):
                return int(strng[0:1])
            def key2SortByTieBrk(strng):
                return int(strng[2:4])
            def key2SortByTieBrk2(strng):
                return int(strng[5:])
            res = list(arr)
            res.sort(key=lambda x : (key2SortBy(x),key2SortByTieBrk(x),key2SortByTieBrk2(x)))
            return res.copy()
        def compressDictionary(arr):
            if len(arr) == 0:
                return
            starts = []
            ends = []
            starts.append(arr[0])
            for i in range(len(arr)-1):#time format %w %H:%M
                curr_str = arr[i]
                curr_day = int(curr_str[0:1])
                curr_hour = int(curr_str[2:4])
                curr_min = int(curr_str[5:]) + (curr_hour*60)
                next_str = arr[i+1]
                next_day = int(next_str[0:1])
                next_hour = int(next_str[2:4])
                next_min = int(next_str[5:]) + (next_hour*60)
                if(curr_day != next_day or next_min != curr_min + 5):
                    ends.append(curr_str)
                    starts.append(next_str)
            ends.append(arr[-1])
            res = []
            res.append(starts)
            res.append(ends)
            return res
        #################################################################################
        #################################################################################
        common_times = []
        for i in range(len(self.ppl_to_cmp) - 1):
            curr_mem = self.ppl_to_cmp[i]
            next_mem = self.ppl_to_cmp[i+1]
            if i == 0: #continuously intersect sets to remove uncommon times in O(n)
                common_times = set(self.keyName_valAvailableMinutes.get(curr_mem)).\
                    intersection(self.keyName_valAvailableMinutes.get(next_mem))
            else:
                common_times = set(common_times).\
                    intersection(self.keyName_valAvailableMinutes.get(next_mem))
        tmp = list(common_times)
        self.overlap = tmp.copy()
        self.sorted_overlap = sortOverlap(self.overlap.copy())
        self.cmprsd_overlap = compressDictionary(self.sorted_overlap.copy())


    def drawOverlap(self) -> None:
        #####################################################inner fxns#############
        ############################################################################
        def convertNum2Day(str) -> str:
            day_of_week = str[0:1]
            if day_of_week == '0':
                return 'Mon - ' + str[2:]
            elif day_of_week == '1':
                return 'Tue - ' + str[2:]
            elif day_of_week == '2':
                return 'Wed - ' + str[2:]
            elif day_of_week == '3':
                return 'Thr - ' + str[2:]
            elif day_of_week == '4':
                return 'Fri - ' + str[2:]
            elif day_of_week == '5':
                return 'Sat - ' + str[2:]
            elif day_of_week == '6':
                return 'Sun - ' + str[2:]
            return str
        ########################################################################
        ########################################################################
        if len(self.overlap) == 0:
            print("this team has no common time!")
            return

        for i in range(len(self.cmprsd_overlap[0])):
            if self.cmprsd_overlap[0][i] == self.cmprsd_overlap[1][i]:
                continue
            print(f"{convertNum2Day(self.cmprsd_overlap[0][i])} to ", end="")
            print(f"{(self.cmprsd_overlap[1][i])[2:]}")
