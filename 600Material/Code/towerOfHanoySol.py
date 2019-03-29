
t1 = [4, 3, 2, 1]
t2 = []
t3 = []
T = [t1,t2,t3]


def movePiece(orig, dest):
    tomove = T[orig][len(T[orig])-1]
    T[dest].append(tomove)
    T[orig].remove(tomove)    
    print "move from " + str(orig) + " to " + str(dest)
    x = raw_input()
    print T[0]
    print T[1]
    print T[2]


def getOther(origin, dest):
    t = [0, 1, 2]
    t.remove(origin)
    t.remove(dest)
    return t[0]

def moveTower(origin, dest, n):
    if(n==1):
        movePiece(origin, dest)
    else:
        other = getOther(origin, dest)
        moveTower(origin, other, n-1)
        movePiece(origin, dest)
        moveTower(other, dest, n-1)


moveTower(0, 2, 4)
