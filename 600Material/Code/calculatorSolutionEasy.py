

def isInt(w):
    if(len(w)>0):
        if w[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
    return False


def printExpr(elist):
    if(len(elist)==0):
        return '', elist
    if(isInt(elist[0])):
        return elist[0], elist[1:]
    if elist[0] == '*':
        left, rest = printExpr(elist[1:])
        right, rest = printExpr(rest)
        return '(' + left + '*' + right + ')', rest
    if elist[0] == '+':
        left, rest = printExpr(elist[1:])
        right, rest = printExpr(rest)
        return '(' + left + '+' + right + ')', rest
    return '', elist


def evalExpr(elist):
    if(len(elist)==0):
        return 0, elist
    if(isInt(elist[0])):
        return int(elist[0]), elist[1:]
    if elist[0] == '*':
        left, rest = evalExpr(elist[1:])
        right, rest = evalExpr(rest)
        return left * right , rest
    if elist[0] == '+':
        left, rest = evalExpr(elist[1:])
        right, rest = evalExpr(rest)
        return left + right, rest
    return 0, elist



def testerPrinter(printer):
    def check(instr, expected):
        rv, rest = printer(instr)
        if( rv != expected ):
            print 'Test for "' + str(instr) + '" failed returned ' + str(rv) + ' instead of ' + str(expected)
            return False
        print str(instr) + ' = ' + str(rv)
        return True
    
    rv = True
    rv = check(['+', '5', '9'], '(5+9)') and rv
    rv = check(['+', '5', '10'], '(5+10)') and rv # Remember, single digits only.
    rv = check(['+', '8', '*', '5', '2'], '(8+(5*2))') and rv    
        
    #Add more of your own tests here.

    
    if(rv):
        print 'All tests passed!'


def testerEvaluator(evaluator):
    def check(instr, expected):
        rv, rest = evaluator(instr)
        if( rv != expected ):
            print 'Test for "' + str(instr) + '" failed returned ' + str(rv) + ' instead of ' + str(expected)
            return False
        print str(instr) + ' = ' + str(rv)
        return True
    
    rv = True
    rv = check(['+', '5', '9'], 14) and rv
    rv = check(['+', '5', '10'], 15) and rv # Remember, single digits only.
    rv = check(['+', '8', '*', '5', '2'], 18) and rv    
        
    #Add more of your own tests here.

    
    if(rv):
        print 'All tests passed!'

testerPrinter(printExpr)
testerEvaluator(evalExpr)
