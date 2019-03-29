import time

def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def isSorted(L):
    for i in xrange(0, len(L)-1):            
            if(L[i] > L[i+1]):
                return False
    return True

def bubbleSort(L):    
    doMore = True
    while(doMore):
        doMore = False
        for i in xrange(0, len(L)-1):            
            if(L[i] > L[i+1]):                                
                swap(L, i, i+1)
                doMore = True

    return L

def insertionSort(L):
    for end in xrange(1, len(L)):
        #what do we know here?
        # assert isSorted(L[0:end])
        # note: this check is expensive, so only run it when you are debugging
        temp = L[end]
        for i in xrange(0, end):
            if(temp < L[i]):
                temp2 = L[i]
                L[i] = temp
                temp = temp2
        L[end] = temp
        #what do we know here?
        #assert isSorted(L[0:end+1])
        #note: this check is expensive, so only run it when you are debugging
    return L


def merge(L1, L2):
    result = []
    p1 = 0
    p2 = 0
    for i in xrange(0, len(L1) + len(L2)):
        if(p1 < len(L1) and p2 < len(L2)):
            if( L1[p1] < L2[p2] ):
                result.append(L1[p1])
                p1 += 1
            else:
                result.append(L2[p2])
                p2 += 1
        else:
            if p1 < len(L1):
                result.append(L1[p1])
                p1 += 1
            else:
                result.append(L2[p2])
                p2 += 1
                
    return result

def mergeSort(L):
    if(len(L) <= 1):
        return L
    mid = len(L) / 2
    L1 = mergeSort(L[0:mid])
    L2 = mergeSort(L[mid:])
    return merge(L1, L2)
    

def readList(fname):
    L = []
    f = open(fname)
    for x in f:
        L.append(x[0:len(x)-1])
    return L


def sortLongList(inlist, algo, algoname):
    mylist = inlist[0:] # we want to make a copy because some of the sorting algorithms modify the underlying array.
    start = time.clock()
    out = algo(mylist)
    end = time.clock()
    print algoname + ' takes ' + str(end-start) + ' seconds for a list of len ' + str(len(mylist))
    assert isSorted(out)

mylist = readList('randomList')
sortLongList(mylist, mergeSort, 'mergeSort')
sortLongList(mylist, insertionSort, 'insertionSort')
sortLongList(mylist, bubbleSort, 'bubbleSort')
    
# mylist = [3, 5, 7, 2, 77, 3, 22, 1, 8, 4, 17]

# print mergeSort(mylist)
