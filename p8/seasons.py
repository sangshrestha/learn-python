from datetime import date
import math
import sys

count = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tenth = [
    "zero",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

powers_of_1000 = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
]


class Bday:
    def __init__(self, birthdate):
        try:
            self.year, self.month, self.day = birthdate.split("-")
        except ValueError:
            sys.exit()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    @classmethod
    def get(cls):
        date = input("Date of Birth: ").strip()
        return cls(date)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        try:
            self._year = int(year)
        except ValueError:
            sys.exit()

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        try:
            if 1 <= int(month) <= 12:
                self._month = int(month)
            else:
                raise ValueError
        except ValueError:
            sys.exit()

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        try:
            if 1 <= int(day) <= 31:
                self._day = int(day)
            else:
                raise ValueError
        except ValueError:
            sys.exit()


def main():
    bday = Bday.get()
    diff = date.today() - date(bday.year, bday.month, bday.day)
    diff_split = diff.days * 24 * 60
    print(f"{say_num(diff_split)} minutes")


def say_hundreds(n):
    string = ""

    if n == 0:
        string += ""
    else:
        hundred_digit = math.floor(n / 100)
        if hundred_digit != 0:
            string += f"{count[hundred_digit]} hundred "

        ten_num = n - hundred_digit * 100

        if 0 < ten_num < 20:
            string += f"{count[ten_num]}"
        else:
            ten_digit = math.floor(ten_num / 10)
            joiner = ""

            if ten_digit != 0:
                joiner = "-"
                string += f"{tenth[ten_digit]}"

            one_digit = ten_num - ten_digit * 10

            if one_digit != 0:
                string += f"{joiner}{count[one_digit] }"

    return string.strip()


def say_num(n):
    if n == 0:
        return "Zero"

    n_split = f"{n:,}".split(",")
    power = len(n_split)
    string = []

    for i, num in enumerate(n_split):
        if int(num) != 0:
            local_string = ""
            local_string += say_hundreds(int(num))

            if i + 1 < power:
                local_string += f" {powers_of_1000[power - i - 1]}"

            string.append(local_string)

    return ", ".join(string).capitalize()


if __name__ == "__main__":
    main()
