import math

with open('day8.txt') as f:
	lines = f.read().splitlines()

instr = lines[0]
network = dict()

for line in lines[2:]:
	line = line.split()
	network[line[0]] = [line[2][1:-1], line[3][:-1]]

last_char_only = False

def numsteps(pos):
	i = 0
	while (not last_char_only and pos != 'ZZZ') or (last_char_only and pos[-1] != 'Z'):
		pos = network[pos][0] if instr[i % len(instr)] == 'L' else network[pos][1]
		i += 1
	return i

print(numsteps('AAA'))

pos = list(filter(lambda x: x[-1] == 'A', network.keys()))
last_char_only = True
print(math.lcm(*list(map(numsteps, pos))))
