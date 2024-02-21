from casadi import *
import numpy as np
import matplotlib.pyplot as plt

opti = Opti()

# simulation parameters
T = 5
dt = 0.025
N = int(T/dt)

# [ x y x' y' theta theta' ]^T
states = opti.variable(6, N)

# [ a alpha ]
inputs = opti.variable(2, N-1)

# Set initial and final conditions
states_i = [ 0, 0, 0, 0, 0, 0 ]
states_f = [ 2, 2, 0, 0, None, 0]

for i in range(6):
    if states_i[i] is not None:
        opti.subject_to(states[i, 0] == states_i[i])
    
    if states_f[i] is not None:
        opti.subject_to(states[i, N-1] == states_f[i])


# cost function
f = 0
for i in range(N):
    f += 1.0 * (states_f[0] - states[0, i])**2 + 1.0 * (states_f[1] - states[1, i])**2

for i in range(N-1):
    f += inputs[0,i]**2 + inputs[1,i]**2


# apply kinematic constraints
        
def get_helpful_subarrays(matrix):
    class subscriptable:
        def __init__(self, mx, r):
            self.mx = mx
            self.r = r
        def __getitem__(self, c):
            return self.mx[self.r, c]
        
    for i in range(matrix.size()[0]):
        yield subscriptable(matrix, i)


x, y, vx, vy, theta, omega = get_helpful_subarrays(states)
accel, alpha = get_helpful_subarrays(inputs)
for i in range(N-1):
    opti.subject_to(x[i + 1] == x[i] + vx[i] * dt)
    opti.subject_to(y[i + 1] == y[i] + vy[i] * dt)
    opti.subject_to(vx[i + 1] == vx[i] + accel[i] * cos(theta[i]) * dt)
    opti.subject_to(vy[i + 1] == vy[i] + accel[i] * sin(theta[i]) * dt)
    opti.subject_to(theta[i + 1] == theta[i] + omega[i] * dt)
    opti.subject_to(omega[i + 1] == omega[i] + alpha[i] * dt)

for i in range(N):
    opti.subject_to(opti.bounded(-5, vx[i], 5))
    opti.subject_to(opti.bounded(-5, vy[i], 5))

for i in range(N-1):
    opti.subject_to(opti.bounded(-10, accel[i], 10))
    opti.subject_to(opti.bounded(-10, alpha[i], 10))

ox, oy, r = 1, 1, 1
for i in range(N-1):
    opti.subject_to((x[i] - ox)**2 + (y[i] - oy)**2 >= r**2)

opti.solver('ipopt')
soln = opti.solve()

x, y, vx, vy, theta, omega = soln.value(states) 
accel, alpha = soln.value(inputs)

print(x[-1], y[-1])
print(accel)


circle = plt.Circle((ox, oy), r, edgecolor='b', facecolor='none')


plt.gca().add_patch(circle)

plt.scatter(x, y)
plt.show()

# t = np.linspace(0, T, N)
# plt.plot(t, theta)

# tu = np.linspace(0, T-dt, N-1)
# plt.plot(tu, accel)

# plt.show()