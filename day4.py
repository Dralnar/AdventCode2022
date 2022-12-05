import re

filepath = "inputs/day4.input"

with open(filepath, "r") as f:
    lines = f.readlines()

count_overlapping_pairs = 0
for line in lines:
    m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)
    if m:
        if (m.group(1) <= m.group(3) and m.group(2) >= m.group(4)) or (m.group(1) >= m.group(3) and m.group(2) <= m.group(4)):
            count_overlapping_pairs += 1
    else:
        print(line)

print(count_overlapping_pairs)
