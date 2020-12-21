import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC


def parse_input(data):
    all_lines = list()
    for line in data:
        temp = line.split("(contains")
        if len(temp) > 1:
            ingred = temp[0].split()
            allegens = temp[1][:-1].replace(",", "").split()
            lines = {"ingred": ingred, "allegens": allegens}
            all_lines.append(lines)
    return all_lines


def part1():
    all_allegens_temp = []
    all_ingred_temp = []
    for x in ingred_list:
        all_allegens_temp += x["allegens"]
        all_ingred_temp += x["ingred"]
    all_allegens = set(all_allegens_temp)
    all_ingred = set(all_ingred_temp)
    print(all_allegens)
    print(all_ingred)


def part2():
    pass


a = AOC(21, test=True)
data = a.read_lines()
ingred_list = parse_input(data)
part1()