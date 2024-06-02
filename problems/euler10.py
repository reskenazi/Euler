from utilities import *

def run():
  print(solve(2000000))

def solve(n):
  sum = 0
  for i in range(n):
    if(isPrime(i)):
      sum += i
  return sum-1