import math
import random
import pylab


def dist(c1, c2):    
    t = 0.0
    for x,y in zip(c1, c2):
        t += (x-y)**2
    return math.sqrt(t)

        

def genData(N, K, sigma):
    centers = [ (random.random()*50, random.random()*50)  for i in xrange(K)]
    rv = []
    for i in xrange(N):
        cluster = centers[random.randint(0, K-1)]
        pt = [random.gauss(cluster[0], sigma), random.gauss(cluster[1], sigma)]
        rv.append(pt)
    return rv


def mean(ll):
    pt = [0.0, 0.0]
    if(len(ll)==0):
        return (random.random()*50, random.random()*50)
    for x in ll:
        pt[0] += x[0]
        pt[1] += x[1]
    return [pt[0]/len(ll), pt[1]/len(ll)]

def kmeans(data, k):
    centers = [ (random.random()*50, random.random()*50)  for i in xrange(k)]
    clusters = [data, [], []]
    for t in xrange(5):
        D = []
        tclus = [[],[],[]]
        oldCenters = centers[:]        
            
        for t in clusters:
            D = D + t
        print len(D)
        for pt in D:
            minC = -1
            minD = 100000
            for x in xrange(k):
                d = dist(centers[x], pt)
                # print str(centers[x]) + ' d=' + str(d)
                if d < minD:
                    minD = d
                    minC = x
            tclus[minC].append(pt)
        clusters = tclus
        for x in xrange(k):
            centers[x] = mean(clusters[x])            
            for pt in clusters[x]:
                if x == 0:
                    c = 'ro'
                if x == 1:
                    c = 'go'
                if x == 2:
                    c = 'bo'
                pylab.plot([pt[0]], [pt[1]], c)
        pylab.xlim(-10, 50)
        pylab.ylim(-10, 50)
        for x in xrange(k):            
            pylab.plot([oldCenters[x][0]], [oldCenters[x][1]], 'rx', markersize=10.0)
            print oldCenters[x]
        
        pylab.show()


data = genData(30, 3, 3)
#for x in data:
#    pylab.plot([x[0]], [x[1]], 'ro')
kmeans(data, 3)

