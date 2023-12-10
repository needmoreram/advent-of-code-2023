with open('day9.txt') as f:
	lines = f.read().splitlines()
	lines = [x.split() for x in lines]

def getnext(seq):
	new_seq = []
	keep_going = False
	for i in range(1, len(seq)):
		diff = int(seq[i]) - int(seq[i-1])
		if diff != 0:
			keep_going = True
		new_seq.append(diff)
	return int(seq[-1]) + (getnext(new_seq) if keep_going else 0)

def getprev(seq):
	new_seq = []
	keep_going = False
	for i in range(1, len(seq)):
		diff = int(seq[i]) - int(seq[i-1])
		if diff != 0:
			keep_going = True
		new_seq.append(diff)
	return int(seq[0]) - (getprev(new_seq) if keep_going else 0)

print(sum(map(getnext, lines)))
print(sum(map(getprev, lines)))
