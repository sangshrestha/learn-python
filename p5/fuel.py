def main():
    user_value = input("Fraction: ")
    print(gauge(convert(user_value)))


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


def convert(fraction):
    numerator, denominator = fraction.split("/")
    division = int(numerator) / int(denominator)

    if division <= 1:
        return round(division * 100)
    else:
        raise ValueError("Numerator is bigger than denominator")


if __name__ == "__main__":
    main()
