import syllable


def tester(fun):
    out = fun('cooperate')
    print out
    if(out != ['coo', 'pe', 'ra', 'te']):
        print "ERROR!!"
        return False    

    out = fun('birthday')
    print out
    if(out != ['birth', 'day']):
        return False

    out = fun('antidisestablishmentarianist')
    if(out != ['an', 'ti', 'di', 'ses', 'tab', 'lish', 'men', 'ta', 'ria', 'nist']):
        return False
    print out

    
    out = fun('the')
    if(len(out) != 1):
        return False
    print out

    out = fun('a')
    if(len(out) != 1):
        return False
    print out

    out = fun('gym')
    if(len(out) != 1):
        return False
    print out

    out = fun('grr')
    if(len(out) != 1):
        return False
    print out

    out = fun('')
    if(len(out) != 1):
        return False
    print out
    
    return True
    


if(tester(syllable.syllable)):
    print "Success!!"
else:
    print "Failure"
    
