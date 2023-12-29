## Playback Speed
from helper import test


def main():
    success = test(
        playback,
        [
            "This is CS50",
            "This is our week on functions",
            "Let's implement a function called hello",
        ],
        [
            "This...is...CS50",
            "This...is...our...week...on...functions",
            "Let's...implement...a...function...called...hello",
        ],
    )
    if success:
        user_input = input("Say a sentence: ")
        print(playback(user_input))


def playback(text):
    text_stripped = text.strip()
    return text_stripped.replace(" ", "...")


# WHY IS IT IMPOSSIBLE TO IMPORT SHIT IN PYTHON
main()
