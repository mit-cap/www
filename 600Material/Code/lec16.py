

import random as rr
import pylab as pl

def uniform(a, b):
    return rr.random()*(b-a)+a



def expon(p): # probability that I stop.
    t = 0.0;
    while( rr.random() > p ):
        t += 1.0
    return t



def plotDistr(name, d, n):
    x = []
    pl.figure(name)
    for i in xrange(0,n):
        x.append(d())    
    pl.hist(x, bins=15)



plotDistr('uniform', lambda : uniform(5, 10), 100)


plotDistr('exponential', lambda : expon(.1), 100)


pl.show()
