import random


C = 40

def pt():
    return ( random.random() * (C-1)+1, random.random())

N = 10000000
cnt = 0
for i in xrange(0, N):
    (x, y) = pt()    
    if( y < 1/x):
        cnt += 1

print (float(cnt) / N) * (C-1)
