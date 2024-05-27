def isPrime(n):
  if(n % 2 == 0):
    return False
  for i in range(3, int(math.sqrt(n)), 2):
    if(n % i == 0):
      return False
  return True