from utilities import *
def run():
  print(solve(20))

def solve(n):
  base = 1
  
  for i in range (1,n+1):
    if(isPrime(i)):
      base = base * i
  
  temp = base
  while(not check(temp)): 
    temp += base
    
  return temp

def check(n):
  for i in range(11,21):
    if(n % i != 0):
      return False
  return True