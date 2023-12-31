import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    print("Too few cmd-line args")
    sys.exit()


in_suffix = sys.argv[1].split(".")[-1]
out_suffix = sys.argv[2].split(".")[-1]


if not in_suffix in ["jpg", "jpeg", "png"]:
    print("Invalid format")
    sys.exit()

if in_suffix != out_suffix:
    print("Input != Output")
    sys.exit()

shirt = Image.open("shirt.png")

try:
    with Image.open(sys.argv[1]) as input:
        input_crop = ImageOps.fit(input, shirt.size)
        input_crop.paste(shirt, mask=shirt)
        input_crop.save(sys.argv[2])

except FileNotFoundError:
    print("404")
