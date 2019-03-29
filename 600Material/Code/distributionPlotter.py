import random as rr
import pylab as pl

def uniform(a, b):
    return rr.random()*(b-a)+a


def gaussian(a, b):
    t = 0.0
    for x in xrange(100):
        t += rr.random()*b + a - 0.5*b
    return t / 100


def exponential(p):
    t = 0.0
    while(rr.random() < p):
        t += 1.0
    return t



def plotDistr(name, d, n):
    x = []
    pl.figure(name)
    for i in xrange(0,n):
        x.append(d())    
    pl.hist(x, bins=15)
    


plotDistr('uniform', lambda : uniform(5, 10), 10000)
pl.xlim((0, 20))

plotDistr('gaussian', lambda : gaussian(5, 10), 10000)

plotDistr('exponential', lambda : exponential(0.5), 10000)
# pl.xlim((0, 10))



    
pl.show()
