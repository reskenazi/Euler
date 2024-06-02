import math
from utilities import *

def run():
   print(solve(600851475143))

def solve(target):
  for i in range(int(math.sqrt(target))-1, 1, -2):
    if(isPrime(i) and target % i == 0):
      return i

  raise ValueError("not found")