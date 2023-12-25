## Nutrition Facts
from helper import test

fruits = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90, "honeydew melon": 50, 
          "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50, 
          "plums": 70, "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80 }

def main():
  user_input = get_fruit()
  print(f"Calories: {calories(user_input)}")

def get_fruit():
  while True:
    fruit_input = input("Fruit: ")
    for fruit in fruits: 
      if fruit == fruit_input.lower():
        return fruit_input


def calories(key):
  return fruits[key.lower()]

# Run test
success = test(calories, ["Apple", "Avocado", "Sweet Cherries"], [130, 50, 100])

# Run main if test was successful
if success:
  main()