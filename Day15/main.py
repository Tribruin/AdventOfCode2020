import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC


def find_last(array, check):
    for n, i in enumerate(array[::-1]):
        if i == check:
            return n


def play_game(count):
    words_spoke = input.split(",")
    for i in range(len(words_spoke), count):
        if (i % 1000) == 0:
            print(i)
        last_word = words_spoke[-1]
        if last_word not in words_spoke[:-1]:
            words_spoke.append("0")
        else:
            last_spoken = find_last(words_spoke[:-1], words_spoke[-1])
            words_spoke.append(str(last_spoken + 1))
    print(words_spoke[-1])


def play_game_alt(count):
    last_position = dict()
    words_spoken = input.split(",")
    for n, i in enumerate(words_spoken[:-1]):
        last_position[int(i)] = (0, n)
    last_spoken = int(words_spoken[-1])
    for i in range(len(words_spoken) - 1, count):
        last_pos = last_position.get(last_spoken, None)
        if last_pos == None:
            last_position[last_spoken] = (0, i)
            x, y = last_position[0]
            last_position[0] = (y, i + 1)
            last_spoken = 0
            words_spoken.append(str(last_spoken))
        else:
            x, y = last_pos
            diff = y - x
            last_position[diff] = (y, i + 1)
            last_spoken = diff
            words_spoken.append(str(last_spoken))

    # for i in range(len(words_spoken), count):

    # last_word = words_spoke[-1]
    # if last_word not in words_spoke[:-1]:
    #     words_spoke.append("0")
    #     previous_postion = last_position["0"]
    #     last_position["0"] = i
    # else:
    #     last_spoken = i - previous_postion - 1
    #     words_spoke.append(str(last_spoken))
    #     previous_postion = last_position[last_word]
    #     last_position[str(last_spoken)] = i
    print(words_spoken[-1])


# a = AOC({{INT}}), test=True)
input = "0,3,6"
# input = "9,19,1,6,0,5,4"
play_game_alt(2020)
# play_game(30000000)
