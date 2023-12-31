import sys
import csv


if len(sys.argv) != 3:
    print("Too few cmd-line args")
    sys.exit()

if not sys.argv[1].endswith(".csv"):
    print("Not a .csv file")
    sys.exit()

new_dict = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for student in reader:
            last, first = student["name"].split(",")
            update_student = {
                "last": last.strip(),
                "first": first.strip(),
                "house": student["house"],
            }
            new_dict.append(update_student)
except UnicodeDecodeError:
    print("Unicode error")
    sys.exit()
except FileNotFoundError:
    print("404")
    sys.exit()

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(
        file, fieldnames=["last", "first", "house"], lineterminator="\n"
    )
    writer.writeheader()
    for student in new_dict:
        writer.writerow(student)
