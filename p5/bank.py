## Back to the Bank
def main():
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")


def value(greeting):
    greeting_clean = greeting.strip().lower()

    if greeting_clean.startswith("hello"):
        return 0
    elif greeting_clean.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
