import sys

import main_compare as mc
import main_parallel as mp


def argCheck(args : list):
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
        else:
            return
