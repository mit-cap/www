import random as rr

def checkPair(x,y):
    if(x==y):
        return True
    if(x=='o' and y=='u'):
        return True
    if(x=='e' and y=='a'):
        return True
    if(x=='o' and y=='a'):
        return True
    if(x=='y' and y=='o'):
        return True
    if(x=='o' and y=='i'):
        return True
    if(x=='i' and y=='e'):
        return True
    if(x=='i' and y=='o'):
        return True
    return False

def isVow(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='y'):
        return True;
    else:
        return False;


def sylable(word):    
    def beforeVow(lst, i, sz, cs):
        if(i==sz):
            lst.append(cs)
            return
        if(not isVow(word[i])):            
            cs = cs + word[i]
            beforeVow(lst, i+1, sz, cs)
        else:
            cs = cs + word[i]
            inVow(lst, i+1, sz, i, cs)
    def inVow(lst, i, sz, vp, cs):
        if(i==sz):
            if(vp+1 < sz):
                cs = cs + word[vp+1:sz]
            lst.append(cs)
            return
        if(i==vp+1 and isVow(word[i]) and checkPair(word[vp], word[i])):
            cs = cs + word[i]
            inVow(lst, i+1, sz, i,  cs)
        else:
            if(isVow(word[i])):
                end = ((vp+i+1)/2)                
                if(end < sz and word[end-1] == 's' and word[end] == 'h'):
                    end = end + 1
                cs = cs + word[vp+1:end]
                lst.append(cs)                
                beforeVow(lst, end, sz, '')
            else:
                inVow(lst, i+1, sz, vp, cs)

    l = []
    beforeVow(l, 0, len(word), '')
    return l


def addAppend(key, val, D):
    if(key in D):
        D[key].append(val)
    else:
        D[key] = [val]

def addAppend(key1, key2, val, D):
    if(key1 in D):
        d2 = D[key1]
    else:
        d2 = {}
        D[key1] = d2
    addAppend(key2, val, d2)
    
    

DbyLastSyl = {}
DbyWLen = {}

f = open('curatedlist')

for w in f:
    w = w[0:len(w)-1]
    bw = sylable(w)
    wl = len(bw)
    if( wl in DbyWLen):
        DbyWLen[wl].append(w)
    else:
        DbyWLen[wl] = [w]

    ls = bw[wl-1]
    if( ls in DbyLastSyl ):
        DbyLastSyl[ls].append(w)
    else:
        DbyLastSyl[ls] = [w]



def buildPhrase(plist, result):
    print plist
    lastSyl = plist[len(plist)-1]
    if(lastSyl in DbyLastSyl):
        wl = DbyLastSyl[lastSyl]
        cword = wl[rr.randint(0,len(wl)-1)]
        print cword
        result = cword + " " + result
        wld = sylable(cword)
        if(len(wld) + 3 < len(plist)):
            return buildPhrase(plist[0:len(plist)-len(wld)], result)
        else:
            if(len(wld) >= len(plist)):
                return result
            else:
                wl = DbyWLen[len(plist)-len(wld)]
                return wl[rr.randint(0,len(wl)-1)] + " " + result


def sylSplit(phrase):
    plist = []
    for x in phrase.split():
        plist.extend(sylable(x))
    return plist

def rhymePhrase(phrase):
    plist = sylSplit(phrase)    
    print phrase
    res = buildPhrase(plist, '')
    print res
    print sylSplit(res)
    

rhymePhrase("I am a great professor")
