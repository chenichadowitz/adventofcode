#!/usr/bin/env python3
import re

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

total = 0
m = {'one': 1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
for l in lines:
#  digits = re.findall(r'([0-9]|one|two|three|four|five|six|seven|eight|nine)', l)
  match = re.search(r'([0-9]|one|two|three|four|five|six|seven|eight|nine)', l)
  rmatch = re.search(r'([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', l[::-1])
  if not match or not rmatch:
    raise RuntimeError(f"No results for {l}")
  if len(match.group()) > 1:
    first = m[match.group()]
  else:
    first = match.group()
  if len(rmatch.group()) > 1:
    last = m[rmatch.group()[::-1]]
  else:
    last = rmatch.group()[::-1]
  num = f"{first}{last}"
  print(f"{num}: {match.group()}, {rmatch.group()[::-1]}: {l}")
  numint = int(num)
  total += numint

print(total)
