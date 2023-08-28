from PIL import Image

width = 600
height = 400

# Cria uma nova imagem com tamanho especificado e cor de fundo branca
im = Image.new("RGB", (width, height), (255, 255, 255))

# Define a altura de cada faixa
stripe_height = height // 3

# Preenche a primeira faixa com a cor vermelha
for i in range(stripe_height):
    for j in range(width):
        im.putpixel((j, i), (206, 17, 38))  # Vermelho

# Preenche a segunda faixa com a cor amarela
for i in range(stripe_height, 2 * stripe_height):
    for j in range(width):
        im.putpixel((j, i), (252, 209, 22))  # Amarelo

# Preenche a terceira faixa com a cor verde
for i in range(2 * stripe_height, height):
    for j in range(width):
        im.putpixel((j, i), (0, 128, 38))  # Verde

# Exibe a imagem e salva em um arquivo
im.show()
im.save("bandeira-bolivia.jpg")
