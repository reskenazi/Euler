from importlib import resources as impresources
from . import inputs

def run():
  arr = []
  inp_file = impresources.files(inputs) / 'euler22.txt'
  with inp_file.open("rt") as f:
    for x in f:
      arr = list(map(str, x.split()))