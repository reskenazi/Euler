def run():
  sum = 0
  first = 1
  next = 2
  while(next <= 4000000):
    if next % 2 == 0:
      sum += next
    temp = next
    next += first
    first = temp
  print(sum)