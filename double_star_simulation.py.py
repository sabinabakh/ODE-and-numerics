#!/usr/bin/env python3

"""
Double Star Simulation
"""

"""double_star(m1,m2,x1,x2,p,h) solves the differential equation using the classic Runge-Kutta method
and creates a film showing the movement of the masses m1, m2.

p: determines initial speeds
x1, x2: initial positions
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from numpy import linalg as la

#%matplotlib notebook

def double_star(M1, M2, x1, x2, p, H):

    global m1
    global m2
    global gamma
    global h

    m1 = M1
    m2 = M2
    gamma = 1
    h = H

    # Initial condition

    x1_0 = [x1, 0]
    x2_0 = [x2, 0]
    v1_0 = [0, p / m1]
    v2_0 = [0, -p / m2]

    global y

    y = np.array([x1_0, x2_0, v1_0, v2_0])

    # Animating

    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)

    point1, = ax.plot(y[0][0], y[0][1], marker="o")
    point2, = ax.plot(y[1][0], y[1][1], marker="o")

    def animate(n):
        
        x1, y1, x2, y2 = calculate_trajectory(n, f, y, h)
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)

        ax.plot(x1, y1, '--', color='black')
        ax.plot(x2, y2, '--', color='black')

        for i in range(n):
            point1.set_data([x1[i]], [y1[i]])
            point2.set_data([x2[i]], [y2[i]])

        return point1, point2

    anim = animation.FuncAnimation(fig, animate, frames=1000, interval=10, repeat=True)
    plt.show()

    return anim


def calculate_trajectory(n, f, y, h):
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for i in range(n):
        y = runge_kutta_step(f, y, h)
        x1.append(y[0][0])
        x2.append(y[1][0])
        y1.append(y[0][1])
        y2.append(y[1][1])

    return x1, y1, x2, y2


def runge_kutta_step(f, y, h):

    k1 = f(y)
    k2 = f(y + h * (1 / 2) * k1)
    k3 = f(y + h * (1 / 2) * k2)
    k4 = f(y + h * k3)

    y_new = y + h * ((k1 / 6) + (k2 / 3) + (k3 / 3) + (k4 / 6))

    return y_new


def f(y):

    F1 = ((gamma * m1 * m2) / (la.norm(y[1] - y[0]) ** 3)) * (y[1] - y[0])
    F2 = -F1

    return np.array([y[2], y[3], F1 / m1, F2 / m2])


anim = double_star(1, 5, -1, 1, 1, 0.01)
