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

tiny_shirt = Image.open("tiny_shirt.png")
tiny_data = list(tiny_shirt.getdata())
new_shirt = Image.new("P", size=shirt.size)
new_shirt.info = tiny_shirt.info
new_shirt.putpalette(tiny_shirt.palette)
data = list(shirt.getdata())


def map_data(data):
    new_data = []
    count = 0
    for d in data:
        count += 1
        if count > 300000:
            print(d)
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(d)

    print(count)
    return new_data


def compare(data, tiny_data):
    for i in range(len(data)):
        if i > 300000:
            print(data[i], tiny_data[i])


# new_data = compare(data, tiny_data)

new_shirt.putdata(tiny_data)
new_shirt.save("new_shirt.png")

try:
    with Image.open(sys.argv[1]) as input:
        input_crop = ImageOps.fit(input, shirt.size)
        input_crop.paste(shirt, mask=shirt)
        input_crop.save(sys.argv[2])

except FileNotFoundError:
    print("404")
