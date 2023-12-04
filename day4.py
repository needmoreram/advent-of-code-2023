import numpy as np

with open('day4.txt') as f:
	lines = f.read().splitlines()

def inc(x):
	return x + 1

total = 0
counts = np.ones([len(lines)])

for i, card in enumerate(lines):
	s = card.split('|')
	set_a = set(s[0].split()[2:])
	set_b = set(s[1].split())
	n = len(set_a.intersection(set_b))
	total += pow(2,n-1) if n > 0 else 0
	counts[i+1:i+n+1] += counts[i]

print(total)
print(int(sum(counts)))
