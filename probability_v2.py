from random import randint

class Probability:

    def __init__(self, d, i, t, s):
        self.d = d
        self.i = i
        self.t = t
        self.s = s
        self.a = []
        self.z = []
        self.p = []
        self.n = self.d / self.s

    def calcTries(self):
        for x in range(1, self.i + 1):
            while True:
                r = randint(1, self.d)
                if r == self.d:
                    print("iteration: " + str(x) + ", tries: " + str(self.t + 1))
                    self.z.append(self.t + 1)
                    self.t = 0
                    break
                else:
                    self.t += 1

    def calcSplit(self):
        for x in range(0, self.s + 1):
            self.a.append([])
        for i in range(len(self.z)):
            for j in range(1, self.s + 1):
                m = int(self.n * j)
                if self.z[i] < m:
                    self.a[j - 1].append(self.z[i])
                elif self.z[i] > self.d:
                    self.a[self.s].append(self.z[i])

    def calcPercentages(self):
        for i in range(len(self.a)):
            self.p.append(len(self.a[i]) / sum(len(x) for x in self.a) * 100)
        print(self.p)

init = Probability(300, 10, 0, 7)
init.calcTries()
init.calcSplit()
print(init.a)

# init.calcPercentages()