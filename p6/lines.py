import sys


if len(sys.argv) != 2:
    print("Too few cmd-line args")
    sys.exit()

if not sys.argv[1].endswith(".py"):
    print("Not a .py file")
    sys.exit()


# read py file
try:
    with open(sys.argv[1]) as file:
        count = 0
        for line in file:
            line_strip = line.strip()
            if len(line_strip) == 0 or line_strip.startswith("#"):
                pass
            else:
                count += 1
        print(count)
except UnicodeDecodeError:
    print("Unicode error")
    sys.exit()
except FileNotFoundError:
    print("404")
    sys.exit()
