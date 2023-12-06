import re

total = 0

def checkLeftRight(start, end, s, currentRow=False):
#  print(f"Testing row {start} to {end} {s}: {s[max(0, start-1):min(len(s)-1, end+1)]}")
  match = re.search(r"[^\.0-9]", s[max(0, start-1):min(len(s)-1, end+1)])
#  print(match)
  return match
#  if start > 0 and re.match(r"[^\.0-9]", s[start-1]):
#    return True
#  if end < len(s) - 2 and re.match(r"[^\.0-9]", s[end+1]):
#    return True
#  if not currentRow and re.match(r"[^\.0-9]", s[start:end]):
#    return True
  return False    

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]
print(f"Total rows: {len(lines)}")
for rownum, l in enumerate(lines):
  print(f"Row {rownum}: {l}")
  for m in re.finditer(r"[0-9]+", l):
    start = m.start()
    end = m.end()
    if rownum > 0 and checkLeftRight(start, end, lines[rownum-1]): # Check row above
      print(f"Adding {int(m.group())} because of previous row")
      total += int(m.group())
      continue
    if checkLeftRight(start, end, l, currentRow=True): # Check this row
      print(f"Adding {int(m.group())} because of current row")
      total += int(m.group())
      continue
    if rownum < len(lines) - 1 and checkLeftRight(start, end, lines[rownum+1]): # Check row below
      print(f"Adding {int(m.group())} because of next row")
      total += int(m.group())
      continue

print(total)
