import numpy as np

with open('day10.txt') as f:
	lines = f.read().splitlines()
	lines = np.array([list(x) for x in lines])
	lines = np.pad(lines, pad_width=1)

start = list(zip(*np.where(lines == 'S')))[0]
visited = set()
visited.add(start)

match lines[start[0]-1, start[1]]:
	case '|' | '7' | 'F':
		pos = (start[0]-1, start[1])
match lines[start[0]][start[1]-1]:
	case '-' | 'L' | 'F':
		pos = (start[0], start[1]-1)
match lines[start[0]][start[1]+1]:
	case '-' | 'J' | '7':
		pos = (start[0], start[1]+1)
match lines[start[0]+1][start[1]]:
	case '|' | 'L' | 'J':
		pos = (start[0]+1, start[1])

def getnext(pos):
	i, j = pos
	match lines[i][j]:
		case '|':
			return (i-1, j), (i+1, j)
		case '-':
			return (i, j-1), (i, j+1)
		case 'L':
			return (i-1, j), (i, j+1)
		case 'J':
			return (i-1, j), (i, j-1)
		case '7':
			return (i, j-1), (i+1, j)
		case 'F':
			return (i, j+1), (i+1, j)
		case _:
			assert False

steps = 0
while pos != start:
	visited.add(pos)
	steps += 1
	a, b = getnext(pos)
	pos = a if lines[a] != '0' and a not in visited else b

print((steps + 1) // 2)