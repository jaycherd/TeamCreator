import main_compare as mc
import main_parallel as mp

def ArgCheck(args : list()):
    if(args[0] == "cmp"):
        mc.main()
    elif(args[0] == "prl"):
        mp.main()