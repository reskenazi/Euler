def run():
  base = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
  temp = base
  while(not check(temp)): 
    temp += base
  print(temp)

def check(n):
  for i in range(11,21):
    if(n % i != 0):
      return False
  return True