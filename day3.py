with open('day3.txt') as f:
    lines = f.read().splitlines()

class Numeric:
    def __init__(self, num):
        self.num = num
        self.marked = False
    def __str__(self):
        return self.num
 
nums = dict()
syms = set()
gears = set()
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
            if ch == '*':
                gears.add((i, j))
            syms.add((i-1, j-1))
            syms.add((i-1, j))
            syms.add((i-1, j+1))
            syms.add((i, j-1))
            syms.add((i, j+1))
            syms.add((i+1, j-1))
            syms.add((i+1, j))
            syms.add((i+1, j+1))

for k in syms:
    if k in nums and nums[k].marked == False:
        total += int(nums[k].num)
        nums[k].marked = True

print(total)
