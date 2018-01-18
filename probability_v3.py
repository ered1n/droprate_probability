from random import randint

class Probability:

    def __init__(self, d, i, t):
        self.d = d
        self.i = i
        self.t = t
        self.a = []
        self.p = [[], []]

    def calcTries(self):
        for x in range(1, self.i + 1):
            while True:
                if randint(1, self.d) == self.d:
                    self.t += 1
                    print("iteration: {}, tries: {}".format(x, self.t))
                    self.a.append(self.t)
                    self.t = 0
                    break
                else:
                    self.t += 1

    def calcPercentages(self):
        for i in range(len(self.a)):
            if self.a[i] < self.d:
                self.p[0].append(self.a[i])
            elif self.a[i] > self.d:
                self.p[1].append(self.a[i])
        for j in range(len(self.p)):
            print("{} {}: {}%".format("<" if j == 0 else ">", self.d, round(float(len(self.p[j])) / len(self.a) * 100, 2)))

init = Probability(500, 10000000, 0)
init.calcTries()
init.calcPercentages()