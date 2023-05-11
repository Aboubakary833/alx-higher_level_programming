#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} argument".format(len(sys.argv) - 1), end="")
    print("{}:".format("s" if len(sys.argv) != 2 else ""))
    for arg_n in range(1, len(sys.argv)):
        print("{}: {}".format(arg_n, sys.argv[arg_n]))
