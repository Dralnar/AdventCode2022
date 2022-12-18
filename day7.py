import re
import numpy as np


class FileStructure:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.file_list = dict()
        self.child_dir = dict()
        if parent is not None:
            self.full_path = parent.get_full_path() + "/" + name
        else:
            self.full_path = name

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_full_path(self):
        return self.full_path

    def add_file(self, file: str, size: int):
        if file not in self.file_list.keys():
            self.file_list[file] = size

    def get_file_list(self):
        return self.file_list

    def add_child(self, child):
        if child.get_name() not in self.child_dir.keys():
            self.child_dir[child.get_name()] = child

    def get_children_dir(self):
        return self.child_dir


def calculate_dirs_size(directory: FileStructure, dirs_size: dict):
    total_size = 0
    total_size += np.sum([int(x) for x in directory.get_file_list().values()])
    # for s in directory.get_file_list().values():
    #     total_size += s
    for c in directory.get_children_dir().values():
        dirs_size = calculate_dirs_size(c, dirs_size)
        total_size += int(dirs_size[c.get_full_path()])
    dirs_size[directory.get_full_path()] = total_size
    return dirs_size


filepath = "inputs/day7.input"
with open(filepath, 'r') as f:
    lines = f.readlines()

re_cd_root = r'\$ cd /'
re_cd_in = r'\$ cd (\w+)'
re_cd_out = r'\$ cd \.\.'
re_ls = r'\$ ls'
re_ls_file = r'(\d+) ([\w\.]+)'
re_ls_dir = r'dir (\w+)'

all_dir_dict = {}
root = FileStructure("root", None)
# all_dir_dict["root"] = root
current_dir = root
in_ls = False

for line in lines:
    if re.match(re_cd_root, line):
        current_dir = root
        in_ls = False
    elif re.match(re_cd_out, line):
        if current_dir != root:
            current_dir = current_dir.get_parent()
        in_ls = False
    elif re.match(re_cd_in, line):
        dir_in = re.match(re_cd_in, line).group(1)
        if dir_in in current_dir.get_children_dir().keys():
            new_current_dir = current_dir.get_children_dir()[dir_in]
        else:
            new_current_dir = FileStructure(dir_in, current_dir)
            # all_dir_dict[dir_in] = new_current_dir
            current_dir.add_child(new_current_dir)
        current_dir = new_current_dir
        in_ls = False
    elif re.match(re_ls, line):
        in_ls = True
    elif re.match(re_ls_dir, line):
        # Nothing to do ?
        pass
    elif re.match(re_ls_file, line) and in_ls:
        m = re.match(re_ls_file, line)
        file_name = m.group(2)
        file_size = int(m.group(1))
        current_dir.add_file(file_name, file_size)

full_dir_sizes = calculate_dirs_size(root, {})
size_part1 = int(np.sum([x for x in full_dir_sizes.values() if x <= 100000]))
# size_part1 = 0
# for x in full_dir_sizes.values():
#     if x <= 100000:
#         size_part1 += x
print(size_part1)

root_size = full_dir_sizes['root']
space_left = 70000000 - root_size
space_to_retrieve = 30000000 - space_left

dirs_biggest_than_space_to_retrieve = [x for x in full_dir_sizes.values() if x >= space_to_retrieve]
dir_size_to_delete = min(dirs_biggest_than_space_to_retrieve)
print(dir_size_to_delete)
