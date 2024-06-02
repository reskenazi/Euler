from importlib import resources as impresources
from . import inputs

def run():
  arr = []
  inp_file = impresources.files(inputs) / 'euler13.txt'
  with inp_file.open("rt") as f:
    for x in f:
      assert len(x.strip()) == 50
      arr.append(x.strip())

  result = []
  carry = 0
  for i in range(49, -1, -1):
    sum = carry
    for j in range(len(arr)):
      sum += int(arr[j][i]) 
    result.insert(0, str(sum % 10))
    carry = sum // 10
  
  result.insert(0,str(carry))
  print("".join(result))
  