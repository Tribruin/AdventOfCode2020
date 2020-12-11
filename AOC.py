class AOC:
    def __init__(self, day, test=True):
        self.day = day
        self.test_file = test
        self.input_file = f"Day{self.day}-Input.txt"
        self.input_test_file = f"Day{self.day}-Input-Test.txt"

    def _read_file(self):
        if self.test_file:
            file = self.input_test_file
        else:
            file = self.input_file

        with open(file, "r") as f:
            lines = f.read().splitlines()

        return lines

    def read_int(self):
        array = [int(x) for x in self._read_file()]
        return array


def main():
    a = AOC(10, True)
    test = a.read_int()
    print(test)


if __name__ == "__main__":
    main()