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
  if emotion == "good":
    print("That's great to hear!")
  elif emotion == "bad":
    print("I'm sorry to hear that")
  else: 
    print("Oh ok, well I am doing botty today.")
  
  siblings = int(input("How many siblings do you have?"))
  if siblings == "0":
    print("You are an only child!")
  elif siblings > 0:
    print("You are not an only child!")
  year = int(input("What year are you born? "))
  if year >= 1995:
     print("You are apart of generation Z!")
  else:
    print("You are not apart of generation Z. Which means you are older than the age of 26!")
  
    

  animal = input("What is your favorite animal?: ")
  animal_reaction = ["Wow, I love that animal!", "Wow thats a really cool animal. My favorite is a gorrila.","That's awesome!", "Oh wow, my favorite animal is a gorilla!", "How cool!"]
  print(random.choice(animal_reaction))
  animal 
  

if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()



