def run():
  num = [2]
  for i in range(999): #has to be one less
    num = addToSelf(num)
  sum = 0
  for i in range(len(num)):
    sum = sum + int(num[i])
  print(sum)

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