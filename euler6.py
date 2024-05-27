import math

def run():
  sumsquare = 0
  for i in range(101):
    sumsquare += math.pow(i,2)
  squaresum = 0
  for i in range(101):
    squaresum += i
  squaresum = math.pow(squaresum,2)
  print(squaresum - sumsquare)