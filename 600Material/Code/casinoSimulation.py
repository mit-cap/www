import random as rr

def rollDice():
    return rr.randint(1,6)


def playGameCasino(playerWager, casinoWager):
    '''Returns the win of the casino on a given game'''
    v = rollDice()
    if v == 1:
        #Casino wins the amount waged by the player
        return playerWager
    else:
        #Casino loses the amount waged by casino
        return -casinoWager



def repeatedPlay(rounds, playerWager, casinoWager):
    casinoWin = 0.0
    for x in xrange(rounds):
        casinoWin += playGameCasino(playerWager, casinoWager)
    return casinoWin/rounds

def compareResult(casino, rounds):
    print "Player = 12, casino = " + str(casino)
    print "Monte Carlo result = " + str(repeatedPlay(rounds, 12, casino))
    print "True solution = " + str( 12.0/6.0 - casino*5.0/6.0)

compareResult(1, 100000)
compareResult(2.4, 100000)
compareResult(3, 100000)

