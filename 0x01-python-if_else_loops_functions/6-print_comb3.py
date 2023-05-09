#!/usr/bin/python3
for n in range(10):
    for m in range(n + 1, 10):
        print("{}{}, ".format(n, m) if n != 8 else f"{n}{m}", end="")
print("")
