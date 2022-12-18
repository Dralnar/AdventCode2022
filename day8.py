import numpy as np

filepath = "inputs/day8.input"
forest = np.genfromtxt(filepath, int, delimiter=1)

# part 1
visible_trees = 4 * (forest.shape[0] - 1)
# part 2
total_score = 0

for i in range(1, forest.shape[0] - 1):
    for j in range(1, forest.shape[0] - 1):
        tree_size = forest[i, j]
        if max(forest[i, :j]) < tree_size or max(forest[i, j+1:]) < tree_size or max(forest[:i, j]) < tree_size or max(forest[i+1:, j]) < tree_size:
            visible_trees += 1

        # trees on the left
        left_trees = forest[i, :j]
        left_score = 0
        for n in range(len(left_trees)):
            if left_trees[-n-1] < tree_size:
                left_score += 1
            if left_trees[-n-1] >= tree_size:
                left_score += 1
                break

        # trees on the right
        right_trees = forest[i, j+1:]
        right_score = 0
        for n in range(len(right_trees)):
            if right_trees[n] < tree_size:
                right_score += 1
            elif right_trees[n] >= tree_size:
                right_score += 1
                break

        # trees on the top
        top_trees = forest[:i, j]
        top_score = 0
        for n in range(len(top_trees)):
            if top_trees[-n-1] < tree_size:
                top_score += 1
            elif top_trees[-n-1] >= tree_size:
                top_score += 1
                break

        # trees on the bottom
        bottom_trees = forest[i+1:, j]
        bottom_score = 0
        for n in range(len(bottom_trees)):
            if bottom_trees[n] < tree_size:
                bottom_score += 1
            elif bottom_trees[n] >= tree_size:
                bottom_score += 1
                break

        tree_score = right_score * left_score * top_score * bottom_score
        total_score = tree_score if tree_score > total_score else total_score

# part 1
print(visible_trees)
# part 2
print(total_score)
