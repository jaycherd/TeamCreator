import time as t

class Performance:
    """class for tracking program performance"""
    def __init__(self):
        self.srt_t = t.perf_counter()
        self.srt_t_p = 0
        self.end_t = 0
        self.end_t_p = 0
        self.srt_t_combo = 0
        self.end_t_combo = 0
        self.srt_t_sfinder = 0
        self.end_t_sfinder = 0
        self.srt_t_sf_init = 0
        self.end_t_sf_init = 0
        self.srt_t_sf_cmod = 0
        self.end_t_sf_cmod = 0
        self.srt_t_sf_csd = 0
        self.end_t_sf_csd = 0
        self.srt_t_sf_ccd = 0
        self.end_t_sf_ccd = 0
        self.srt_t_sf_dgs = 0
        self.end_t_sf_dgs = 0
        self.srt_t_ea = 0
        self.end_t_ea = 0
        self.srt_t_eagd = 0
        self.end_t_eagd = 0

    def printStart(self):
        self.srt_t_p = t.perf_counter()

    def printEnd(self):
        self.end_t_p = t.perf_counter()

    def start(self):
        self.srt_t = t.perf_counter()

    def end(self):
        self.end_t = t.perf_counter()

    def startCombo(self):
        self.srt_t_combo = t.perf_counter()

    def endCombo(self):
        self.end_t_combo = t.perf_counter()

    def startEA(self):
        self.srt_t_ea = t.perf_counter()

    def endEA(self):
        self.end_t_ea = t.perf_counter()

    def startEAGD(self):
        self.srt_t_eagd = t.perf_counter()

    def endEAGD(self):
        self.end_t_eagd = t.perf_counter()

    def startSetFinder(self):
        self.srt_t_sfinder = t.perf_counter()

    def endSetFinder(self):
        self.end_t_sfinder = t.perf_counter()

    def startSFInit(self):
        self.srt_t_sf_init = t.perf_counter()

    def endSFInit(self):
        self.end_t_sf_init = t.perf_counter()

    def startSFCMOD(self):
        self.srt_t_sf_cmod = t.perf_counter()

    def endSFCMOD(self):
        self.end_t_sf_cmod = t.perf_counter()

    def startSFCSD(self):
        self.srt_t_sf_csd = t.perf_counter()

    def endSFCSD(self):
        self.end_t_sf_csd = t.perf_counter()

    def startSFCCD(self):
        self.srt_t_sf_ccd = t.perf_counter()

    def endSFCCD(self):
        self.end_t_sf_ccd = t.perf_counter()

    def startSFDGS(self):
        self.srt_t_sf_dgs = t.perf_counter()

    def endSFDGS(self):
        self.end_t_sf_dgs = t.perf_counter()

    def drawPerformance(self):
        print("\n----------------------------------------------------------------")
        print("Program performance:")
        print(f"Overall : {(self.end_t - self.srt_t):.4f} seconds")
        print(f"Combo   : {(self.end_t_combo - self.srt_t_combo):.4f} seconds")
        if self.end_t_ea != 0:
            print(f"EA      : {(self.end_t_ea - self.srt_t_ea):.4f} seconds")
        if self.end_t_eagd != 0:
            print(f"EAGD    : {(self.end_t_eagd - self.srt_t_eagd):.4f} seconds")
        if self.end_t_sfinder != 0:
            print(f"SFinder : {(self.end_t_sfinder - self.srt_t_sfinder):.4f} seconds")
        if self.end_t_sf_init != 0:
            print(f"SF Init : {(self.end_t_sf_init - self.srt_t_sf_init):.4f} seconds")
        if self.end_t_sf_cmod != 0:
            print(f"SF CMOD : {(self.end_t_sf_cmod - self.srt_t_sf_cmod):.4f} seconds")
        if self.end_t_sf_csd != 0:
            print(f"SF CSD  : {(self.end_t_sf_csd - self.srt_t_sf_csd):.4f} seconds")
        if self.end_t_sf_ccd != 0:
            print(f"SF CCD  : {(self.end_t_sf_ccd - self.srt_t_sf_ccd):.4f} seconds")
        if self.end_t_sf_dgs != 0:
            print(f"SF DGS  : {(self.end_t_sf_dgs - self.srt_t_sf_dgs):.4f} seconds")        
        # print(f"Prints  : {(self.end_t_p - self.srt_t_p):.4f} seconds")
        print("----------------------------------------------------------------\n")
