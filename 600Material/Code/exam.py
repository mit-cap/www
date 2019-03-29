def f(L, x):
    def helper(L, x, low, high):
        if high-low<2:
            return 0
        m=(low+high)/2
        print m # note the print
        if L[m]>x:
            return helper(L, x, low, m)
        else:
            return helper(L, x, m, high)
    return helper(L, x, 0, len(L))
L=[1, 4, 5, 6, 13]
y=f(L, 4)
print 'final value:', y
