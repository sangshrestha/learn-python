import random


def main():
    level_input = get_level("Level: ")
    score = 0
    tries = 3
    for _ in range(10):
        int_1 = generate_integer(level_input)
        int_2 = generate_integer(level_input)
        sum = int_1 + int_2

        q_prompt = f"{int_1} + {int_2} = "

        for i in range(tries):
            user_ans = int(input(q_prompt))
            if (user_ans == sum):
                score += 1
                break
            else:
                print(f"{q_prompt} {sum}" if i + 1 == tries else "EEE") 
        

    
    print(f"Score: {score}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def get_level(prompt):
    while True:
        level = get_int(prompt)

        if 1 <= level <= 3:
            return level

def generate_integer(level):
    return random.randint(1, 10**level - 1)


if __name__ == "__main__":
    main()