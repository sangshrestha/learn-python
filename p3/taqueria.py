menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        total = total + get_cost("Item: ")
        print(f"Total: ${total:0.2f}")

def get_cost(prompt):
    while True:
        item = input(prompt).strip().title()

        try:
            cost = menu[item]
        except KeyError:
            print("Not in the menu")
        else:
            return cost

try:
    main()
except KeyboardInterrupt:
    pass