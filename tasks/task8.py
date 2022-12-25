import math

from tasks.base import Task


class Task8(Task):
    def __init__(self, filename="input/8.txt"):
        super().__init__(filename)

    def run1(self):
        forest: list[list[int]] = list()
        visible: list[list[int]] = list()
        for line in self.file:
            line = line.strip()
            forest.append(list(map(int, line)))
            visible.append([0 for _ in line])
        x, y = len(forest), len(forest[0])
        for i in range(x):
            max_heights = [-1, -1]
            for j in range(y):
                visible[i][j] = 1 if forest[i][j] > max_heights[0] or visible[i][j] == 1 else 0
                max_heights[0] = max(forest[i][j], max_heights[0])
                visible[i][y-j-1] = 1 if forest[i][y-j-1] > max_heights[1] or visible[i][y-j-1] == 1 else 0
                max_heights[1] = max(forest[i][y-j-1], max_heights[1])
        for j in range(y):
            max_heights = [-1, -1]
            for i in range(x):
                visible[i][j] = 1 if forest[i][j] > max_heights[0] or visible[i][j] == 1 else 0
                max_heights[0] = max(forest[i][j], max_heights[0])
                visible[x-i-1][j] = 1 if forest[x-i-1][j] > max_heights[1] or visible[x-i-1][j] == 1 else 0
                max_heights[1] = max(forest[x-i-1][j], max_heights[1])
        result = sum([sum(row) for row in visible])
        print(result)

    def run2(self):
        max_view = 0
        forest: list[list[int]] = list()
        for line in self.file:
            line = line.strip()
            forest.append(list(map(int, line)))
        x, y = len(forest), len(forest[0])

        for i in range(1, x):
            for j in range(1, y):
                views = [1, 1, 1, 1]
                for d in range(2, x):
                    if i + d >= x or forest[i][j] <= forest[i+d-1][j]:
                        break
                    views[0] += 1
                for d in range(2, x):
                    if i - d < 0 or forest[i][j] <= forest[i-d+1][j]:
                        break
                    views[1] += 1
                for d in range(2, y):
                    if j - d < 0 or forest[i][j] <= forest[i][j-d+1]:
                        break
                    views[2] += 1
                for d in range(2, y):
                    if j + d >= y or forest[i][j] <= forest[i][j+d-1]:
                        break
                    views[3] += 1
                max_view = max(max_view, math.prod(views))
        print(max_view)
