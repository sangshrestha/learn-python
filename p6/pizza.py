import sys
import csv
from tabulate import tabulate


if len(sys.argv) != 2:
    print("Too few cmd-line args")
    sys.exit()

if not sys.argv[1].endswith(".csv"):
    print("Not a .csv file")
    sys.exit()


try:
    with open(sys.argv[1]) as file:
        list = []
        reader = csv.reader(file)
        for row in reader:
            list.append(row)
        print(tabulate(list, tablefmt="grid"))

except UnicodeDecodeError:
    print("Unicode error")
    sys.exit()
except FileNotFoundError:
    print("404")
    sys.exit()
