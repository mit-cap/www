import math
import simpleplot as sp

g = -9.8
dt = 0.01;
damping = 0.6

pos = (0.1, 0.1)

v = 25.0
ang = 30.0
vx = v*math.cos((ang/ 180.0) * math.pi)
vy = v*math.sin((ang/ 180.0) * math.pi)


while True:
    x = x + vx*dt
    y = y + vy*dt + g*dt*dt/2
    vy = vy + g*dt    
    sp.plotTrajectory((x,y))
    print str(y) + " " + str(vy)
    if y < 0.0 and vy < 0.0:
        print "** " + str(y) + " " + str(vy)
        vy = -vy*damping
        if(vy< 0.1):
            break
print str(vx) + " " + str(vy)
sp.doAnimation()
