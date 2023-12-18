import re
from functools import reduce

with open('day15.txt') as f:
	lines = f.read()[:-1].split(',')

def myhash(a, b):
	return ((a + b) * 17) % 256

total = 0
for word in lines:
	word = map(ord, ['\0'] + list(word))
	total += reduce(myhash, word)

print(total)

boxes = dict()
for word in lines:
	m = re.match(r"(\w+)([=-])(\d?)", word)
	label = m.group(1)
	operator = m.group(2)

	h = reduce(myhash, map(ord, ['\0'] + list(label)))
	if operator == "-":
		if h in boxes and label in boxes[h]:
			boxes[h].pop(label)
	elif operator == "=":
		if h not in boxes:
			boxes[h] = dict()
		boxes[h][label] = int(m.group(3))

total = 0
for boxnum in boxes:
	for slotnum, label in enumerate(boxes[boxnum].keys()):
		total += (boxnum + 1) * (slotnum + 1) * boxes[boxnum][label]

print(total)