# from helper import test


def main():
    for i in [722, 723, 724, 725, 726]:
        print(f"n: {i} - Is prime? {isPrime(i)}")


def isPrime(n):
    if n < 2:
        return False

    for i in range(round(n / 2) + 1)[2:]:
        if n % i == 0:
            return False
    return True


# Run test
## success = test(isPrime, [1,2,3,4,5,6,7,8,9], [False, True, True, False, True, False, True, False, False])

##if success:
main()
