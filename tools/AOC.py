from genericpath import exists
import requests
from os import path

# Login in to Advent of Code and get the session cookie. Cookies last one month, so will need to reset
SESSION_ID = "53616c7465645f5fec0de59dcb22942549edaa80deb4498cf25b1fb94b7ad561b377e004e238d17e029fa98ded4ccfa0"
YEAR = 2020


class AOC:
    def __init__(self, day, test=True):
        self.day = int(day)
        self.test_file = test
        if self.test_file:
            self.input_file = f"Day{self.day}/Day{self.day}-Input-Test.txt"
            print(f"Using test data from existing input file")
            if not path.exists(self.input_file):
                raise FileNotFoundError("Test Input File does not exist")
        else:
            self.input_file = f"Day{self.day}/Day{self.day}-Input.txt"
            self._pull_input_data_from_aoc()

    def _read_file(self):
        with open(self.input_file, "r") as f:
            lines = f.read().splitlines()
        return lines

    def _pull_input_data_from_aoc(self):
        if not path.exists(self.input_file):
            print(f"Pulling Input from AOC Website for Day: {self.day}")
            aoc_input_url = f"https://adventofcode.com/{YEAR}/day/{self.day}/input"
            cookies = dict(session=SESSION_ID)
            response = requests.get(url=aoc_input_url, cookies=cookies)
            txt = response.text
            with open(self.input_file, "w") as f:
                f.write(txt)
        elif self.test_file:
            print(f"Using test input file for Day {self.day}")
        else:
            print(f"Using existing input file for Day {self.day}")

    def read_int(self):
        array = [int(x) for x in self._read_file()]
        return array

    def read_lines(self):
        array = [x.strip() for x in self._read_file()]
        return array


def main():
    a = AOC(10, True)
    test = a.read_int()
    print(test)


if __name__ == "__main__":
    main()