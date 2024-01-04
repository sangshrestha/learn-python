from fpdf import FPDF

name = input("Name: ").strip()

width, height = 210, 297

pdf = FPDF(format=(width, height))
pdf.add_page()
pdf.set_font("helvetica", "", 48)
pdf.cell(0, 50, "CS50 Shirtificate", align="C")


# Add image
image_w = 180
image_y = height / 4
pdf.image("shirtificate.png", x=(width - image_w) / 2, y=image_y, w=image_w)


# Add text on top of image
pdf.set_x(0)
pdf.set_font("helvetica", "B", 18)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 250, f"{name} took CS50", align="C")

pdf.output("tuto1.pdf")
