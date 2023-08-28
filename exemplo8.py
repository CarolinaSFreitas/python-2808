from PIL import Image

im = Image.new("RGB", (400, 400), (255, 255, 0))

# for i in range(400):
#     im.putpixel((i, 0), (0, 0, 255))
#     im.putpixel((i, 1), (0, 0, 255))
#     im.putpixel((i, 2), (0, 0, 255))
#     im.putpixel((i, 3), (0, 0, 255))
#     im.putpixel((i, 4), (0, 0, 255))
#     im.putpixel((i, 5), (0, 0, 255))

for i in range(400):
    for j in range(200):
        im.putpixel((i, j), (0, 0, 255))
    
im.show()
im.save("teste.jpg")

                    