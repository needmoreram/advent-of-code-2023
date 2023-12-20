from itertools import combinations
import numpy as np

with open('day11.txt') as f:
	lines = f.read().splitlines()
	universe = np.array([list(x) for x in lines])

empty_cols = np.where(np.all(universe == '.', axis=0))[0]
empty_rows = np.where(np.all(universe == '.', axis=1))[0]
galaxies = zip(*np.where(universe == '#'))

def calc(n):
	total = 0
	for a, b in combinations(galaxies, r=2):
		ax = min(a[0], b[0])
		bx = max(a[0], b[0])
		ay = min(a[1], b[1])
		by = max(a[1], b[1])
		dist = (bx - ax) + (by - ay)
		rcrossings = len([x for x in empty_rows if ax < x < bx])
		ccrossings = len([y for y in empty_cols if ay < y < by])
		total += dist + n * (rcrossings + ccrossings)
	return total

print(calc(1000000-1))
