import re

total = 0

def checkRow(start, end, s):
  print(f"Testing row {s} from {start} to {end}")
  nums = []
  for m in re.finditer(r"[0-9]+", s):
    print(m)
    if start > 0 and m.end() >= start and m.end() <= end:
      print(f"found overlap with start {m}")
      nums.append(int(m.group()))
    elif end < len(s) - 1 and m.start() <= end and m.end() >= end:
      print(f"found overlap with end {m}")
      nums.append(int(m.group()))
  return nums

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]
print(f"Total rows: {len(lines)}")
for rownum, l in enumerate(lines):
  print(f"Row {rownum}: {l}")
  for m in re.finditer(r"\*", l):
    nums = []
    start = m.start()
    end = m.end()
    if rownum > 0: # Check row above
      nums.extend(checkRow(start, end, lines[rownum-1]))
    nums.extend(checkRow(start, end, l)) # Check this row
    if rownum < len(lines) - 1: # Check row below
      nums.extend(checkRow(start, end, lines[rownum+1]))
    print(f"Nums: {nums}")
    if len(nums) == 2:
      total += nums[0]*nums[1]
print(total)
