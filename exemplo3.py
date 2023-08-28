from PIL import Image
im = Image.open("spock-kirk.jpg")
print(im.format, im.size, im.mode)
box = (820, 730, 1500, 1200)
region = im.crop(box)
region.show()
