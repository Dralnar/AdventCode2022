import re


class CargoStack:
    def __init__(self):
        self.stack = list()

    def add_first(self, element):
        self.stack.insert(0, element)

    def add_last(self, element):
        self.stack.append(element)

    def get_first(self):
        return self.stack[0]

    def remove_first(self):
        return self.stack.pop(0)

    def remove_last(self):
        return self.stack.pop()

    def remove_many(self, n):
        return [self.stack.pop(0) for x in range(n)]

    def add_many(self, elements: list):
        elements.reverse()
        for element in elements:
            self.add_first(element)


filepath = "inputs/day5.input"
with open(filepath, "r") as f:
    lines = f.readlines()

cargo_separation = 0
for line in lines:
    if line == "" or line.isspace():
        break
    cargo_separation += 1

cargo_nums = [int(x) for x in lines[cargo_separation-1] if x != " " and x != "\n"]
total_stacks = max(cargo_nums)
# part 1 cargo
cargo = {}
# part 2 cargo
cargo2 = {}
for i in range(total_stacks):
    cargo[i] = CargoStack()
    cargo2[i] = CargoStack()

stack_re = r'( {3}|\[\w\]) ?'
for i in range(cargo_separation-1):
    ms = re.findall(stack_re, lines[i])
    for j in range(len(ms)):
        if not ms[j].isspace():
            elmt = ms[j].replace("[", "").replace("]", "")
            cargo[j].add_last(elmt)
            cargo2[j].add_last(elmt)

command_re = r'move (\d+) from (\d+) to (\d+)'
for line in lines[cargo_separation:]:
    m = re.match(command_re, line)
    if m:
        total_moves = int(m.group(1))
        stack1 = int(m.group(2))-1
        stack2 = int(m.group(3))-1

        for i in range(total_moves):
            if len(cargo[stack1].stack) != 0:
                cargo[stack2].add_first(cargo[stack1].remove_first())

        cargo2[stack2].add_many(cargo2[stack1].remove_many(total_moves))

final_message = ""
final_message2 = ""
for i in range(total_stacks):
    final_message += cargo[i].get_first()
    final_message2 += cargo2[i].get_first()

print(final_message)
print(final_message2)
