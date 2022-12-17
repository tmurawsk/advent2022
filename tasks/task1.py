from tasks.base import Task


class Task1(Task):
    def __init__(self, filename="input/1.txt"):
        super().__init__(filename)

    def run1(self):
        calories = 0
        max_calories = 0
        for line in self.file:
            line = line.strip()
            if len(line) < 1:
                max_calories = max(max_calories, calories)
                calories = 0
                continue
            calories += int(line)
        print(max_calories)

    def run2(self):
        calories = 0
        max_calories = [0, 0, 0]
        for line in self.file:
            line = line.strip()
            if len(line) < 1:
                max_calories.append(calories)
                max_calories.sort(reverse=True)
                max_calories = max_calories[:3]
                calories = 0
                continue
            calories += int(line)
        print(max_calories)
        print(sum(max_calories))
