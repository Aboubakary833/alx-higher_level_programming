#!/usr/bin/python3
for n in range(100):
    print(f"{n:02d}, ".format(n) if n < 99 else (f"{n}"), end="")
print("")
