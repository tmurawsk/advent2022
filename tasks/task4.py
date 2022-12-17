from tasks.base import Task


class Range:
    def __init__(self, pair: str):
        [self.start, self.end] = list(map(int, pair.split('-')))

    def __gt__(self, other):
        return self.start < other.start or self.start == other.start and self.end >= other.end

    def overlaps_fully(self, other):
        first = self if self > other else other
        second = other if self > other else self
        return first.start <= second.start <= first.end and first.start <= second.end <= first.end

    def overlaps(self, other):
        first = self if self > other else other
        second = other if self > other else self
        return first.start <= second.start <= first.end


class Task4(Task):
    def __init__(self, filename="input/4.txt"):
        super().__init__(filename)

    def run1(self):
        cnt = 0
        for line in self.file:
            [part1, part2] = line.strip().split(',')
            if Range(part1).overlaps_fully(Range(part2)):
                cnt += 1
        print(cnt)

    def run2(self):
        cnt = 0
        for line in self.file:
            [part1, part2] = line.strip().split(',')
            if Range(part1).overlaps(Range(part2)):
                cnt += 1
        print(cnt)
