def run():
  print(solve(4000000))

def solve(lim):
  sum = 0
  first = 1
  next = 2
  while(next <= lim):
    if next % 2 == 0:
      sum += next
    temp = next
    next += first
    first = temp
  return sum