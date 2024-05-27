from utilities import *

def run():
  sum = 0
  for i in range(10):
    if(isPrime(i)):
      sum += i
  print(sum-1)