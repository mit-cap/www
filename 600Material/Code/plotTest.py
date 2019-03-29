import random as rr

import pylab


def simplePlot():
    pylab.figure(1)
    pylab.plot([1,2,3,4], [1,7,3,5])
    pylab.show()



def printPi():
    n = 5000
    count = 0
    for t in xrange(0,n):
        x = rr.random()
        y = rr.random()
        if x*x + y*y < 1.0:
            pylab.plot([x], [y], 'ro')
            count += 1
        else:
            pylab.plot([x], [y], 'go')

    print 4* (float(count) / n)


pylab.figure("fig1")
pylab.plot([1,2,3], [2,1,1])
#pylab.show()

pylab.figure("fig2")
pylab.plot([1,2,3], [2,1,5])

pylab.figure("fig3")
pylab.plot([1,1.5,3, 9.5])
pylab.title('Very cool graph', fontsize='xx-large')

pylab.figure("Pi")
printPi()
pylab.show()

