import math

def run():
  largest = 0
  for i in range(999, 99, -1):
    for j in range(999, 99, -1):
      if(i * j < largest):
        break
      if(isPalindrome(i * j)):
        largest =  i * j
  print(largest)
  
def isPalindrome(n):
  digits = int(math.log(n,10))
  while(digits >= 1):
    back = n % 10
    n = n // 10
    digits -= 1
    temp = int(math.pow(10, digits))
    front = n // temp
    if(front != back):
      return False
    n = n - (front * temp)
    digits -= 1
  return True