import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    match = re.search(r"src=['\"]https?://(?:www.)?youtube.com/embed/(\w+)['\"]", s)
    return f"https://youtu.be/{match.group(1)}" if match else None


if __name__ == "__main__":
    main()
