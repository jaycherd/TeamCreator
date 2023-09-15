import sys

import main_compare as mc

HELP_STR = """
    program usage: 'python main.py <flags>'
    note flags are optional \U0001F6A9
    flags:
        cmp - compare two or more specific members common times
        prf - print out program performance for improvement purposes
                prf flag can be run with 'rr' flag but prf must be first flag
        rr  - rerun program, use if made changes that aren't getting detected
"""

# res = [<prf_flag>,<rerun_flag>]
def argCheck(args : list)-> list:
    res = [False for _ in range(2)]
    if args[0] == "cmp":
        mc.main()
        sys.exit(0)
    elif args[0] == "prl":
        sys.exit(0)
    elif args[0] == "prf": #prf must be specified first
        if len(args) > 1:
            if args[1] == "rerun" or args[1] == "rr":
                res[0] = True
                res[1] = True
                return res
            print(HELP_STR)
            sys.exit(0)
        else:
            res[0] = True
            return res
    elif args[0] == "rerun" or args[0] == "rr":
        res[1] = True
        return res
    elif args[0] == "h" or args[0] == "help":
        print(HELP_STR)
    else:
        print("ERROR: invalid flag(s)")
        print(HELP_STR)
    sys.exit(0)
