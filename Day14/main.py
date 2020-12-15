import sys
import re
from itertools import permutations, combinations, combinations_with_replacement, product

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC


def parse_input(lines):
    cmds = list()
    for line in lines:
        cmd, value = line.split(" = ")
        if cmd[:3] == "mem":
            cmd, mem = cmd[:3], cmd.split("[")[1][:-1]
            cmds.append([cmd, int(mem), int(value)])
        else:
            cmds.append([cmd, value])
    return cmds


def mask_num_part1(mask, num) -> list:
    num_bin = f"{num:-036b}"
    new_num = ""
    for i in range(len(num_bin)):
        if mask[i] == "X":
            new_num += num_bin[i]
        else:
            new_num += mask[i]
    return int(new_num, 2)


def part1():
    memory = {}
    mask = ""
    for cmd in cmds:
        if cmd[0] == "mask":
            mask = cmd[1]
        else:
            mem, value = cmd[1], cmd[2]
            memory[mem] = mask_num_part1(mask, value)
    print(sum(memory.values()))


def mask_num_part2(mask, mem) -> int:
    def flatten(T):
        if type(T) != tuple:
            return (T,)
        elif len(T) == 0:
            return ()
        else:
            return flatten(T[0]) + flatten(T[1:])

    def replace_x(bin_num):
        all_numbers = list()
        xs_found = list()
        for i in range(len(bin_num)):
            if bin_num[i] == "X":
                xs_found.append(i)

        subs = [0, 1]
        for i in range(len(xs_found) - 1):
            subs = product(subs, [0, 1])
            subs = [flatten(i) for i in subs]

        for sub in subs:
            new_num = bin_num
            for i in range(len(xs_found)):
                new_num = (
                    new_num[0 : xs_found[i]] + f"{sub[i]}" + new_num[xs_found[i] + 1 :]
                )
            all_numbers.append(new_num)

        return all_numbers

    num_bin = f"{mem:-036b}"
    new_mem = ""
    add_array = list()
    for i in range(len(num_bin)):
        if mask[i] == "X":
            new_mem += "X"
        elif mask[i] == "1":
            new_mem += "1"
        else:
            new_mem += num_bin[i]

    add_array = replace_x(new_mem)
    return add_array


def part2():
    memory = {}
    for cmd in cmds:
        if cmd[0] == "mask":
            mask = cmd[1]
        else:
            mem, value = cmd[1], cmd[2]
            mem_values = mask_num_part2(mask, mem)
            for mem_value in mem_values:
                memory[int(mem_value, 2)] = value
    print(sum(memory.values()))
    return


a = AOC(14, test=False)
cmds = parse_input(a.read_lines())
part1()
part2()
