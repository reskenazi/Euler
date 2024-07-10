from utilities import *

def run():
  num = [2]
  for i in range(3, 101):
    num = multiply(num, i)
  print(num)
  sum = 0
  for i in range(len(num)):
    sum = sum + num[i]
  print(sum)
