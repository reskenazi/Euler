from utilities import *

def run():
  print(solve(10000))

def solve(n):
  count = 0
  num = 1
  while(count <= n):
    num += 1
    if(isPrime(num)):
      count += 1
  return num