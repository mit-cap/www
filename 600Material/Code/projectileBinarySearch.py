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

goal = 500.0

low = 0.0
high = 500.0

mid = (low+high)/2.0
landing = nerdFinalPos(45.0, mid)

while abs(landing - goal)>0.01:
    if(landing < goal):
        low = mid
    else:
        high = mid
    mid = (low+high)/2.0
    landing = nerdFinalPos(45.0, mid)
    print "low=" + str(low) + " high=" + str(high) +
        " mid = " + str(mid) + " landing = " + str(landing)

    
# sp.doAnimation()

