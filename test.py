import numpy as np


class Slope:
    def __init__(self, filename) -> None:

        lines = []
        with open(file=filename) as f:
            for line in f:
                lines.append(line.strip())
        # lines = [l.strip() for l in lines]

        self.columns = len(lines[0])
        self.rows = len(lines)
        self.slope_data = np.zeros((self.rows, self.columns), dtype=bool)

        for y in range(self.rows):
            for x in range(self.columns):
                self.slope_data[y][x] = lines[y][x] == "#"
        return


slope = Slope("Day3-InputTest.txt")
print(slope)