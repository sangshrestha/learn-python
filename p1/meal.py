## Meal Time
from helper import test

def main():
      user_input = input("What time is it? ")
      time_value = convert(user_input)
      print(meal(time_value))

def meal(val):
  if 7 <= val <= 8:
    return "breakfast time"
  elif 12 <= val <= 13: 
    return "lunch time"
  elif 18 <= val <= 19: 
    return "dinner time"
  else:
    return "" 

def convert(time):
    ## check if p.m.
    parts = time.split(" ")
    time_part = parts[0]
    hour, minute = time_part.split(":")
    time_in_decimal = float(hour) + float(minute) / 60
    offset = 12 if parts[-1] == "p.m." else 0
    return round(time_in_decimal + offset, 1)


# Run test
def test_fn(time):
  return meal(convert(time))

success = test(test_fn, ["7:00", "7:30", "12:42", "18:32", "5:00 a.m.", "6:00 p.m."], ["breakfast time", "breakfast time", "lunch time", "dinner time", "", "dinner time"]) 

if __name__  == "__main__" and success:
    main()