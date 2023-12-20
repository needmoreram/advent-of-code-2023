import re

with open('day19.txt') as f:
	lines = f.read().split('\n\n')
	flows = lines[0].splitlines()
	parts = lines[1].splitlines()

wf = dict()
for line in flows:
	label, rules = re.findall(r"(\w+){(.*)}", line)[0]
	rulelist = list()
	for chunk in rules.split(','):
		m = re.search(r"([xmas][<>]\d+):(\w+)", chunk)
		if not m:
			rulelist.append(("True", chunk))
			continue
		rulelist.append((m.group(1), m.group(2)))
	wf[label] = rulelist

def accepted(x, m, a, s):
	label = "in"
	while True:
		for rule, target in wf[label]:
			if eval(rule):
				match target:
					case 'A':
						return True
					case 'R':
						return False
					case _:
						label = target
						break

total = 0
for line in parts:
	x, m, a, s = list(map(int, re.findall(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", line)[0]))
	if accepted(x, m, a, s):
		total += x + m + a + s

print(total)

rules_for_accept = list()
explore = [(list(), "in")]

while len(explore) > 0:
	rulechain, label = explore.pop()
	if label == 'A' or label == 'R':
		if label == 'A':
			rules_for_accept.append(rulechain)
		continue

	for rule, upnext in wf[label]:
		if rule == "True":
			# unconditional jump
			explore.append((rulechain.copy(), upnext))
			# => no more rules to process
			break
		else:
			explore.append((rulechain.copy() + [(rule, "pos")], upnext))
			rulechain.append((rule, "neg"))

def numways(rulechain):
	lowerbound = {
		'x': 1,
		'm': 1,
		'a': 1,
		's': 1,
	}
	upperbound = {
		'x': 4000,
		'm': 4000,
		'a': 4000,
		's': 4000,
	}

	def flip(op):
		return "<=" if op == '>' else '>='

	for rule, cond in rulechain:
		var, op, val = re.findall(r"([xmas])([<>])(\d+)", rule)[0]
		op = flip(op) if cond == "neg" else op
		match op:
			case '<':
				upperbound[var] = min(upperbound[var], int(val) - 1)
			case '<=':
				upperbound[var] = min(upperbound[var], int(val))
			case '>':
				lowerbound[var] = max(lowerbound[var], int(val) + 1)
			case '>=':
				lowerbound[var] = max(lowerbound[var], int(val))

	ways = 1
	ways *= upperbound['x'] - lowerbound['x'] + 1
	ways *= upperbound['m'] - lowerbound['m'] + 1
	ways *= upperbound['a'] - lowerbound['a'] + 1
	ways *= upperbound['s'] - lowerbound['s'] + 1

	return ways

print(sum(map(numways, rules_for_accept)))
