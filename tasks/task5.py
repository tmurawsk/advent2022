from tasks.base import Task


class Task5(Task):
    def __init__(self, filename="input/5.txt"):
        super().__init__(filename)

    def run1(self):
        reading_stacks = True
        stacks: list[list] = list()
        for line in self.file:
            line = line.strip('\n')
            if len(line) < 2:
                reading_stacks = False
                for stack in stacks:
                    stack.reverse()
                continue

            if reading_stacks:
                stacks_cnt = int((len(line)+1)/4)
                if len(stacks) < stacks_cnt:
                    for _ in range(stacks_cnt - len(stacks)):
                        stacks.append(list())
                for i in range(1, len(line), 4):
                    if line[i] != ' ':
                        stacks[int(i/4)].append(line[i])
            else:
                [cnt, source, target] = list(map(int, line.split(' ')[1::2]))
                for _ in range(cnt):
                    stacks[target-1].append(stacks[source-1].pop())
        result = ''.join([stack.pop() for stack in stacks])
        print(result)

    def run2(self):
        reading_stacks = True
        stacks: list[list] = list()
        for line in self.file:
            line = line.strip('\n')
            if len(line) < 2:
                reading_stacks = False
                for stack in stacks:
                    stack.reverse()
                continue

            if reading_stacks:
                stacks_cnt = int((len(line)+1)/4)
                if len(stacks) < stacks_cnt:
                    for _ in range(stacks_cnt - len(stacks)):
                        stacks.append(list())
                for i in range(1, len(line), 4):
                    if line[i] != ' ':
                        stacks[int(i/4)].append(line[i])
            else:
                [cnt, source, target] = list(map(int, line.split(' ')[1::2]))
                to_move = [stacks[source-1].pop() for _ in range(cnt)]
                to_move.reverse()
                stacks[target-1].extend(to_move)
        result = ''.join([stack.pop() for stack in stacks])
        print(result)
