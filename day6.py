import numpy as np

filepath = "inputs/day6.input"
with open(filepath, "r") as f:
    line = f.readline()

for i in range(3, len(line)):
    if np.unique([line[i-3], line[i-2], line[i-1], line[i]]).size == 4:
        print(i+1)
        break

for i in range(13, len(line)):
    if np.unique([line[i-x] for x in range(0, 14)]).size == 14:
        print(i + 1)
        break
