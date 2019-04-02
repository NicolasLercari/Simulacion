import numpy as np
import matplotlib.pyplot as plt 

def inversa(x):
	return 1 / (1 - (4*x/5))


l=[inversa(np.random.random()) for _ in xrange(100000)]



fig, axs = plt.subplots()

axs.hist(l, bins=1000)

plt.show()