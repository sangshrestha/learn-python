## Template used for most of the problems
from helper import test


def main():
    user_input = input("")
    print(fn(user_input))


def fn():
    return


# Run test
success = test(fn, ["", "", ""], ["", "", ""])

# Run main if test was successful
if success:
    main()
