import re

import numpy as np

filepath = "inputs/day4.input"

with open(filepath, "r") as f:
    lines = f.readlines()

count_contained_pairs = 0
count_overlapping_pairs = 0
for line in lines:
    m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)
    if m:
        if (int(m.group(1)) <= int(m.group(3)) and int(m.group(2)) >= int(m.group(4))) or (int(m.group(1)) >= int(m.group(3)) and int(m.group(2)) <= int(m.group(4))):
            count_contained_pairs += 1
        if int(m.group(1)) in range(int(m.group(3)), int(m.group(4))+1) \
                or int(m.group(2)) in range(int(m.group(3)), int(m.group(4))+1) \
                or int(m.group(3)) in range(int(m.group(1)), int(m.group(2))+1)\
                or int(m.group(4)) in range(int(m.group(1)), int(m.group(2))+1):
            count_overlapping_pairs += 1
    else:
        print(line)

print(count_contained_pairs)
print(count_overlapping_pairs)
