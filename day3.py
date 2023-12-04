with open('day3.txt') as f:
    lines = f.read().splitlines()

class Numeric:
    def __init__(self, num):
        self.num = num
        self.counted = False
    def __str__(self):
        return self.num
 
nums = dict()
syms = set()
gears = []
total = 0

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch.isdigit():
            if (i, j-1) in nums:
                t = nums[(i, j-1)]
                t.num += ch
                nums[(i, j)] = t
            else:
                nums[(i, j)] = Numeric(ch)
        elif ch == '.':
            continue
        else:
            t = set()
            t.add((i-1, j-1))
            t.add((i-1, j))
            t.add((i-1, j+1))
            t.add((i, j-1))
            t.add((i, j+1))
            t.add((i+1, j-1))
            t.add((i+1, j))
            t.add((i+1, j+1))
            syms = syms.union(t)
            if ch == '*':
                gears.append(t)

for k in syms:
    if k in nums and not nums[k].counted:
        total += int(nums[k].num)
        nums[k].counted = True

print(total)

total = 0
for neighbors in gears:
    ids = set()
    for n in neighbors:
        if n in nums:
            ids.add(nums[n])
    if len(ids) == 2:
        t = 1
        for x in ids:
            t *= int(x.num) 
        total += t

print(total)
