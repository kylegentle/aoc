#!/usr/bin/env python3
from collections import Counter

left = []
right = []
with open("inputs/d1.txt") as f:
    for line in f:
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

distance = 0
for l, r in zip(sorted(left), sorted(right)):
    distance += abs(l - r)

print(distance)
    
similarity = 0
rfreq = Counter(right)
for x in left:
    similarity += x * rfreq[x]

print(similarity)
    
