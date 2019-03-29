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
    """buildSyllable phase of syllable algorithm. Assumes csyll contains no vowels"""
    if(cpos == size): # Base Case
        result.append(csyll) # Append the current syllable to the result
        return result        # Return
    if(isVow(word[cpos])):   # Upon finding a Vowel, transition to findNextVowel phase.
        csyll += word[cpos]  # But first add the vowel to the current word.
                             # if csyll has a vowel, this would introduce a second one.
        return findNextVowel(word, result, csyll, cpos, cpos+1, size)
    else:
        csyll += word[cpos] # Recursive case; advance pos by one and keep going.
        return buildSyllable(word, result, csyll, cpos+1, size)


def findNextVowel(word, result, csyll, lastVowel, cpos, size):
    """findNextVowel phase of syllable algorithm. Assumes lastVowel is lower than cpos."""
    if(cpos == size):
       if(lastVowel+1 < size): # Can this condition ever be false?
          csyll = csyll + word[lastVowel+1:size]
       result.append(csyll)
       return result
    if(cpos==lastVowel+1 and isVow(word[cpos])): # Two consecutive vowels. start findNextVowel  phase from the second one.
       csyll += word[cpos]
       return findNextVowel(word, result, csyll, cpos, cpos+1, size)
    if(isVow(word[cpos])): # Found the next vowel. 
       end = (lastVowel + cpos + 1)/2 # Find the midpoint
       if(checkSpecialCase(word[end-1], word[end])): # check for the 'th' or 'sh' special case.
           end += 1
       csyll += word[lastVowel+1:end]
       result.append(csyll) # append the result 
       return buildSyllable(word, result, '' , end, size) # start the next syllable from end.
    else:
       return findNextVowel(word, result, csyll, lastVowel, cpos+1, size)



def syllable(word):
        return buildSyllable(word, [], '', 0, len(word)) # the result is initially empty, and so is the current syllable.

           
