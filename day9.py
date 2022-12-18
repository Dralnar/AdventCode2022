import numpy as np


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_down(hpos: Position, tpos: Position, loc_map):
    loc_map[hpos.x, hpos.y] = 0
    hpos.x += 1
    loc_map[hpos.x, hpos.y] = -1
    if hpos.y == tpos.y:
        if abs(hpos.x - tpos.x) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.x += 1
            loc_map[tpos.x, tpos.y] = 2
    else:
        if abs(hpos.x - tpos.x) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.x += 1
            tpos.y = hpos.y
            loc_map[tpos.x, tpos.y] = 2
    return hpos, tpos, loc_map


def move_up(hpos: Position, tpos: Position, loc_map):
    loc_map[hpos.x, hpos.y] = 0
    hpos.x -= 1
    loc_map[hpos.x, hpos.y] = -1
    if hpos.y == tpos.y:
        if abs(hpos.x - tpos.x) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.x -= 1
            loc_map[tpos.x, tpos.y] = 2
    else:
        if abs(hpos.x - tpos.x) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.x -= 1
            tpos.y = hpos.y
            loc_map[tpos.x, tpos.y] = 2
    return hpos, tpos, loc_map


def move_left(hpos: Position, tpos: Position, loc_map):
    loc_map[hpos.x, hpos.y] = 0
    hpos.y -= 1
    loc_map[hpos.x, hpos.y] = -1
    if hpos.x == tpos.x:
        if abs(hpos.y - tpos.y) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.y -= 1
            loc_map[tpos.x, tpos.y] = 2
    else:
        if abs(hpos.y - tpos.y) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.y -= 1
            tpos.x = hpos.x
            loc_map[tpos.x, tpos.y] = 2
    return hpos, tpos, loc_map


def move_right(hpos: Position, tpos: Position, loc_map):
    loc_map[hpos.x, hpos.y] = 0
    hpos.y += 1
    loc_map[hpos.x, hpos.y] = -1
    if hpos.x == tpos.x:
        if abs(hpos.y - tpos.y) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.y += 1
            loc_map[tpos.x, tpos.y] = 2
    else:
        if abs(hpos.y - tpos.y) > 1:
            loc_map[tpos.x, tpos.y] = 1
            tpos.y += 1
            tpos.x = hpos.x
            loc_map[tpos.x, tpos.y] = 2
    return hpos, tpos, loc_map


filepath = "inputs/day9.input"
command_re = r'([RULD]) (\d)'
lines = np.fromregex(file=filepath, regexp=command_re, dtype=[('dir', 'S3'), ('step', int)])
dim_map = int(np.sum([x['step'] for x in lines]) + 1)
# dim_map = 200
location_map = np.zeros((2*dim_map + 1, 2*dim_map + 1), dtype=int)
# set starting point
head_pos = Position(dim_map, dim_map)
tail_pos = Position(dim_map, dim_map)

location_map[tail_pos.x, tail_pos.y] = 1

for command in lines:
    direction = command['dir'].decode("utf-8")
    if direction == 'R':
        for n in range(command['step']):
            head_pos, tail_pos, location_map = move_right(head_pos, tail_pos, location_map)
    elif direction == 'L':
        for n in range(command['step']):
            head_pos, tail_pos, location_map = move_left(head_pos, tail_pos, location_map)
    elif direction == 'U':
        for n in range(command['step']):
            head_pos, tail_pos, location_map = move_up(head_pos, tail_pos, location_map)
    elif direction == 'D':
        for n in range(command['step']):
            head_pos, tail_pos, location_map = move_down(head_pos, tail_pos, location_map)

print(np.sum(location_map))
