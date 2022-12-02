filepath = "inputs/day1.input"
calories = []
with open(filepath, "r") as f:
    f_list = f.readlines()
    total = 0
    for line in f_list:
        if line == "\n":
            calories.append(total)
            total = 0
        else:
            total += int(line)


# part 1
print(max(calories))

# part 2
total_top_three = 0
for x in range(3):
    total_top_three += max(calories)
    calories.remove(max(calories))

print(total_top_three)
