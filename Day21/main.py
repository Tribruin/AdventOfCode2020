import sys
from itertools import chain

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
    # Collect all allegens and ingreds and put each in to a set
    all_allegens = set([y for x in ingred_list for y in x["allegens"]])
    all_ingred = set([y for x in ingred_list for y in x["ingred"]])
    ingred_w_allegens = list()
    for allegen in all_allegens:
        possible_ingreds = all_ingred
        for line in ingred_list:
            if allegen in line["allegens"]:
                possible_ingreds = possible_ingreds.intersection(set(line["ingred"]))
        ingred_w_allegens += list(possible_ingreds)
    ingreds_wo_allegens = set(all_ingred.difference(set(ingred_w_allegens)))
    total_count = 0
    for ingred in ingreds_wo_allegens:
        for line in ingred_list:
            if ingred in line["ingred"]:
                total_count += 1
    print(total_count)
    return ingreds_wo_allegens


def part2():
    all_allegens = set([y for x in ingred_list for y in x["allegens"]])
    all_ingred = set([y for x in ingred_list for y in x["ingred"]])
    unused_ingreds = part1()
    ingred_allegen = dict()
    allegen_ingreds = all_ingred.difference(unused_ingreds)

    pass


a = AOC(21, test=True)
data = a.read_lines()
ingred_list = parse_input(data)
# part1()
part2()