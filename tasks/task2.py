from base import Task

choose_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

outcome_score = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
    }
}

outcome_score2 = {
    'X': {
        'A': 0 + choose_score['Z'],
        'B': 0 + choose_score['X'],
        'C': 0 + choose_score['Y']
    },
    'Y': {
        'A': 3 + choose_score['X'],
        'B': 3 + choose_score['Y'],
        'C': 3 + choose_score['Z']
    },
    'Z': {
        'A': 6 + choose_score['Y'],
        'B': 6 + choose_score['Z'],
        'C': 6 + choose_score['X']
    }
}


class Task2(Task):
    def __init__(self, filename="input/2.txt"):
        super().__init__(filename)

    def run1(self):
        score = 0
        for line in self.file:
            [opp_part, my_part] = line.strip().split(' ')
            score += choose_score[my_part]
            score += outcome_score[my_part][opp_part]
        print(score)

    def run2(self):
        score = 0
        for line in self.file:
            [opp_part, result] = line.strip().split(' ')
            score += outcome_score2[result][opp_part]
        print(score)
