from utilities import *

def run():
  count = 0
  num = 1
  while(count < 10001):
    num += 1
    if(isPrime(num)):
      count += 1

  print(num)