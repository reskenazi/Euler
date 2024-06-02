import math

def run():
  a = 1
  b = 2
  t = False
  for i in range(1000):
    for j in range(1000):
      if(pythagorean(a+i,b+j) != -1 and (a + i) + (b + j) + pythagorean(a+i,b+j) == 1000):
        print("a = " + str(a+i))
        print("b = " + str(b+j))
        print((a+i) * (b + j) * int(pythagorean(a+i,b+j)))
        t = True
        break
    if(t):
      break

def pythagorean(a,b):
  temp = math.sqrt(int(math.pow(a,2)) + int(math.pow(b,2)))
  if(temp % 1 > 0):
    return -1
  return temp