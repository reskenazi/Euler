from utilities import *
def run():
  num = 1
  count = 1
  while(True):
    temp = numDivisors(num)
    if(temp > 500):
      print(num)
      break
    num += count + 1
    count += 1
