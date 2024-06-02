def run():
  arr = []
  with open("euler11text.txt", "r") as f:   
    for x in f:
      arr.append(list(map(int, x.split())))
  largest = 0 
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if(j < len(arr[i])-3):
        temp = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
        
      if(temp > largest):
        largest = temp
      if(i < len(arr)-3):
        temp = arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j]
        
        if(temp > largest):
          largest = temp
      if(i < len(arr)-3 and j < len(arr[i])-3):
        temp = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
        
        if(temp > largest):
          largest = temp
      if((i-3) >= 0 and j < len(arr[i])-3):
        temp = arr[i][j] * arr[i-1][j+1] * arr[i-2][j+2] * arr[i-3][j+3]
        
        if(temp > largest):
          largest = temp

  print(largest)
  