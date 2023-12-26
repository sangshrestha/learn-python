months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    old_date = get_date()
    new_date = f"{old_date[2]}-{old_date[1]:02d}-{old_date[0]:02d}"
    print(new_date)
    return new_date

def check_date(date):
    month, day, year = date
    return 1 <= month <= 12 and 1<= day <= 31 and year > 0

def intMap(n):
    return int(n)

def get_date():
    while True:
        user_input = input("Date: ").strip()

        # xx/xx/xxxx format
        mdy_split = user_input.split("/")

        try: 
            if len(mdy_split) == 3:
                user_date = list(map(intMap, mdy_split))
            else:
                comma_split = user_input.split(",")
                month, day = comma_split[0].split(" ")
                user_date = [months.index(month.capitalize()) + 1, int(day), int(comma_split[1])]
            
            if check_date(user_date):
                return user_date
        except ValueError:
            pass


main()