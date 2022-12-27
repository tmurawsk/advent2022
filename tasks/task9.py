from tasks.base import Task

is_debug = False


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return self.x * 1000000 + self.y

    def is_same_axis(self, other: "Point"):
        return self.x == other.x or self.y == other.y

    def is_sticking(self, other: "Point"):
        return abs(self.x - other.x) + abs(self.y - other.y) <= 1 \
            or abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1

    def get_other_quarter(self, other: "Point"):
        if other.x > self.x:
            if other.y > self.y:
                return 1
            return 4
        else:
            if other.y > self.y:
                return 2
            return 3


class Rope:
    def __init__(self, head: Point = None):
        self.head: Point = Point() if head is None else head
        self.tail: Point = Point()
        self.visited: {int: set[int]} = {}
        self.x_range = [-5, 5]
        self.y_range = [-5, 5]

    def __str__(self):
        return f'{self.head} -> {self.tail}'

    def print(self):
        if not is_debug:
            return
        print('')
        for y in range(self.y_range[1], self.y_range[0]+1, -1):
            line = ''
            for x in range(self.x_range[0], self.x_range[1]+1, 1):
                if (x, y) == (self.head.x, self.head.y):
                    line += 'H'
                elif (x, y) == (self.tail.x, self.tail.y):
                    line += 'T'
                elif (x, y) == (0, 0):
                    line += 'O'
                elif x in self.visited.keys() and y in self.visited[x]:
                    line += '#'
                else:
                    line += '.'
            print(line)

    def visit(self):
        if self.tail.x not in self.visited:
            self.visited[self.tail.x] = set()
        self.visited[self.tail.x].add(self.tail.y)

    def move_tail(self) -> bool:
        if self.head.is_sticking(self.tail):
            return False
        if self.head.is_same_axis(self.tail):
            dir_step = 1 if self.head.x > self.tail.x or self.head.y > self.tail.y else -1
            if self.head.x != self.tail.x:
                self.tail.x += dir_step
            else:
                self.tail.y += dir_step
            self.visit()
            return True
        quarter = self.head.get_other_quarter(self.tail)
        if quarter == 1:
            self.tail.x -= 1
            self.tail.y -= 1
        elif quarter == 2:
            self.tail.x += 1
            self.tail.y -= 1
        elif quarter == 3:
            self.tail.x += 1
            self.tail.y += 1
        else:
            self.tail.x -= 1
            self.tail.y += 1
        self.visit()
        return True

    def move(self, dir: str, dir_step: int, is_debug: bool = False):
        if dir in ['L', 'R']:
            self.head.x += dir_step
        else:
            self.head.y += dir_step
        self.x_range[0] = min(self.x_range[0], self.head.x-1)
        self.x_range[1] = max(self.x_range[1], self.head.x+1)
        self.y_range[0] = min(self.y_range[0], self.head.y-1)
        self.y_range[1] = max(self.y_range[1], self.head.y+1)
        self.print()
        self.move_tail()


class Task9(Task):
    def __init__(self, filename="input/9.txt"):
        super().__init__(filename)

    def run1(self):
        rope = Rope()
        for line in self.file:
            line = line.strip()
            [dir, step] = line.split(' ')
            dir_step = 1 if dir in ['R', 'U'] else -1
            for _ in range(int(step)):
                rope.move(dir, dir_step, False)
        count = sum([len(s) for s in rope.visited.values()])
        print(count)

    @staticmethod
    def print_ropes(knots: [Rope], x_range: [int], y_range: [int]):
        if not is_debug:
            return
        print('')
        current_points: {int: {int}} = {}
        for knot in knots[1:]:
            if knot.head.x not in current_points:
                current_points[knot.head.x] = set()
            current_points[knot.head.x].add(knot.head.y)
        for y in range(y_range[1], y_range[0]-1, -1):
            line = ''
            for x in range(x_range[0], x_range[1]+1, 1):
                p = Point(x, y)
                if p == knots[0].head:
                    line += 'H'
                elif p == knots[8].tail:
                    line += 'T'
                elif x in current_points and y in current_points[x]:
                    for i in range(1, 9):
                        if p == knots[i].head:
                            line += str(i)
                            continue
                elif (x, y) == (0, 0):
                    line += 'O'
                elif x in knots[8].visited.keys() and y in knots[8].visited[x]:
                    line += '#'
                else:
                    line += '.'
            print(line)

    def run2(self):
        x_range = [-5, 5]
        y_range = [-5, 5]
        knots = [Rope()]
        for i in range(8):
            knots.append(Rope(knots[i].tail))
        for line in self.file:
            line = line.strip()
            [dir, step] = line.split(' ')
            dir_step = 1 if dir in ['R', 'U'] else -1
            for _ in range(int(step)):
                knots[0].move(dir, dir_step)
                x_range = [min(x_range[0], knots[0].head.x-1), max(x_range[1], knots[0].head.x+1)]
                y_range = [min(y_range[0], knots[0].head.y-1), max(y_range[1], knots[0].head.y+1)]
                self.print_ropes(knots, x_range, y_range)
                for i in range(1, 9):
                    if knots[i].move_tail():
                        self.print_ropes(knots, x_range, y_range)
        count = sum([len(s) for s in knots[8].visited.values()])
        print(count+1)
