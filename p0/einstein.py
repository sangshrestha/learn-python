## Einstein
from helper import test


def main():
    success = test(
        energy,
        [1, 14, 50],
        [90000000000000000, 1260000000000000000, 4500000000000000000],
    )
    if success:
        user_input = input("Enter mass: ")
        print(energy(user_input))


def energy(mass):
    speed_of_light = 300000000
    mass_in_int = int(mass)
    energy = mass_in_int * speed_of_light**2
    return energy


# WHY IS IT IMPOSSIBLE TO IMPORT SHIT IN PYTHON
main()
