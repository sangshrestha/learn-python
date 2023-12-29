## Re-requesting a Vanity Plate
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

        if count <= 2 and not char.isalpha():
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


if __name__ == "__main__":
    main()
