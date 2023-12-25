## Template
from helper import test

def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

def is_valid(s):
  count = 0
  num_found = False

  for char in s:
    count += 1

    if count > 6:
      return False
    
    if count <=2 and not char.isalpha():
      return False

    if char.isdigit():
      if char == "0" and not num_found:
        return False
      num_found = True

    elif char.isalpha():
      if num_found:
        return False
    
    else:
      return False
  
  return True if count >= 2 else False

# Run test
success = test(is_valid, ["CS50", "CS05", "CS50P", "PI3.14", "H", "OUTATIME"], [True, False, False, False, False, False])

# Run main if test was successful
if success:
  main()