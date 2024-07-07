from importlib import resources as impresources
from . import inputs

def run():
  arr = []
  inp_file = impresources.files(inputs) / 'euler67.txt'
  with inp_file.open("rt") as f:
    for x in f:
      result = list(map(int, x.split()))
      arr.append(result)

  cache = []
  for i in range(1, len(arr)+1):
    temp = [-1] * i
    cache.append(temp)

  num = recurse(arr, 0, 0, cache)
  print(num)

def recurse(arr, x, y, cache):
  if(y == len(arr)-1):
    return arr[y][x]

  if(cache[y][x] != -1):
    return cache[y][x]

  leftPath = arr[y][x] + recurse(arr, x, y+1, cache)

  rightPath = arr[y][x] + recurse(arr, x+1, y+1, cache)

  cache[y][x] = max(leftPath,rightPath)

  return cache[y][x]
