
def movePiece(orig, dest):
    """Move a piece from orig to dest. Print the instructions and also update the state. """
    print " move from " + str(orig) + " to " + str(dest)


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

moveTower(0, 2, 5)
