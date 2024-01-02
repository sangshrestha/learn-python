from validator_collection import checkers


def main():
    print(check_email(input("Email: ").strip()))


def check_email(s):
    return checkers.is_email(s)


if __name__ == "__main__":
    main()
