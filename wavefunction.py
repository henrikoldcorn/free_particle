import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import myfuncs, matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np

a, m = 1, 1#1E-12, 1E-30
hbar = 1 #1.0545718E-34

def psi(r, t, a, m):
    b = (2*a/np.pi)
    expo = np.exp(-a*x*x / (1+(2*1j*hbar*a*t / m)))
    frac = np.sqrt(1 + (2*1j*hbar*a*t / m))
    return pow(b, 1/4) * expo / frac

def p(r, t, a, m):
    return abs(psi(r, t, a, m))**2


fig, ax = plt.subplots()

x = np.arange(-3*a, 3*a, a/600)
line, = ax.plot(x, p(x, 0, a, m))


def animate(i):
    line.set_ydata(p(x, i/100, a, m))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)
ani.save("wavefunction.gif", dpi=100, writer="imagemagick")

plt.show()
