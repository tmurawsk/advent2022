from tasks.base import Task


def get_num(c: str) -> int:
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27


class Task3(Task):
    def __init__(self, filename="input/3.txt"):
        super().__init__(filename)

    def run1(self):
        sum_num = 0
        for line in self.file:
            line = line.strip()
            ln = len(line)
            parts = [line[0:int(ln/2)], line[int(ln/2):ln]]
            sum_num += get_num(set(parts[0]).intersection(set(parts[1])).pop())
        print(sum_num)

    def run2(self):
        sum_num = 0
        it = 0
        common = set()
        for line in self.file:
            it += 1
            line = line.strip()
            if len(common) == 0:
                common = set(line)
                continue
            common = common.intersection(set(line))
            if it == 3:
                it = 0
                sum_num += get_num(common.pop())
        print(sum_num)
