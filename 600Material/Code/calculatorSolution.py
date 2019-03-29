
def isParen(c):
    return c == '(' or c==')'

def isSpace(c):
    return c == ' '

def isDigit(c):
    return c in [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def evalInsideParen(word):
    # print 'evalInsideParen ' + word
    if(len(word)==0):
        return (False, 0, word)
    if isSpace(word[0]):
        return evalInsideParen(word[1:])
    if isDigit(word[0]):
        (rf, rest) = closeParen(word[1:])
        return (rf, int(word[0]), rest)
    if word[0] == '+':
        (rf, val1, rest) = evalExpression(word[1:])
        if not rf:
            return (False, 0, word)
        (rf, val2, rest) = evalExpression(rest)
        if not rf:
            return (False, 0, word)
        (rf, rest) = closeParen(rest)
        return (rf, val1 + val2, rest)
    if word[0] == '*':
        (rf, val1, rest) = evalExpression(word[1:])
        if not rf:
            return (False, 0, word)
        (rf, val2, rest) = evalExpression(rest)
        if not rf:
            return (False, 0, word)
        (rf, rest) = closeParen(rest)
        return (rf, val1 * val2, rest)
    return (False, 0, word)


def evalExpression(word):
    # print 'evalExpression ' + word
    if(len(word)==0):
        return (False, 0, word)
    if isSpace(word[0]):
        return evalExpression(word[1:])
    if word[0] == '(':
        return evalInsideParen(word[1:])
    return (False, 0, word)

def closeParen(word):
    # print 'closeParen ' + word
    if(len(word)==0):
        return (False, word)
    if isSpace(word[0]):
        return closeParen(word[1:])
    if word[0] == ')':
        return (True, word[1:])
    return (False, word)


def runExpression(word):
    (rf, rv, w) = evalExpression(word)
    return rv

def testerFunction(evaluator):
    def check(instr, expected):
        rv = evaluator(instr)
        if( rv != expected ):
            print 'Test for "' + instr + '" failed returned ' + str(rv) + ' instead of ' + str(expected)
            return False
        print instr + ' = ' + str(rv)
        return True
    
    rv = True
    rv = check('(+ (5) (9))', 14) and rv
    rv = check('(+ (5) (10))', 0) and rv # Remember, single digits only.
    rv = check('[([]() )[  [u](  x )]]', 0) and rv    
    
    rv = check('(* (3) (2', 0) and rv
    rv = check('(* (+ (3) (2)) (* (2) (2)) )', 20) and rv
    #Add more of your own tests here.

    
    if(rv):
        print 'All tests passed!'


testerFunction(runExpression)
