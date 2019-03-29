import random as rr

rr.seed(55)
n = 5000000
count = 0
for t in xrange(0,n):
    x = rr.random()
    y = rr.random()
    if x*x + y*y < 1.0:
        count += 1

print 4* (float(count) / n)


N=1000
NC=0.0
x=-1.0
for i in xrange(2*N):
    y=-1.0
    for j in xrange(2*N):
        if x*x+y*y<1:
            NC=NC+1
        y=y+1.0/N
    x=x+1.0/N    
print NC/(N*N)
