import time
import random

iters = 1000000
abs_total = 0
sqr_total = 0

x = random.random() * 1000000
y = random.random() * 1000000

for i in range(iters):
	start_time = time.time()
	z = abs(x-y)
	abs_total += time.time() - start_time

	start_time = time.time()
	z = (x-y)**2
	z **= .5
	sqr_total += time.time() - start_time

print("AVG ABS TIME: ", abs_total/iters)
print("AVG SQR TIME: ", sqr_total/iters)
