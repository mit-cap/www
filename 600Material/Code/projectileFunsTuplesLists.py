import math
import simpleplot as sp

g = -9.8
dt = 0.01;
damping = 0.6


def initialVel(v1, ang):
    return (v1*math.cos(ang), v1*math.sin(ang))

def degToRad(deg):
    return (deg / 180.0) * math.pi


pos = [(0.1,0.1)] #list with one position
vel = [initialVel(100.0, degToRad(10.0))] # list with one velocity

def step(p, v):
    p = (p[0] + v[0]*dt, p[1] + v[1]*dt + g*dt*dt/2)
    v = (v[0] , v[1] + g*dt)
    bounced = False
    if p[1] < 0.0 and v[1] < 0.0:        
        v = (v[0], -v[1]*damping)
        bounced = True
    return p,v, bounced

while len(pos)<30:
    npos = []
    nvel = []
    for p,v in zip(pos, vel):
        p,v, b = step(p, v)
        npos.append(p)
        nvel.append(v)
        if(b):
            npos.append(p)
            nvel.append((-v[0], v[1]))
    pos = npos
    vel = nvel    
    
    sp.plotTrajectory(pos)
        
    if(pos[0][1] < 0.0 and vel[0][1]< 0.5):
        break
sp.doAnimation()
