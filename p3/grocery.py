def main():
    inputs = {}
    try:
        while True:
            try:
                item = get_item()
                inputs[item] += 1
            except KeyError:
                inputs[item] = 1
    
    except KeyboardInterrupt:
        inputs_keys = list(inputs.keys())
        inputs_keys.sort()
        for key in inputs_keys:
            print(f"{inputs[key]} {key}")
        


def get_item():
    return input().strip().upper()

  
main()