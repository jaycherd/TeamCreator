import main_compare as mc
import main_parallel as mp
import main_performance as mperf
from Performance import Performance

def ArgCheck(args : list()):
    if(args[0] == "cmp"):
        mc.main()
    elif(args[0] == "prl"):
        mp.main(False)
    elif(args[0] == "prf"): #prf must be specified first
        P = Performance()
        if(len(args) > 1):
            if(args[1] == "prl"):
                mp.main(True)
                P.end()
                P.drawPerformance()
        else:
            mperf.main()
            P.end()
            P.drawPerformance()
