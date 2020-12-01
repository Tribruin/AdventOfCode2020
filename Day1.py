RESULT = 2020

with open("Day1-Source.txt", "r") as f:
    data = f.readlines()

data_numbers = [int(x) for x in data]


def check_array_part1(array):
    for i in range(len(array) - 1):
        num_sum = array[0] + array[i + 1]
        if num_sum == RESULT:
            print("FOUND RESULT")
            return True, array[0], array[i + 1]
    return False, 0, 0


def part_1():
    for count in range(len(data_numbers) - 1):
        result, n1, n2 = check_array_part1(data_numbers[count:])
        if result:
            print(n1 * n2)
            break


def check_array_part2(array):
    for i in range(1, len(array) - 1):
        if array[0] + array[i] >= RESULT:
            pass
        else:
            for k in range(i + 1, len(array)):
                num_sum = array[0] + array[i] + array[k]
                # print(
                #     f"Checking Nums: {array[0]}, {array[i]}, {array[k]}, total={num_sum}"
                # )
                if num_sum == RESULT:
                    print("FOUND RESULT")
                    return True, array[0], array[i], array[k]
    return False, 0, 0, 0


def part_2():
    for count in range(len(data_numbers) - 2):
        result, n1, n2, n3 = check_array_part2(data_numbers[count:])
        if result:
            print(n1 * n2 * n3)
            return


part_1()
part_2()