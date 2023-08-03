import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

M = 0.5
kL = 1
ekl = np.exp(1j*kL)
eklM = 1 / ekl

umoins = (1 - M) * eklM / ((1 - M) * eklM - (1 + M) * ekl)
uplus = (1 + M) * ekl / ((1 + M) * ekl - (1 - M) * eklM)

x = np.arange(0, 1, 0.001)

def ucorde(x,t):
    return uplus * np.exp(1j * (t - x)) + umoins * np.exp(1j * (t + x))

t = 0
ts = np.arange(0, 10, 0.1)
f, ax  = plt.subplots()
corde, = ax.plot(x, np.real(ucorde(x, t)))
ax.set_ylim([-10, 10])
ax.set_xlim([0, 1])


def update(frame):
    corde.set_data(x, np.real(ucorde(x, frame)))
    return corde,

ani = FuncAnimation(f, update, frames=ts, blit=True)

plt.show()