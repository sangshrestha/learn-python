import sys
from random import choice
from pyfiglet import Figlet, FigletFont


if len(sys.argv) == 1:
    user_font = choice(FigletFont.getFonts())
elif len(sys.argv) == 3:
    if sys.argv[2] == "-f" or sys.argv[2] == "--font":
         user_font = sys.argv[-1]
    else:
        sys.exit()

try: 
    figlet = Figlet(font=user_font)
except:
    print("Not valid font")
else:
    user_string = input("Input: ")
    print(figlet.renderText(user_string))



