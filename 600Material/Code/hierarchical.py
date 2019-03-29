import math
import random
import pylab



class Cluster:
    def getCenter(self):
        pass
    def getSum(self):
        pass
    def getN(self):
        pass    
    def plot(self):
        pass



class Singleton(Cluster):
    def __init__(self, pt):
        assert type(pt) == list
        self.pt = pt
    def getCenter(self):
        return self.pt
    def getSum(self):
        return self.pt
    def getN(self):
        return 1
    def __str__(self):
        return '(' + "{0:.2f}".format(self.pt[0]) + ',' + "{0:.2f}".format(self.pt[1]) + ')'
    def plot(self):
        pylab.plot([self.pt[0]], [self.pt[1]], 'go')



class Composite(Cluster):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
    def getN(self):
        return self.c1.getN() + self.c2.getN()
    def getSum(self):
        s1 = self.c1.getSum()
        s2 = self.c2.getSum()
        return [ x+y  for (x,y) in zip(s1, s2)]
    def getCenter(self):
        s = self.getSum()
        n = self.getN()
        return [ x/n for x in s]
    def __str__(self):
        return '[' + str(self.c1) + ', ' + str(self.c2) + ']'
    def plot(self):
        self.c1.plot()
        self.c2.plot()
        p1 = self.c1.getCenter()
        p2 = self.c2.getCenter()
        pylab.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-')



def dist(c1, c2):
    p1 = c1.getCenter()
    p2 = c2.getCenter()
    t = 0.0
    for x,y in zip(p1, p2):
        t += (x-y)**2
    return math.sqrt(t)


def hierarchical(data):
    def findMinDist(clist):
        mv = (-1, -1)
        minDist = 1000000.0        
        ll = len(clist)
        for x in xrange(ll):
            for y in xrange(x+1, ll):
                d = dist(clist[x], clist[y])
                if d < minDist:
                    mv = (x, y)                    
                    minDist = d
        return mv
    
    clist = [Singleton(x) for x in data]
    while len(clist) > 1:        
        mx, my = findMinDist(clist)            
        
        nxt = []
        for t in xrange(len(clist)):
            if t != mx:
                if t == my:
                    nxt.append(Composite(clist[mx], clist[my]))
                else:
                    nxt.append(clist[t])
        clist = nxt
    clist[0].plot()
    return clist



def genData(N, K, sigma):
    centers = [ (random.random()*50, random.random()*50)  for i in xrange(K)]
    rv = []
    for i in xrange(N):
        cluster = centers[random.randint(0, K-1)]
        pt = [random.gauss(cluster[0], sigma), random.gauss(cluster[1], sigma)]
        rv.append(pt)
    return rv



data = genData(100, 3, 3)
for x in data:
    pylab.plot([x[0]], [x[1]], 'ro')


pylab.show()
