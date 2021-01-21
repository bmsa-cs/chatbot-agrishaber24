"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util
import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v tests.py"
  print(command)
  os.system(command)

def main():
  name = input("What is your name? ")
  print("Hello there " + name + " my name is chatbot!")

  color = input("What is your favorite color? ")
  if color == "Blue":
    print(" You have the most popular favorote color!")
  else:
    print("Blue is the most popular favorite color, but " + color + " is my favorite too.")
  emotion = input("How are you feeling today " + name +"?")


  name = input("What is your name? ")
  print("Hello there " + name + " my name is chatbot!")





  color = input("What is your favorite color? ")
  if color == "Blue":
    print(" You have the most popular favorote color!")
  else:
    print("Blue is the most popular favorite color, but " + color + " is my favorite too.")


  emotion = input("How are you doing today " + name +"?")

if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()
