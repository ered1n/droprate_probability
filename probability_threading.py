from random import randint
import threading
import time

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
            global counter
            counter += 1
            # time.sleep(0.001)
            print(counter)

    def calcPercentages(self):
        for i in range(len(self.a)):
            if self.a[i] < self.d:
                self.p[0].append(self.a[i])
            elif self.a[i] > self.d:
                self.p[1].append(self.a[i])
        for j in range(len(self.p)):
            print("{} {}: {}%".format("<" if j == 0 else ">", self.d, round(float(len(self.p[j])) / len(self.a) * 100, 2)))

if __name__ == "__main__":
    droprate = 500
    iterations = 100000
    counter = 0
    t = time.time()
    threads = 2
    threadList = []

    init = Probability(droprate, iterations / 2, 0)

    # init.calcTries()
    # init.calcTries()

    for i in range(threads):
        t = threading.Thread(target=init.calcTries())
        t.start()
        threadList.append(t)

    print("done in: ", time.time() - t)
    print("total iterations: ", counter)