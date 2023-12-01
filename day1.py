import re

with open('day1.txt') as f:
    lines = f.readlines()

total = 0
for s in lines:
    digits = re.findall(r'\d', s)
    total += int(digits[0] + digits[-1])

print(total)

lookup = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

total = 0
for s in lines:
    digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', s)
    total += lookup[digits[0]] * 10 + lookup[digits[-1]]

print(total)
