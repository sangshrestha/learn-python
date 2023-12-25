## Indoor Voice
from helper import test

def main():
  success = test(silence, ["HELLO", "THIS IS CS50", "50"], ["hello", "this is cs50", "50"])
  if success:
    user_input = input("SHOUT IN ALL CAPS: ")
    print(silence(user_input))

def silence(text):
  text_lowercase = text.strip().lower()
  return text_lowercase

# WHY IS IT IMPOSSIBLE TO IMPORT SHIT IN PYTHON
main()