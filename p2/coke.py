## Coke Machine

def main():
  coke()

def coke():
  cost = 50

  while True:
    x = int(input("Insert Coin: "))

    match x:
      case 5 | 10 | 25:
        cost = cost - x

        if cost <= 0:
          print(f"Change Owed: {cost * -1}")
          return cost
        else:
          print(f"Amount Due: {cost}")


main()