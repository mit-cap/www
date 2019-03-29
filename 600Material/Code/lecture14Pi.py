import random as rr
import pylab


pylab.figure("Pi")
n = 1000
count = 0
for t in xrange(0, n):
    x = rr.random()
    y = rr.random()
    if x*x + y*y < 1.0:
        pylab.plot([x], [y], 'ro')
        count += 1
    else:
        pylab.plot([x], [y], 'go')

print 4* (float(count) / n)


pylab.figure("Pi det")
N=20
NC=0.0
x=-1.0
for i in xrange(2*N):
    y=-1.0
    for j in xrange(2*N):
        if x*x+y*y<1:
            pylab.plot([x], [y], 'ro')
            NC=NC+1
        else:
            pylab.plot([x], [y], 'go')
        y=y+1.0/N
    x=x+1.0/N    
print NC/(N*N)

pylab.show()
