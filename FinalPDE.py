#Julia Mascialino

import math
import numpy as np
import matplotlib.pyplot as plt

### intial variable declaration
a = 1
ntotal = 20
itotal = 11
gx = 3
gt = 3
dt = gt / ntotal
dx = gx / itotal
l = dt / (2 * dx)
u = np.zeros((ntotal, itotal))
x_points = np.zeros(itotal)

### function f(x) = sin(pi * x)
def f(x):
    if 0 <= x <= 1:
        return round(math.sin(math.pi * x), 3)
    else:
        return 0

### initial condition for u(0,x)
for i in range(1, itotal + 1):
    x = (i - 1) * dx
    u[0, i - 1] = f(x)
    x_points[i - 1] = x


### full grid for u(r, c)
for r in range(ntotal - 1):
    for c in range(itotal - 1):
        current = u[r, c]
        past = u[r, c - 1]
        future = u[r, c + 1]
        new = round(current - a * l * (future - past), 3)
        if new > 0:
            u[r + 1, c] = new

### plotting numerical and analyitcal solution seperatly
plot1 = plt.figure(1)
for t in range(4):
    plt.plot(x_points + t, u[0], ".-", label = "t_a = " + str(t))

plt.title("Analytical Solution for i = " + str(itotal) + ", n = " + str(ntotal))
plt.xlabel('x + t')
plt.ylabel('u [t], t = 0')
plt.legend()

plot2 = plt.figure(2)
for t in range(4):
    plt.plot(x_points + t, u[t], ".--", label = "t_n = " + str(t))

plt.title("Numerical Solution for i = " + str(itotal) + ", n = " + str(ntotal))
plt.xlabel('x + t')
plt.ylabel('u [t], t = [0, 3]')
plt.legend()

plt.show()

### plotting numerical and analyitcal solution together
plot1 = plt.figure(1)
for t in range(4):
    plt.plot(x_points + t, u[0], ".-", label = "t_a = " + str(t))

for t in range(4):
    plt.plot(x_points + t, u[t], ".--", label = "t_n = " + str(t))

plt.title("Analytical Numerical Comparison for i = " + str(itotal) + ", n = " + str(ntotal))
plt.xlabel('x + t')
plt.ylabel('u [t], t = [0, 3]')
plt.legend()
plt.show()

### determining the error between anaylitcal and numerical solutions
error = np.zeros((4, itotal))
max_val = 0
max_error = np.zeros(4)
for x in range(4):
    for i in range(itotal):
        error[x, i] = abs(u[0, i] - u[x, i])
        if error[x, i] > max_val:
            max_error[x] = error[x, i]
            max_val = error[x, i]

### plotting numerical and analyitcal solution error
for t in range(4):
    plt.plot(t, max_error[t], ".", label = "max error at time " + str(t))
plt.title("Error for i = " + str(itotal) + ", n = " + str(ntotal))
plt.xlabel('t')
plt.ylabel('max error')
plt.legend()
plt.show()
