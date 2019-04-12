import numpy as np
import matplotlib.pyplot as plt 

def inversa(x):
	return 20 * x * np.math.pow(1-x,3)

c=2.11

x=[inversa(np.random.random()) for _ in range(100000)]
y=[np.random.random() for _ in range(100000)]
u=[np.random.random() for _ in range(100000)]


print(x / y*c)

