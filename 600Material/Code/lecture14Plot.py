import matplotlib.pyplot as pylab




pylab.figure('Figure 1')
# (0,0) , (1,2), (2,2)
pylab.plot( [0, 1, 2], color='r')
pylab.plot([1,2,3], [3,2,1], color='r', marker='*', markersize=20, linewidth=6.0)

pylab.xlabel('x axis')
pylab.ylabel('y axis')
pylab.title('Very cool graph', fontsize='x-large')
pylab.axis([0, 5, -1, 5])

pylab.figure('Figure 2')
pylab.plot( [2, 1, 2], [0, 1, 2])
pylab.title('Not so cool graph', fontsize='xx-large')


pylab.figure('Figure 1')
pylab.plot( [2, 1, 0], [0, 1, 2])
pylab.show()

