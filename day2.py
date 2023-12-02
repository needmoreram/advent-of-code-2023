import re

with open('day2.txt') as f:
    lines = f.readlines()

idsum = 0
powersum = 0
for gameid, game in enumerate(lines):
    blue = max(map(int, re.findall(r'(\d+) blue', game)))
    green = max(map(int, re.findall(r'(\d+) green', game)))
    red = max(map(int, re.findall(r'(\d+) red', game)))
    if red <= 12 and green <= 13 and blue <= 14:
        idsum += gameid + 1
    powersum += (red * blue * green)

print(idsum)
print(powersum)
