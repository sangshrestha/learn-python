## Home Federal Savings Bank
from helper import test

def main():
    user_input = input("Greeting: ")
    print(bank(user_input))

def bank(greeting):
  greeting_clean = greeting.strip().lower()

  if greeting_clean.startswith("hello"):
     return "$0"
  elif greeting_clean.startswith("h"):
     return "$20"
  else:
     return "$100"
    

# Run test
success = test(bank, ["Hello", "Hello, Newman", "How you doing?", "What's happening?"], ["$0", "$0", "$20", "$100"])

# Run main if test was successful
if success:
  main()