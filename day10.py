import re
import numpy as np

def update_cycle_strength(r, c):
    if c%40 == 20:
        return r*c
    else:
        return 0


def update_screen(r, c, s):
    c -= 1
    row = c // 40
    col = c % 40
    # if col == r-1 or col == r or col == r+1:
    if col in range(r-1, r+2):
        s[row][col] = "#"
    else:
        s[row][col] = "."
    return s


filepath = "inputs/day10.input"

with open(filepath, 'r') as f:
    lines = f.readlines()

noop_re = r'noop'
add_re = r'addx (-?\d+)'

register = 1
cycle = 1
signal_strengths_sum = 0
screen = np.full((6, 40), "")
current_line = 0

for line in lines:
    if re.match(noop_re, line):
        # begin cycle
        screen = update_screen(register, cycle, screen)
        signal_strengths_sum += update_cycle_strength(register, cycle)
        # end cycle
        cycle += 1 # next cycle
    else:
        m = re.match(add_re, line)
        if m:
            # begin cycle
            screen = update_screen(register, cycle, screen)
            signal_strengths_sum += update_cycle_strength(register, cycle)
            # end cycle
            cycle += 1 # next_cycle
            # begin cycle
            screen = update_screen(register, cycle, screen)
            signal_strengths_sum += update_cycle_strength(register, cycle)
            # end cycle
            register += int(m.group(1)) # end cycle update register
            cycle += 1 # next cycle

print(signal_strengths_sum)
print('\n'.join([''.join([str(cell) for cell in row]) for row in screen]))
