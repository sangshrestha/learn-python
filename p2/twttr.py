## Just setting up my twttr
from helper import test

def main():
  user_input = input("Input: ")
  print(twttr(user_input))

def twttr(text):
  text_without_vowels = ""

  for letter in text:
    match letter.lower():
      case "a" | "e" | "i" | "o" | "u":
        pass
      case _:
        text_without_vowels += letter
  
  return text_without_vowels


# Run test
success = test(twttr, ["Twitter", "What's your name?", "CS50"], ["Twttr", "Wht's yr nm?", "CS50"])

# Run main if test was successful
if success:
  main()