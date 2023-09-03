import time as t

class Performance:

    def __init__(self):
        self.start_time = t.perf_counter()
        self.start_time_p = 0
        self.end_time = 0
        self.end_time_p = 0
    
    def printStart(self):
        self.start_time_p = t.perf_counter()

    def printEnd(self):
        self.end_time_p = t.perf_counter()

    def start(self):
        self.start_time = t.perf_counter()
    
    def end(self):
        self.end_time = t.perf_counter()

    def drawPerformance(self):
        print(f"\n----------------------------------------------------------------")
        print(f"Program performance:\nOverall : {(self.end_time - self.start_time):.4f} seconds")
        # print(f"Prints  : {(self.end_time_p - self.start_time_p):.4f} seconds")
        print(f"----------------------------------------------------------------\n")