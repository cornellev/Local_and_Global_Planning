from casadi import *
import numpy as np

import matplotlib.pyplot as plt

opti = Opti()

# simulation parameters
T = 5
dt = 0.01
N = int(T/dt)

# [ x_cg, y_cg, angle, steering angle ]
x = opti.variable(4, N)

# [ v_cg (at front wheel???), steering omega ]
u = opti.variable(2, N-1)


x_0 = [ 0, 0, 0, 0.0 ]
x_T = [ 2, 2, 0, 0 ]

# cost function
f = 0
for i in range(N):
    f += 1.0 * (x_T[0] - x[0, i])**2 + 1 * (x_T[1] - x[1, i])**2

# for i in range(N):
#     f += 
    
opti.minimize(f)

# kinematics parameters
L = 1 #m
l_r = L/2

for i in range(N-1):
    B = atan((l_r * tan(x[3, i])))
    opti.subject_to(x[0, i + 1] == x[0, i] + u[0, i] * cos(x[2, i] + B) * dt)
    opti.subject_to(x[1, i + 1] == x[1, i] + u[0, i] * sin(x[2, i] + B) * dt)
    opti.subject_to(x[2, i + 1] == x[2, i] + (u[0, i] * cos(B) * tan(x[3, i]) / L) * dt)
    opti.subject_to(x[3, i + 1] == x[3, i] + u[1,i] * dt)


# set bounds on inputs

for i in range(N-1):
    opti.subject_to(opti.bounded(-5,u[0, i],+5))
    opti.subject_to(opti.bounded(-5,u[1, i],+5))

# set initial conditions 
for i in range(4):
    opti.subject_to(x_0[i] == x[i, 0])

# set final conditions
# opti.subject_to(x[0, -1] == x_T[0])
# opti.subject_to(x[1, -1] == x_T[1])

opti.solver('ipopt')

soln = opti.solve()

X = soln.value(x)
U = soln.value(u)

print(X[0][-1], X[1][-1])
print(U[1])
# print(X[0][-1], X[1][-1])
# print(X[0])

plt.scatter(X[0], X[1])
plt.show()

T = np.linspace(0, T, N)
plt.plot(T, X[2])

TU = np.linspace(0, T-dt, N-1)
# plt.plot(TU, U[1])
plt.plot(TU, U[0])
# plt.plot(T, X[2])
plt.show()