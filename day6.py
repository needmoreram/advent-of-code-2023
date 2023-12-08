import math
import numpy as np

games = [(34, 204), (90, 1713), (89, 1210), (86, 1780)]

def numways(time, dist):
	roots = np.roots([1, -time, dist])
	return (int(max(roots)) - int(min(roots)))

total = 1
for time, dist in games:
	total *= numways(time, dist)

print(total)
print(numways(34908986, 204171312101780))
