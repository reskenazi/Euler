def run():
  cache = {
    1 : 1
  }
  largest = 1
  for i in range(2,1000000):
    count = 1
    temp = i
    while(temp != 1):
      if(temp % 2 == 0):
        temp /= 2
      elif(temp % 2 == 1):
        temp = 3*temp + 1
      if temp in cache:
        count += cache[temp]
        break
      else:
        count += 1
        
    cache[i] = count
    if(count > largest):
      largest = count
      
  for x in cache.keys():
    if(cache[x] == largest):
      print(x)