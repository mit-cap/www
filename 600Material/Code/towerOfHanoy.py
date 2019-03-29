t0 = []
t1 = []
t2 = []
T=[t0, t1, t2]



def initialize(n): 
    for x in xrange(1, n+1):
        t0.append(x) # Note that t0 is aliased to T[0].
                     # appending to t0 is the same as appending to T[0].


def movePiece(orig, dest):
    """Move a piece from orig to dest. Print the instructions and also update the state. """
    print " move from " + str(orig) + " to " + str(dest)
    x = raw_input()
    lastPos = len(T[orig])-1
    tomove = T[orig][lastPos]
    T[dest].append(tomove)
    T[orig].remove(tomove)

    print T[0]
    print T[1]
    print T[2]


def getOther(orig, dest):
    t = [0, 1, 2]
    t.remove(orig)
    t.remove(dest)
    return t[0]



def moveTower(orig, dest, n):
    """Move n pieces from orig to dest"""
    if(n==1):
        movePiece(orig, dest)
    else:
        other = getOther(orig, dest)
        moveTower(orig, other, n-1)
        movePiece(orig, dest)
        moveTower(other, dest, n-1)

initialize(5)
moveTower(0, 2, 5)
