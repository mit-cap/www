def isVow(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='y'):
        return True;
    else:
        return False;

def checkSpecialCase(l1, l2):
    if(l1=='t' and l2 == 'h'):
        return True
    if(l1=='s' and l2 == 'h'):
        return True
    return False

    
def buildSyllable(word, result, csyll, cpos, size):    
    if(cpos == size):
        result.append(csyll)
        return result
    if(isVow(word[cpos])):
        csyll += word[cpos]
        return findNextVowel(word, result, csyll, cpos, cpos+1, size)
    else:
        csyll += word[cpos]
        return buildSyllable(word, result, csyll, cpos+1, size)


def findNextVowel(word, result, csyll, lastVowel, cpos, size):
    print csyll + ' ' +  str(lastVowel) + ' ' + str(cpos)
    if(cpos == size):
       csyll = csyll + word[lastVowel+1:size]
       result.append(csyll)
       return result
    if(cpos==lastVowel+1 and isVow(word[cpos])):
       csyll += word[cpos]
       return findNextVowel(word, result, csyll, cpos, cpos+1, size)
    if(isVow(word[cpos])):
       end = (lastVowel + cpos)/2
       if(checkSpecialCase(word[end-1], word[end])):
           end += 1
       csyll += word[lastVowel+1:end]
       result.append(csyll)
       return buildSyllable(word, result, '' , end, size)
    else:
       return findNextVowel(word, result, csyll, lastVowel, cpos+1, size)



def syllable(word):
        return buildSyllable(word, [], '', 0, len(word))

           


        
