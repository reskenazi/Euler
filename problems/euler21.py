import math

def run():
  amicable = set()
  for i in range(2, 10000):
    num1 = calcSumOfDivisors(i)
    if calcSumOfDivisors(num1) == i:
      print(i, num1)
      amicable.add(i)
      amicable.add(num1)

  print(amicable)
  print(sum(amicable))

def calcSumOfDivisors(num):
  sum = 1
  for i in range(2, math.floor(math.sqrt(num))):
    if num % i == 0:
      sum = sum + i
      sum = sum + (num // i)
  return sum
