from PIL import Image

width = 600
height = 400

# Cria uma nova imagem com tamanho especificado e cor de fundo branca
im = Image.new("RGB", (width, height), (255, 255, 255))

# Define as proporções da cruz branca
cross_width = width // 8
cross_height = height // 8

# Preenche o fundo de vermelho
for i in range(height):
    for j in range(width):
        im.putpixel((j, i), (186, 12, 47))  # Vermelho

# Desenha a parte horizontal da cruz branca
for i in range(cross_height * 3, cross_height * 5):
    for j in range(width):
        im.putpixel((j, i), (255, 255, 255))  # Branco

# Desenha a parte vertical da cruz branca
for i in range(height):
    for j in range(cross_width * 3, cross_width * 5):
        im.putpixel((j, i), (255, 255, 255))  # Branco

# Define as proporções da cruz azul dentro da branca
blue_cross_width = cross_width // 2
blue_cross_height = cross_height // 2

# Desenha a parte horizontal da cruz azul
for i in range(cross_height * 3 + blue_cross_height, cross_height * 5 - blue_cross_height):
    for j in range(width):
        im.putpixel((j, i), (0, 32, 91))  # Azul

# Desenha a parte vertical da cruz azul
for i in range(height):
    for j in range(cross_width * 3 + blue_cross_width, cross_width * 5 - blue_cross_width):
        im.putpixel((j, i), (0, 32, 91))  # Azul

# Exibe a imagem e salva em um arquivo
im.show()
im.save("bandeira-noruega.jpg")
