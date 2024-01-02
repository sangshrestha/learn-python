import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    match = re.search(r"^([\d:]{1,5} (?:AM|PM)) to ([\d:]{1,5} (?:AM|PM))$", s)

    if not match:
        raise (ValueError)

    times = []
    for time in match.groups():
        value, meridian = time.split(" ")
        value_split = value.split(":")
        hour = int(value_split[0])
        minute = int(value_split[1]) if len(value_split) == 2 else 0

        if 1 <= hour <= 12 and 0 <= minute <= 59:
            if meridian == "PM":
                hour = hour + 12
            times.append(f"{hour:02d}:{minute:02d}")
        else:
            raise (ValueError)
    return f"{times[0]} to {times[1]}"


if __name__ == "__main__":
    main()
