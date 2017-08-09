#!/usr/bin/env python3

import random

aLength = random.randint(10, 15)
bLength = random.randint(10, 15)

a = []
b = []
overlap = []

# Generate list a
for num in range(0, aLength):
    a.append(random.randint(1, 25))

# Generate list b
for num in range(0, bLength):
    b.append(random.randint(1, 25))

# Find those overlaps
for item in a:
    if item in b and item not in overlap:
        overlap.append(item)

# Print the overlap list
print(overlap)
