import math

def run():
  target = 600851475143
  for i in range(int(math.sqrt(target))-1, 1, -2):
    if(isPrime(i) and target % i == 0):
      print(i)
      break
  
def isPrime(n):
  if(n % 2 == 0):
    return False
  for i in range(3, int(math.sqrt(n)), 2):
    if(n % i == 0):
      return False
  return True