from random import randint

d = int(input("droprate: "))
i = int(input("iterations: "))
t = 0

def calcTries(x):
    global d, t, i
    while True:
        r = randint(1, d)
        if r == d:
            print("iteration: " + str(x) + ", tries: " + str(t + 1))
            t = 0
            break
        else:
            t += 1

for x in range(1, i + 1):
    calcTries(x)