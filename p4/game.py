from random import randint
import sys

def main():
    level = get_int("Level: ")
    target = randint(1, level)
    while True:
        guess = get_int("Guess: ")

        if guess > target:
            print("Too large!")
        elif guess < target:
            print("Too small!")
        else:
            print("Just right!")
            sys.exit()

def get_int(prompt):
    while True:
        try:
            user_int = int(input(prompt))
        except ValueError:
            pass
        else:
            if user_int > 0:
                return user_int
try:
    main()
except KeyboardInterrupt:
    pass