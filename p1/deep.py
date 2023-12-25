## Deep Thought
from helper import test

def main():
  success = test(deep_thought, ["42", "Forty Two", "forty-two", "50"], ["Yes", "Yes", "Yes", "No"])
  if success:
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ")
    print(deep_thought(user_input))

def deep_thought(text):
  text_lowercase = text.strip().lower()
  
  match text_lowercase:
    case "42" | "forty-two" | "forty two":
      return "Yes"
    case _:
      return "No"

# WHY IS IT IMPOSSIBLE TO IMPORT SHIT IN PYTHON
main()