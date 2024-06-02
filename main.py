import importlib

print("Pick problem number: ")
input = input()

try:
  problem = importlib.import_module("problems.euler" + str(input))
  problem.run()
except ModuleNotFoundError:
  print("Problem number " + str(input) + " does not exist")