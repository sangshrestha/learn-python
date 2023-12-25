## Making Faces
from helper import test

def main():
  success = test(faces, ["Hello :)", "Goodbye :(", "Hello :) Goodbye :("], ["Hello 🙂", "Goodbye 🙁", "Hello 🙂 Goodbye 🙁"])
  if success:
    user_input = input("Say a sentence: ")
    print(faces(user_input))

def faces(text):
  text_stripped = text.strip()
  text_to_emoji = text_stripped.replace(":)", "🙂").replace(":(", "🙁")
  return text_to_emoji

# WHY IS IT IMPOSSIBLE TO IMPORT SHIT IN PYTHON
main()