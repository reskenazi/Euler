d = 20

def run():
  cache = []
  for i in range (d+1):
    cache.append([])
    for j in range (d+1):
      cache[i].append(-1)
  num = recurse(0,0, cache)
  print(num)

def recurse(x, y, cache):
  if(x == d and y == d):
    return 1
    
  if(cache[x][y] != -1):
    return cache[x][y]
    
  paths = 0
  
  if(x < d):
    paths = paths + recurse(x+1, y, cache)
  if(y < d):
    paths = paths + recurse(x, y+1, cache)

  cache[x][y] = paths
  
  return paths