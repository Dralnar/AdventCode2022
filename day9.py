import numpy as np


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_down(hpos: Position, tpos: Position, loc_set):
    hpos.x += 1
    if hpos.y == tpos.y:
        if abs(hpos.x - tpos.x) > 1:
            tpos.x += 1
            loc_set.add((tpos.x, tpos.y))
    else:
        if abs(hpos.x - tpos.x) > 1:
            tpos.x += 1
            tpos.y = hpos.y
            loc_set.add((tpos.x, tpos.y))
    return hpos, tpos, loc_set


def move_up(hpos: Position, tpos: Position, loc_set):
    hpos.x -= 1
    if hpos.y == tpos.y:
        if abs(hpos.x - tpos.x) > 1:
            tpos.x -= 1
            loc_set.add((tpos.x, tpos.y))
    else:
        if abs(hpos.x - tpos.x) > 1:
            tpos.x -= 1
            tpos.y = hpos.y
            loc_set.add((tpos.x, tpos.y))
    return hpos, tpos, loc_set


def move_left(hpos: Position, tpos: Position, loc_set):
    hpos.y -= 1
    if hpos.x == tpos.x:
        if abs(hpos.y - tpos.y) > 1:
            tpos.y -= 1
            loc_set.add((tpos.x, tpos.y))
    else:
        if abs(hpos.y - tpos.y) > 1:
            tpos.y -= 1
            tpos.x = hpos.x
            loc_set.add((tpos.x, tpos.y))
    return hpos, tpos, loc_set


def move_right(hpos: Position, tpos: Position, loc_set):
    hpos.y += 1
    if hpos.x == tpos.x:
        if abs(hpos.y - tpos.y) > 1:
            tpos.y += 1
            loc_set.add((tpos.x, tpos.y))
    else:
        if abs(hpos.y - tpos.y) > 1:
            tpos.y += 1
            tpos.x = hpos.x
            loc_set.add((tpos.x, tpos.y))
    return hpos, tpos, loc_set


def follow_knot(hpos: Position, tpos: Position):
    xdif = hpos.x - tpos.x
    ydif = hpos.y - tpos.y
    if xdif == 0:
        if ydif < -1:
            tpos.y -= 1
        elif ydif > 1:
            tpos.y += 1
    elif ydif == 0:
        if xdif < -1:
            tpos.x -= 1
        elif xdif > 1:
            tpos.x += 1
    elif xdif < 0 and ydif < 0 and not (xdif == -1 and ydif == -1):
        tpos.x -= 1
        tpos.y -= 1
    elif xdif < 0 < ydif and not (xdif == -1 and ydif == 1):
        tpos.x -= 1
        tpos.y += 1
    elif ydif < 0 < xdif and not (xdif == 1 and ydif == -1):
        tpos.x += 1
        tpos.y -= 1
    elif xdif > 0 and ydif > 0 and not (xdif == 1 and ydif == 1):
        tpos.x += 1
        tpos.y += 1
    return tpos


filepath = "inputs/day9.input"
command_re = r'([RULD]) (\d+)'
lines = np.fromregex(file=filepath, regexp=command_re, dtype=[('dir', 'S3'), ('step', int)])
location_set = {(0,0)}
# set starting point
head_pos = Position(0, 0)
tail_pos = Position(0, 0)

# part 1
for command in lines:
    direction = command['dir'].decode("utf-8")
    if direction == 'R':
        for n in range(command['step']):
            head_pos, tail_pos, location_set = move_right(head_pos, tail_pos, location_set)
    elif direction == 'L':
        for n in range(command['step']):
            head_pos, tail_pos, location_set = move_left(head_pos, tail_pos, location_set)
    elif direction == 'U':
        for n in range(command['step']):
            head_pos, tail_pos, location_set = move_up(head_pos, tail_pos, location_set)
    elif direction == 'D':
        for n in range(command['step']):
            head_pos, tail_pos, location_set = move_down(head_pos, tail_pos, location_set)

print(len(location_set))

# part 2
tail_location_set = {(0,0)}
knot_number = 10
knot_pos = [Position(0,0) for x in range(knot_number)]

for command in lines:
    direction = command['dir'].decode("utf-8")
    if direction == 'R':
        for n in range(command['step']):
            for i in range(knot_number-1):
                if i == 0:
                    knot_pos[i], knot_pos[i+1], loc = move_right(knot_pos[i], knot_pos[i+1], set())
                else:
                    knot_pos[i+1] = follow_knot(knot_pos[i], knot_pos[i+1])
                if i == knot_number - 2:
                    tail_location_set.add((knot_pos[i+1].x, knot_pos[i+1].y))
    elif direction == 'L':
        for n in range(command['step']):
            for i in range(knot_number-1):
                if i == 0:
                    knot_pos[i], knot_pos[i+1], loc = move_left(knot_pos[i], knot_pos[i+1], set())
                else:
                    knot_pos[i+1] = follow_knot(knot_pos[i], knot_pos[i+1])
                if i == knot_number - 2:
                    tail_location_set.add((knot_pos[i+1].x, knot_pos[i+1].y))
    elif direction == 'U':
        for n in range(command['step']):
            for i in range(knot_number-1):
                if i == 0:
                    knot_pos[i], knot_pos[i+1], loc = move_up(knot_pos[i], knot_pos[i+1], set())
                else:
                    knot_pos[i+1] = follow_knot(knot_pos[i], knot_pos[i+1])
                if i == knot_number - 2:
                    tail_location_set.add((knot_pos[i+1].x, knot_pos[i+1].y))
    elif direction == 'D':
        for n in range(command['step']):
            for i in range(knot_number-1):
                if i == 0:
                    knot_pos[i], knot_pos[i+1], loc = move_down(knot_pos[i], knot_pos[i+1], set())
                else:
                    knot_pos[i+1] = follow_knot(knot_pos[i], knot_pos[i+1])
                if i == knot_number - 2:
                    tail_location_set.add((knot_pos[i+1].x, knot_pos[i+1].y))

print(len(tail_location_set))
