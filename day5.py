with open('day5.txt') as f:
    lines = f.read() + " willbeignored"
    lines = lines.split("map:")

sections = [x.split()[:-1] for x in lines]
sections[0] = sections[0][1:]
sections = [list(map(int, x)) for x in sections]
seeds = sections[0]

def getnext(nextmap, v):
    for i in range(0, len(nextmap), 3):
        dst = nextmap[i]
        src = nextmap[i+1]
        n = nextmap[i+2]
        if v >= src and v < src + n:
            return dst+v-src

    return v


minloc = None
for v in seeds:
    for i in range(1, len(sections)):
        v = getnext(sections[i], v)
    if not minloc or v < minloc:
        minloc = v

print(minloc)
