import sys

import main_compare as mc
import main_parallel as mp

# res = [<prf_flag>,<rerun_flag>]
def argCheck(args : list)-> list:
    res = [False for _ in range(2)]
    if args[0] == "cmp":
        mc.main()
        sys.exit(0)
    elif args[0] == "prl":
        mp.main()
        sys.exit(0)
    elif args[0] == "prf": #prf must be specified first
        if len(args) > 1:
            if args[1] == "prl":
                mp.main(True)
                sys.exit(0)
            elif args[1] == "rerun" or args[1] == "rr":
                res[0] = True
                res[1] = True
                return res
        else:
            res[0] = True
            return res
    elif args[0] == "rerun":
        res[1] = True
        return res
