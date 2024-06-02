def run():
  arr = []
  with open("euler13text.txt", "r") as f:   
    for x in f:
      arr.append(list(map(int, x.split())))
      
  arrayToPrint = []
  for i in range(len(arr)):
      print(arr[i])
      arrayToPrint = addArr(arrayToPrint, arr[i])
  print(arrayToPrint)

#the parameters are 1D arrays, not 2D where every element is a single digit__
def addArr(x, y):
  finalArr = []
  for i in range(len(x)):
    temp = x[len(x)-1] + y[len(y)-1]
    finalArr.insert(0,temp % 10)
    if(temp % 10 != 0):
      finalArr.insert(0,1)
  return finalArr