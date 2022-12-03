import re

filepath = "inputs/day3.input"

with open(filepath, "r") as f:
    lines = f.readlines()

# part 1
sum_duplicates = 0
for line in lines:
    mid = int(len(line)/2)
    comp1 = line[0:mid]
    comp2 = line[mid:len(line)]

    doublon = [x for x in comp1 if x in comp2]
    doublon = doublon[0]
    if re.match(r'[a-z]', doublon):
        sum_duplicates += ord(doublon) - 96
    elif re.match(r'[A-Z]', doublon):
        sum_duplicates += ord(doublon) - 38

print(sum_duplicates)

# part 2
sum_badges = 0
i = 1
for line in lines:
    if i%3 == 1:
        bag1 = line
    elif i%3 == 2:
        bag2 = line
    elif i%3 == 0:
        bag3 = line
        badge = [x for x in bag1 if x in [y for y in bag2 if y in bag3]][0]
        if re.match(r'[a-z]', badge):
            sum_badges += ord(badge) - 96
        elif re.match(r'[A-Z]', badge):
            sum_badges += ord(badge) - 38
    i += 1

print(sum_badges)
