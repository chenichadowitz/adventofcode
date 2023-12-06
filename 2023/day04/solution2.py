import re

with open('test.txt', 'r') as f:
  cards = []
  for l in f.readlines():
    winning, *mynums = l.strip().split(': ')[1].split(' | ')
    winning = sorted([int(w) for w in re.findall(r"[0-9]+", winning)])
    mynums = sorted([int(n) for n in re.findall(r"[0-9]+", mynums[0])])
    print(f"Winning: {winning}, my nums: {mynums}")
    winning = set(winning)
    mynums = set(mynums)
    matches = winning.intersection(mynums)
    print(f"Matches: {matches}")
    if len(matches) > 0:
      total += 2**(len(matches)-1)

print(total)
