import math
import simpleplot as sp


def degToRad(ang):
    return (ang/180.0)*math.pi

g = -9.8
dt = 0.01;

def nerdFinalPos(ang, v):
    x = 0.1
    y = 0.1    
    vx = v*math.cos(degToRad(ang))
    vy = v*math.sin(degToRad(ang))

    count = 0
    while count < 5:
        x = x + vx*dt
        y = y + vy*dt + g*dt*dt/2
        vy = vy + g*dt        
        if y < 0.0 and vy <0.0:
            count = count + 1
            vy = -vy*0.5
        # sp.plotTrajectory((x,y))
    return x

pos = nerdFinalPos(45.0, 25.0)

goal = 100.0

testV = 0.0
land = 0.0
count = 0
while land < goal:
    testV = testV + 1.0
    land = nerdFinalPos(45, testV)
    count = count + 1

print "testV = " + str(testV) + " land=" + str(land)
print count
# sp.doAnimation()
