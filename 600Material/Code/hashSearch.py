import time

def myhash(w):
    return hash(w) % 1000

def readList(fname):
    L = []
    f = open(fname)
    for x in f:
        L.append(x[0:len(x)-1])
    return L


def readListHash(fname):
    L = []
    f = open(fname)
    for x in f:
        w = x[0:len(x)-1]
        L.append((myhash(w), w))
    return L

def findWord(word, wlist):
    for w in wlist:
        if w==word:
            return True
    return False

def findWordHash(word, wlist):
    whash = myhash(word)
    for h,w in wlist:
        if h==whash:
            if w == word:
                return True

    return False


mylist = readList('wordlist')
print len(mylist)
start = time.clock()
found = findWord('Dictionary: The current word is office', mylist)
end = time.clock()
print 'no hash takes ' + str(end-start)

myHlist = readListHash('wordlist')
print len(myHlist)
start = time.clock()
found = findWordHash('Dictionary: The current word is office', myHlist)
end = time.clock()
print 'hash takes ' + str(end-start)
