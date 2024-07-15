import math

def run():
  amicable = set()
  for i in range(2, 10001):
    num1 = calcSumOfDivisors(i)
    if calcSumOfDivisors(num1) == i and num1 != i:
      print(i, num1)
      amicable.add(i)
      amicable.add(num1)
  print(amicable)
  print(sum(amicable))

def calcSumOfDivisors(num):
  sum = 1
  for i in range(2,num):
    if(num % i == 0):
      sum = sum + i
  """
  sqrt = int(math.sqrt(num))
  for i in range(2, sqrt):
    if num % i == 0:
      sum = sum + i
      sum = sum + (num // i)
  if(num % sqrt == 0):
    sum = sum + sqrt
  """
  return sum
