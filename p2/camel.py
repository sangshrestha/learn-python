## camelCase
from helper import test

def main():
  user_input = input("camelCase: ")
  print(snake(user_input))

def snake(text):
  text_return = ""

  for letter in text:
    if letter.isupper():
      text_return += f"_{letter.lower()}"
    else:
      text_return += letter
  
  return text_return

# Run test
success = test(snake, ["name", "firstName", "preferredFirstName"], ["name", "first_name", "preferred_first_name"])

# Run main if test was successful
if success:
  main()