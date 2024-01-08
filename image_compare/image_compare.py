from PIL import Image
from PIL import ImageChops
import pytesseract


def show_delta(img1, img2):
    diff = Image.new("RGB", img1.size, (255, 255, 255))
    for x1 in range(img1.size[0]):
        for y1 in range(img1.size[1]):
            p1 = img1.getpixel((x1, y1))
            p2 = img2.getpixel((x1, y1))

            p3 = round((p1[0] / 2) - (p2[0] / 2)) + 128

            diff.putpixel((x1, y1), (p3, p3, p3))

    diff.save("diff.png")


path_to_tesseract = r"C:\Users\sanst\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

path_to_images = [r"slide_art.png", r"slide_thumb.png"]

img0 = Image.open(path_to_images[0])
img1 = Image.open(path_to_images[1])

show_delta(img0, img1)
