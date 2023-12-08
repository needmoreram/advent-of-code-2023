from collections import Counter
from functools import cmp_to_key

joker_enabled = False

with open('day7.txt') as f:
	lines = f.read().split()
	it = iter(lines)
	hands = list(zip(it, it))

def valueof(hand):
	counts = Counter(hand)
	jacks = counts.pop('J') if joker_enabled and 'J' in counts else 0
	top = counts.most_common(2)
	values = {
		5: 10,
		4: 9,
		3: 7,
		2: 5,
		1: 4,
	}
	if len(top) < 2:
		return values[5]
	return values[top[0][1] + jacks] + (1 if top[1][1] == 2 else 0)


order = {
	'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
	'7': 7,	'8': 8, '9': 9, 'T': 10, 'J': 11,
	'Q': 12, 'K': 13, 'A': 14,
}

def mycmp(a, b):
	order['J'] = 1 if joker_enabled else 11
	va = valueof(a[0])
	vb = valueof(b[0])
	if va != vb:
		return 1 if va > vb else -1
	for i in range(5):
		if order[a[0][i]] == order[b[0][i]]:
			continue
		return 1 if order[a[0][i]] > order[b[0][i]] else -1
	assert False


def get_total(hands):
	total = 0
	hands = sorted(hands, key=cmp_to_key(mycmp))
	for i, hand in enumerate(hands):
		x, bid = hand
		total += (int(bid) * (i + 1))
	return total

print(get_total(hands.copy()))
joker_enabled = True
print(get_total(hands))

