import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for capture in matches.groups():
            if not 0 <= int(capture) <= 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
