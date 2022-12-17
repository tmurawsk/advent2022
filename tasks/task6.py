import queue

from tasks.base import Task


class Task6(Task):
    def __init__(self, filename="input/6.txt"):
        super().__init__(filename)

    def run1(self):
        line = self.file.readline().strip()
        marker = list()
        cnt = 0
        for c in line:
            cnt += 1
            marker.append(c)
            if len(marker) <= 3:
                continue
            if len(marker) > 4:
                marker = marker[1:]
            if len(set(marker)) == 4:
                break
        print(cnt)

    def run2(self):
        line = self.file.readline().strip()
        marker = list()
        cnt = 0
        for c in line:
            cnt += 1
            marker.append(c)
            if len(marker) <= 13:
                continue
            if len(marker) > 14:
                marker = marker[1:]
            if len(set(marker)) == 14:
                break
        print(cnt)
