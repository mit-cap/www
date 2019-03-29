import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import types

fig = plt.figure()
ax = fig.add_subplot(111)
lines = []
ax.set_ylim(-0.1, 5)
ax.set_xlim(0, 11)
ax.grid()
traj = []


def plotTrajectory(pos):
    if(type(pos)==types.TupleType):
        pp = [pos]
    else:
        pp = pos
    while(len(lines)<len(pos)):
            ll, = ax.plot([], [], lw=2)
            lines.append(ll)
            
    traj.append(pp)

def doAnimation():    
    ani = animation.FuncAnimation(fig, run, len(traj), blit=True, interval=10, repeat=False)
    plt.show()

xlines = []
ylines = []
def run(arg):
    # update the data
    p = traj[arg]
    pxmax = 0
    pymax = 0
    for t in xrange(len(p)):
        while(len(xlines)<=t):
            xlines.append([])
            ylines.append([])
        xlines[t].append(p[t][0])
        ylines[t].append(p[t][1])
        if(p[t][0]> pxmax):
            pxmax = p[t][0]
        if(p[t][1]> pymax):
            pymax = p[t][1]
    
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    if pxmax >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    if pymax >= ymax:
        ax.set_ylim(ymin, 2*ymax)
        ax.figure.canvas.draw()
    for t in xrange(len(xlines)):
        lines[t].set_data(xlines[t], ylines[t])    
    return lines
