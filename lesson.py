import time
import os
import random

COUNTDOWN = 2

class Lesson():
    def __init__(self, number):
        self.number = number
        self.multi = [x for x in range(self.number, (self.number * 12) + 1, self.number)]
        self.randoms = set()
        self.fill_random()
        self.answers = []
        self.solutions = []
        self.create_problem()

    def get_number(self):
        return self.number

    def create_problem(self):
        print(f'\nHere is the {self.get_number()} times table')
        print(*(self.multi))
        time.sleep(COUNTDOWN)
        os.system('cls')
        #self.solve_problem()

    def solve_problem(self):
        pass

    def fill_random(self):
        pass


class Multiplication(Lesson):
    def fill_random(self):
        while len(self.randoms) < 5:
            self.randoms.add(random.randint(1, 12))

    def solve_problem(self):
        for num in self.randoms:
            self.solutions.append(self.number * num)
            self.answers.append((int)(input(f'{self.number} * {num} = ')))
        results = [self.solutions[i] == self.answers[i] for i in range(0, 5)]
        print(*results)
        if False in results:
            return False
        return True


class Division(Lesson):
    def fill_random(self):
        while len(self.randoms) < 5:
            rand = random.randint(self.number, (self.number * 12) + 1)
            if rand % self.number == 0:
                self.randoms.add(rand)

    def solve_problem(self):
        for num in self.randoms:
            self.solutions.append(num)
            self.answers.append((int)(input(f'{num} / {self.number} = ')))
        for i in range(0, len(self.solutions)):
            self.solutions[i] /= self.number
        results = [self.solutions[i] == self.answers[i] for i in range(0, 5)]
        print(*results)
        if False in results:
            return False
        return True