from importlib import resources as impresources
from . import inputs
from utilities import *

def run():
  arr = []
  inp_file = impresources.files(inputs) / 'euler22.txt'
  with inp_file.open("rt") as f:
    for x in f:
      arr = x.split('","')
  arr[0] = arr[0][1:]
  temp = arr[len(arr)-1]
  temp = temp[0:(len(temp)-1)]
  arr[len(arr)-1] = temp
  arr.sort()
  
  sum = 0
  for x in range(len(arr)):
    sum = sum + (sumOfLetters(arr[x]) * (x+1))
  print(sum)

