from PIL import Image
im = Image.open("spock-kirk.jpg")
# out = im.rotate(45)
out = im.transpose(Image.Transpose.ROTATE_180)
out.show()