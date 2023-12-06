with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

games = {}
for l in lines:
  game, setstxt = l.split(': ')
  game = int(game.split(' ')[-1])
  setstxt = setstxt.split('; ')
  sets = []
  for s in setstxt:
    setinfo = {'red':0,'green':0,'blue':0}
    colors = s.split(', ')
    for i in colors:
      n, *c = i.split(' ')
      print(f"Game {game}: {c}")
      setinfo[c[0]] = int(n)      
    sets.append(setinfo)
  games[game] = sets

startinginfo = {'red':12,'green':13,'blue':14}

total = 0
for g,sets in games.items():
  yes = True
  for s in sets:
    if s['red'] > startinginfo['red'] or s['green'] > startinginfo['green'] or s['blue'] > startinginfo['blue']:
      yes = False
      break
  if yes:
    total += g

print(total)
