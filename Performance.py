import time as t

class Performance:

    def __init__(self):
        self.start_time = t.perf_counter()
        self.start_time_p = 0
        self.end_time = 0
        self.end_time_p = 0
        self.start_time_combo = 0
        self.end_time_combo = 0
        self.start_time_sfinder = 0
        self.end_time_sfinder = 0
        self.start_time_sf_init = 0
        self.end_time_sf_init = 0
        self.start_time_sf_cmod = 0
        self.end_time_sf_cmod = 0
        self.start_time_sf_csd = 0
        self.end_time_sf_csd = 0
        self.start_time_sf_ccd = 0
        self.end_time_sf_ccd = 0
        self.start_time_sf_dgs = 0
        self.end_time_sf_dgs = 0
    
    def printStart(self):
        self.start_time_p = t.perf_counter()

    def printEnd(self):
        self.end_time_p = t.perf_counter()

    def start(self):
        self.start_time = t.perf_counter()
    
    def end(self):
        self.end_time = t.perf_counter()

    def startCombo(self):
        self.start_time_combo = t.perf_counter()

    def endCombo(self):
        self.end_time_combo = t.perf_counter()

    def startSetFinder(self):
        self.start_time_sfinder = t.perf_counter()
    
    def endSetFinder(self):
        self.end_time_sfinder = t.perf_counter()

    def startSFInit(self):
        self.start_time_sf_init = t.perf_counter()
    
    def endSFInit(self):
        self.end_time_sf_init = t.perf_counter()

    def startSFCMOD(self):
        self.start_time_sf_cmod = t.perf_counter()
    
    def endSFCMOD(self):
        self.end_time_sf_cmod = t.perf_counter()

    def startSFCSD(self):
        self.start_time_sf_csd = t.perf_counter()
    
    def endSFCSD(self):
        self.end_time_sf_csd = t.perf_counter()

    def startSFCCD(self):
        self.start_time_sf_ccd = t.perf_counter()
    
    def endSFCCD(self):
        self.end_time_sf_ccd = t.perf_counter()
    
    def startSFDGS(self):
        self.start_time_sf_dgs = t.perf_counter()
    
    def endSFDGS(self):
        self.end_time_sf_dgs = t.perf_counter()

    def drawPerformance(self):
        print(f"\n----------------------------------------------------------------")
        print(f"Program performance:")
        print(f"Overall : {(self.end_time - self.start_time):.4f} seconds")
        print(f"Combo   : {(self.end_time_combo - self.start_time_combo):.4f} seconds")
        print(f"SFinder : {(self.end_time_sfinder - self.start_time_sfinder):.4f} seconds")
        if(self.end_time_sf_init != 0):
            print(f"SF Init : {(self.end_time_sf_init - self.start_time_sf_init):.4f} seconds")
        if(self.end_time_sf_cmod != 0):
            print(f"SF CMOD : {(self.end_time_sf_cmod - self.start_time_sf_cmod):.4f} seconds")
        if(self.end_time_sf_csd != 0):
            print(f"SF CSD  : {(self.end_time_sf_csd - self.start_time_sf_csd):.4f} seconds")
        if(self.end_time_sf_ccd != 0):
            print(f"SF CCD  : {(self.end_time_sf_ccd - self.start_time_sf_ccd):.4f} seconds")
        if(self.end_time_sf_dgs != 0):
            print(f"SF DGS  : {(self.end_time_sf_dgs - self.start_time_sf_dgs):.4f} seconds")
        # print(f"Prints  : {(self.end_time_p - self.start_time_p):.4f} seconds")
        print(f"----------------------------------------------------------------\n")