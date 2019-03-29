import random as rr

import pylab

GOAT = 0
CAR = 1
WIN = 2
LOSE= 3

class Game:
    def putGoat(self):
        p = rr.randint(0, 2)
        x = [GOAT, GOAT, GOAT]
        x[p] = CAR
        return x
        
    def __init__(self):
        self.doors = self.putGoat()

    def nocar(self, v):
        if self.doors[ (v + 1) % 3] == GOAT:
            return (v + 1) % 3
        return (v + 2) % 3;

    def play(self, s):
        p = s.play1()        
        p = s.play2(self.nocar(p))
        if(self.doors[p] == CAR):
            return WIN
        return LOSE

class Strategy:
    def play1(self):
        pass
    def play2(self, g):
        pass

class StayStrategy(Strategy):
    def play1(self):
        self.choice = rr.randint(0, 2)
        return self.choice
    def play2(self, g):
        return self.choice

class SwitchStrategy(Strategy):
    def play1(self):
        self.choice = rr.randint(0, 2)
        return self.choice
    def play2(self, g):
        if self.choice == ((g+1)%3):
            return  (g+2)%3        
        return (g+1)%3


class RandStrategy(Strategy):
    def play1(self):
        self.choice = rr.randint(0, 2)
        return self.choice
    def play2(self, g):
        t = (g+rr.randint(1, 2))%3
        assert t != g
        return t



def monteCarlo(F, N):
    v = 0.0
    for x in xrange(0, N):
        v = v + F()
    return v / N


def play(s):
    g = Game()
    if g.play(s) == WIN:
        return 1.0
    return 0.0

rh = []
pylab.figure('Figure 30')
for x in xrange(0, 1500):
    t = monteCarlo(lambda : play(SwitchStrategy()), 30)
    rh.append(t)
pylab.hist(rh, bins=10)
pylab.figure('Figure 3000')
for x in xrange(0, 1500):
    t = monteCarlo(lambda : play(SwitchStrategy()), 3000)
    rh.append(t)
pylab.hist(rh, bins=10)
print 'done'
pylab.show()

# print "Rand strategy = " + str(monteCarlo(lambda : play(RandStrategy()), 100000))
# print "Switch strategy = " + str(monteCarlo(lambda : play(SwitchStrategy()), 100000))
# print "Stay strategy = " + str(monteCarlo(lambda : play(StayStrategy()), 100000))
