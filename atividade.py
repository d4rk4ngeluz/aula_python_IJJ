from PIL import Image

# Crie uma nova imagem com dimensões específicas
img = Image.new('RGB', (300,300), (255,0,0))

# Coloque os dados na imagem
# img.putdata(my_list)

# Salve a imagem em um arquivo
img.save('image.png')