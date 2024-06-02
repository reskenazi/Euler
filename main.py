import importlib

print("Pick problem number: ")
input = input()
problem = importlib.import_module("eulerpackage.euler" + str(input))
problem.run()