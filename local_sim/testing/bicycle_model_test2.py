from casadi import *
import numpy as np

import matplotlib.pyplot as plt

opti = Opti()

# simulation parameters
T = 5
dt = 0.01
N = int(T/dt)

# [ x  y  angle  steering_angle  v steering_angle' ]
x = opti.variable(6, N)

# [ v'  steering_angle'' ]
u = opti.variable(2, N-1)


x_i = [ 0, 0, 0, 0, 0, 0 ]
x_f = [ 2, 2, 0, None, None, 0 ]

# cost function
f = 0
for i in range(N):
    f += 1.0 * (x_f[0] - x[0, i])**2 + 1.0 * (x_f[1] - x[1, i])**2

# for i in range(N):
#     f += 

opti.minimize(f)

# kinematics parameters
L = 1 #m
l_r = L/2

print(x.size())

# def get_helpful_subarrays(matrix):
#     class subscriptable:
#         def __init__(self, mx, r):
#             self.mx = mx
#             self.r = r
#         def __getitem__(self, c):
#             return self.mx[self.r, c]
        
#     for i in range(matrix.size()[0]):
#         yield subscriptable(matrix, i)

# for i in range(N-1):
#     x, y, theta, steering_angle, v, steering_vel = get_helpful_subarrays(states)
#     accel, steering_accel = get_helpful_subarrays(inputs)

#     B = atan((l_r * tan(theta[i])))
    
#     opti.subject_to(v[i+1] == v[i] + accel[i] * dt)
#     opti.subject_to(steering_vel[i+1] == steering_vel[i] + steering_accel[i] * dt)

#     opti.subject_to(x[i+1] == x[i] + v[i] * cos(theta[i] + B) * dt)
#     opti.subject_to(y[i+1] == y[i]+ v[i] * sin(theta[i] + B) * dt)
#     opti.subject_to(theta[i+1] == theta[i] + (v[i] * cos(B) * tan(steering_angle[i]) / L) * dt)
#     opti.subject_to(steering_angle[i+1] == steering_angle[i] + steering_vel[i] * dt)

for i in range(N-1):
    B = atan((l_r * tan(x[3, i])))
    opti.subject_to(x[4, i] == x[4, i] + u[0, i] * dt)
    opti.subject_to(x[5, i] == x[5, i] + u[1, i] * dt)
    opti.subject_to(x[0, i + 1] == x[0, i] + x[4, i] * cos(x[2, i] + B) * dt)
    opti.subject_to(x[1, i + 1] == x[1, i] + x[5, i] * sin(x[2, i] + B) * dt)
    opti.subject_to(x[2, i + 1] == x[2, i] + (x[4, i] * cos(B) * tan(x[3, i]) / L) * dt)
    opti.subject_to(x[3, i + 1] == x[3, i] + x[5, i] * dt)

# set bounds on inputs

# # set initial conditions 
for i in range(len(x_i)):
    opti.subject_to(x_i[i] == x[i, 0])



# for i in range(len(x_f)):
#     if x_f[i] is not None:
#         opti.subject_to(x_f[i] == x[i, -1])

# set accel constraints
# for i in range(N-1):
#     opti.subject_to(opti.bounded(-500, inputs[0, i] ,500))
#     opti.subject_to(opti.bounded(-500, inputs[1, i] ,500))

# set final conditions
# opti.subject_to(x[0, -1] == x_T[0])
# opti.subject_to(x[1, -1] == x_T[1])

opti.solver('ipopt')

soln = opti.solve()

X = soln.value(x)
U = soln.value(u)

print(X[0][0], X[1][0], X[0][-1], X[1][-1])
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