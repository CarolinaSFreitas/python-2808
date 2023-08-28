from PIL import Image, ImageDraw

width = 600
height = 400

# Cria uma nova imagem com tamanho especificado e cor de fundo branca
im = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(im)

# Define as cores
red_color = (206, 17, 38)
white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 128, 0)

# Preenche a faixa vermelha
stripe_height = height // 3
for i in range(stripe_height):
    draw.line((0, i, width, i), fill=red_color)

# Preenche a faixa branca
for i in range(stripe_height, 2 * stripe_height):
    draw.line((0, i, width, i), fill=white_color)

# Preenche a faixa preta
for i in range(2 * stripe_height, height):
    draw.line((0, i, width, i), fill=black_color)

# Calcula as coordenadas para o triângulo verde
triangle_height = height // 2  # Ajuste a altura do triângulo conforme necessário
triangle_base = width // 4
triangle_top = (height - triangle_height) // 2
triangle_bottom = triangle_top + triangle_height
triangle_points = [(0, triangle_top), (0, triangle_bottom), (triangle_base, height // 2)]

# Desenha o triângulo verde à esquerda
draw.polygon(triangle_points, fill=green_color)

# Exibe a imagem e salva em um arquivo
im.show()
im.save("bandeira-sudao.jpg")
