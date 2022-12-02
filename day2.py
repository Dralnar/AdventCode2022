import re

filepath = "inputs/day2.input"

with open(filepath, "r") as f:
    lines = f.readlines()
# part 1 total
total_score = 0
# part 2 total
total_score2 = 0
strat_re = r'(\w) (\w)'
for line in lines:
    m = re.match(strat_re, line)
    if m:
        opponent = m.group(1)
        player = m.group(2)

        if opponent == "A":
            if player == "X":
                # Rock - Rock
                total_score += 1 + 3
                # Rock - Loose -> Scissors
                total_score2 += 3 + 0
            elif player == "Y":
                # Rock - Paper
                total_score += 2 + 6
                # Rock - Draw -> Rock
                total_score2 += 1 + 3
            elif player == "Z":
                # Rock - Scissors
                total_score += 3 + 0
                # Rock - Win -> Paper
                total_score2 += 2 + 6
        elif opponent == "B":
            if player == "X":
                # Paper - Rock
                total_score += 1 + 0
                # Paper - Loose -> Rock
                total_score2 += 1 + 0
            elif player == "Y":
                # Paper - Paper
                total_score += 2 + 3
                # Paper - Draw -> Paper
                total_score2 += 2 + 3
            elif player == "Z":
                # Paper - Scissors
                total_score += 3 + 6
                # Paper - Win -> Scissors
                total_score2 += 3 + 6
        elif opponent == "C":
            if player == "X":
                # Scissors - Rock
                total_score += 1 + 6
                # Scissors - Loose -> Paper
                total_score2 += 2 + 0
            elif player == "Y":
                # Scissors - Paper
                total_score += 2 + 0
                # Scissors - Draw -> Scissors
                total_score2 += 3 + 3
            elif player == "Z":
                # Scissors - Scissors
                total_score += 3 + 3
                # Scissors - Win -> Rock
                total_score2 += 1 + 6

print(total_score)
print(total_score2)
