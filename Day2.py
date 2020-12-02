with open("Day2-Input.txt") as f:
    passwords_data = f.readlines()

# passwords_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

passwords = [
    {
        "min": int(i.split(":")[0].split("-")[0]),
        "max": int(i.split(":")[0].split("-")[1].split(" ")[0]),
        "letter": i.split(":")[0].split("-")[1].split(" ")[1],
        "code": i.split(":")[1].strip(" ").strip("\n"),
    }
    for i in passwords_data
]


def part1():
    valid_passwords = 0
    for password in passwords:
        # print(password, password["code"].count(password["letter"]))
        letter = password["letter"]
        min = password["min"] - 1
        max = password["max"] - 1
        code = password["code"]

        if min <= code.count(letter) <= max:
            valid_passwords += 1

    print(valid_passwords)


def part2():
    valid_passwords = 0
    for password in passwords:
        letter = password["letter"]
        first_pos = password["min"] - 1
        last_pos = password["max"] - 1
        code = password["code"]

        # This line uses ^ as Exclusive OR (XOR)
        if (code[first_pos] == letter) ^ (code[last_pos] == letter):
            valid_passwords += 1

    print(valid_passwords)


part1()
part2()