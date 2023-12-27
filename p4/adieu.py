def main():
    names = []
    try:
        while True:
            names.append(get_name("Name: "))

    
    except KeyboardInterrupt:
        print("")
        print("Adiew, adieu, to", join(names))
        
def join(array):
    count = len(array)
    j_string = ""
    for i in range(count):
        if i == 0:
            j_string += array[i]
        elif i == count - 1:
            j_string += f" and {array[i]}"
        else:
            j_string += f", {array[i]},"
    return j_string

def get_name(prompt):
    return input(prompt).strip().capitalize()

  
main()