#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for arg_n in range(1, len(sys.argv)):
        result += int(sys.argv[arg_n])
    print(result)
