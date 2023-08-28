from PIL import Image

with Image.open("spock-kirk.jpg") as im:
    im = im.convert("L")
    im.show()