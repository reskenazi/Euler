import math

def isPrime(n):
  if(n == 2):
    return True
  if(n % 2 == 0):
    return False 
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if(n % i == 0):
      return False
  return True

def triangularNumber(n):
  sum = 0
  for i in range(n+1):
    sum += i
  return sum

def numDivisors(n):
  temp = 2
  for i in range(2,int(math.sqrt(n))):
    if(n % i == 0):
      temp += 1
  return temp * 2