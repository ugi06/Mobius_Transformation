from matplotlib.pyplot import *
from numpy import *
print('1 for unit circle, 2 for ring, 3 for circle')
def arg(x, y):
    return arctan(y / x)
def t(a1, a2, b1, b2):
    n = 9999
    t = []
    r = []
    gk = zeros((2, n))
    z_l = input('|z| ')
    for i in range(n):
        t.append((pi) * random.rand())
        if int(z_l) == 1:
            r.append(random.rand())
        elif int(z_l) == 2:
            r.append(1/random.rand())
        elif int(z_l) == 3:
            r.append(1)
        gk[:, i] = [r[i]*cos(t[i]), r[i]*sin(t[i])]
    plot(gk[0, :], gk[1, :], '.', color='red')
    if (a1, a2) != (0, 0):
        z = (a1**2+a2**2)**.5
        for i in range(n):
            gk[:, i] = [z*r[i] * cos(t[i] + arg(a1, a2)), z*r[i] * sin(t[i] + arg(a1, a2))]
    if (b1, b2) != (0, 0):
        for i in range(n):
            gk[:, i] = gk[:, i] + [b1, b2]
    plot(gk[0, :], gk[1, :], '.', color='blue')
    xlabel('Real Axis')
    ylabel('İmaginary Axis')
    return show()

t(-2,8,-3,1)