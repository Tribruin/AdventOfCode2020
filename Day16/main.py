import sys
from copy import deepcopy

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC

valid_tickets = []


def parse_input(data):
    ticket_rules = {}
    my_ticket = []
    other_tickets = []

    i = 0
    while True:
        if data[i] == "":
            break
        rule_name, rules = data[i].split(": ")
        rules = rules.split(" or ")
        rule1 = [int(x) for x in rules[0].split("-")]
        rule2 = [int(x) for x in rules[1].split("-")]
        ticket_rules[rule_name] = [rule1, rule2]
        i += 1

    data = data[i + 2 :]
    my_ticket = [int(x) for x in data[0].split(",")]

    data = data[3:]
    for line in data:
        ticket = [int(x) for x in line.split(",")]
        other_tickets.append(ticket)

    return ticket_rules, my_ticket, other_tickets


def check_ticket(ticket):
    bad_values = list()
    rule_range = ticket_rules.values()
    for value in ticket:
        valid = False
        for range in rule_range:
            min1, max1, min2, max2 = range[0][0], range[0][1], range[1][0], range[1][1]
            if min1 <= value <= max1 or min2 <= value <= max2:
                valid = True
                break
        if not valid:
            bad_values.append(value)
    return bad_values


def part1():
    bad_values = list()
    global valid_tickets
    # valid_tickets = list()
    for ticket in other_tickets:
        new_bad_values = check_ticket(ticket)
        bad_values += new_bad_values
        if len(new_bad_values) == 0:
            valid_tickets.append(ticket)
    print(sum(bad_values))
    return


def part2():
    pass


a = AOC(16, test=False)
data = a.read_lines()
ticket_rules, my_ticket, other_tickets = parse_input(data)
part1()
part2()