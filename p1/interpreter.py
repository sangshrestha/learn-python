## Math Interpreter
from helper import test

def main():
    user_input = input("Expression: ")
    print(interpreter(user_input))

def interpreter(expression):
  parts = expression.split(" ")
  num_1 = float(parts[0])
  num_2 = float(parts[2])
  num_calc = -1

  match parts[1]:
     case "+":
      num_calc = num_1 + num_2
     case "-":
      num_calc = num_1 - num_2
     case "*":
      num_calc = num_1 * num_2
     case "/":
      num_calc = num_1 / num_2

  return round(num_calc, 1)

# Run test
success = test(interpreter, ["1 + 1", "2 - 3", "2 * 2", "50 / 5", "-1 + 100"], [2.0, -1.0, 4.0, 10.0, 99.0])

# Run main if test was successful
if success:
  main()