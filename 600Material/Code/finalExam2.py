import random
PROB_OF_ACNE = 0.31

def expectedResult():
    for color in xrange(0, 20):
        withAcne = 0
        for person in xrange(0, 100):
            if random.random() < PROB_OF_ACNE:
                withAcne += 1
        if withAcne >= 42:
            return True
    return False


def monteCarloTest(N):
    good = 0.0
    for x in xrange(0, N):
        if(expectedResult()):
            good += 1.0
    return good / N

print 'Probability of getting the result = ' + str(monteCarloTest(1000))
