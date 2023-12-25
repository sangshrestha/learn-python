from helper import test

def main():
  success = test(dollars_to_float, ["$50.00", "$100.00", "$15.00"], [50.00, 100.00, 15.00]) & test(percent_to_float, ["15%", "18%", "25%"], [0.15, 0.18, 0.25])
  if success:
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
  return round(float(d.split("$")[1]),2)


def percent_to_float(p):
 return round(float(p.split("%")[0])/100,2)


main()