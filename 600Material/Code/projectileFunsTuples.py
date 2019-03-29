import math
import simpleplot as sp

g = -9.8
dt = 0.01;
damping = 0.6


def initialVel(v1, ang):
    return (v1*math.cos(ang), v1*math.sin(ang))

def degToRad(deg):
    return (deg / 180.0) * math.pi


pos = (0.1,0.1)
vel = initialVel(100.0, degToRad(10.0))

while True:
    pos = (pos[0] + vel[0]*dt, pos[1] + vel[1]*dt + g*dt*dt/2)
    vel = (vel[0] , vel[1] + g*dt)
    sp.plotTrajectory(pos)
    if pos[1] < 0.0 and vel[1] < 0.0:        
        vel = (vel[0], -vel[1]*damping)
    if(pos[1] < 0.0 and vel[1]< 0.1):
        break
sp.doAnimation()
