from importlib import resources as impresources
from . import inputs

def run():
  number = ""
  inp_file = impresources.files(inputs) / 'euler8.txt'
  with inp_file.open("rt") as f:
    for x in f:
      number += x.strip()
  assert len(number) == 1000
  largest = 1
  for i in range(987):
    if "0" not in number[i:i+13]:
      temp = 1
      for j in range(13):
        temp *= int(number[i+j:i+j+1])
      if(temp > largest):
        largest = temp
  print(largest)