def part1(filename: str):
    file = open(filename, 'r')
    calories = 0
    max_calories = 0
    for line in file:
        line = line.strip()
        if len(line) < 1:
            max_calories = max(max_calories, calories)
            calories = 0
            continue
        calories += int(line)
    print(max_calories)
    file.close()


def part2(filename: str):
    file = open(filename, 'r')
    calories = 0
    max_calories = [0, 0, 0]
    for line in file:
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
    file.close()
