from tasks.base import Task

NOOP = 'noop'


def check_register(cycle, reg):
    return cycle * reg if (cycle - 20) % 40 == 0 else 0


def add_pixel(image, reg):
    pixel_position = len(image) % 40
    return '#' if abs(reg - pixel_position) <= 1 else '.'


class Task10(Task):
    def __init__(self, filename="input/10.txt"):
        super().__init__(filename)

    def run1(self):
        result = 0
        cycle = 0
        reg = 1
        for line in self.file:
            cycle += 1
            result += check_register(cycle, reg)
            line = line.strip()
            if line == NOOP:
                continue
            [_, diff] = line.split()
            cycle += 1
            result += check_register(cycle, reg)
            reg += int(diff)
        print(result)

    def run2(self):
        image = ''
        reg = 1
        for line in self.file:
            line = line.strip()
            image += add_pixel(image, reg)
            if line == NOOP:
                continue
            [_, diff] = line.split()
            image += add_pixel(image, reg)
            reg += int(diff)
        for i in range(0, int(len(image)/40)):
            print(image[40*i:40*(i+1)])
