from PIL import Image
im = Image.open("spock.jpg")
print(im.format, im.size, im.mode)
im.show()

