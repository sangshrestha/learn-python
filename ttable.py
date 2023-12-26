from tabulate import tabulate

args = ["P", "Q"]
premises = ["(Pn¬Q)u(¬PnQ)"]

# 8 ["(PnQ)u(¬Pn¬Q)", "¬PuQ", "(Pu¬Q)n(Qu¬P)", "¬(PuQ)", "(QnP)u¬P"]

count = len(args)


def main():
    table = [args + premises]
    for row in range(2**count):
        binary_string = format(row ,"b").zfill(count)
        lookup = {}

        for i in range(count):
            lookup[args[i]] = binary_string[i] == "1"

        for premise in premises:
            lookup[premise] = eval(trans(premise))

        table.append(list(lookup.values()))

    print(tabulate(table))

def trans(string):
    eval_string = ""

    for i in string:
        if i == "(" or i == ")":
            eval_string += i 
        elif i == "u":
            eval_string += " or "
        elif i == "n":
            eval_string += " and "
        elif i == "¬":
            eval_string += " not "
        elif i.isalpha():
            eval_string += f" lookup['{i}'] "
    
    return eval_string

main()