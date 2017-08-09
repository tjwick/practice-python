#!/usr/bin/env python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

lessThan = int(input("Number: "))

for item in a:
    if item < lessThan:
        b.append(item)

print(b)
