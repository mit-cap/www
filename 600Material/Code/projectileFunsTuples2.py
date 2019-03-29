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

def step(p, v):
    p = (p[0] + v[0]*dt, p[1] + v[1]*dt + g*dt*dt/2)
    v = (v[0] , v[1] + g*dt)    
    if p[1] < 0.0 and v[1] < 0.0:        
        v = (v[0], -v[1]*damping)
    return p,v

while True:
    pos, vel = step(pos, vel)
    sp.plotTrajectory(pos)
    if(pos[1] < 0.0 and vel[1]< 0.1):
        break
sp.doAnimation()
