## Testing my twttr


def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(text):
    text_without_vowels = ""

    for letter in text:
        match letter.lower():
            case "a" | "e" | "i" | "o" | "u":
                pass
            case _:
                text_without_vowels += letter

    return text_without_vowels


if __name__ == "__main__":
    main()
