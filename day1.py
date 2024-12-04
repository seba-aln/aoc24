"""Day 1: Location, location, location
"""

from utils import load_data

data = load_data(1, False)
left, right = [], []
for row in data:
    left.append(int(row.split()[0]))
    right.append(int(row.split()[1]))
left.sort()
right.sort()


result = sum([abs(left[i] - right[i]) for i in range(len(left))])
print(f"Part 1: {result}")

result = sum(left[i] * right.count(left[i]) for i in range(len(left)))
print(f"Part 2: {result}")
