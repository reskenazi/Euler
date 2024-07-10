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

def addToSelf(x):
  result = []
  carry = 0
  for i in range(len(x)-1, -1, -1):
    sum = int(x[i]) + int(x[i])
    result.insert(0, str((sum % 10) + carry))
    carry = sum // 10
  if(carry != 0):
    result.insert(0, str(carry))
  return result


def multiply(num, x):
  if(x > 9):
    temp1 = multiply(num, x // 10)
    temp1.append(0)
    temp2 = multiply(num, x % 10)
    return addArrays(temp2, temp1)
  else:
    result = []
    carry = 0
    product = num[len(num)-1] * x
    carry = product // 10
    result.insert(0,product%10)
    for i in range(len(num)-2, -1, -1):
      product = num[i] * x + carry
      carry = product // 10
      result.insert(0, product%10)
    if(carry > 0):
      result.insert(0, carry)
    return result


def addArrays(arr1, arr2):
  result = []
  carry = 0
  difference = len(arr1) - len(arr2)

  if(difference == 0):
      for i in range(len(arr1)-1, -1, -1):
        sum = arr1[i] + arr2[i]
        result.insert(0, sum%10 + carry)
        carry = sum // 10
      if(carry != 0):
        result.insert(0, carry)
      return result

  elif(difference > 0):
    for i in range(len(arr2)-1, -1, -1):
      sum = arr1[i+difference] + arr2[i]
      result.insert(0, sum%10 + carry)
      carry = sum // 10
    if(carry != 0):
      result.insert(0, carry + arr1[difference-1])
      difference = difference-1
    while(difference > 0):
      result.insert(0, arr1[difference-1])
      difference = difference-1
    return result

  elif(difference < 0):
    return addArrays(arr2, arr1)