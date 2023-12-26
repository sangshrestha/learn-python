def main():
    value = get_percentage("Fraction: ")
    if value >= 99:
        print("F")
    elif value <= 1:
        print("E")
    else:
        print(f"{value}%") 

def get_percentage(prompt):
    while True:
        try:
            numerator, denominator = input(prompt).split("/")
            division = int(numerator)/int(denominator)
        except ZeroDivisionError:
            print("Can't divide by 0")
        except ValueError:
            print("Type a valid fraction")
        else: 
            if division <= 1:
                return round(division * 100)
            print("Type a valid fraction")

main()