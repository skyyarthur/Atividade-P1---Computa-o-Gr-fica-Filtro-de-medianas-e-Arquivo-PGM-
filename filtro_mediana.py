import numpy as np
from scipy.ndimage import median_filter
import matplotlib.pyplot as plt

## função que carrega a imagem PGM no formato P2
def load_pgm(filename):
    with open(filename, 'r') as f:
        # ignora a linha do tipo mágico "P2"
        f.readline()
        # ignora comentários
        while True:
            line = f.readline()
            if line[0] != '#':
                break
        ## identifica as dimensões da imagem
        width, height = map(int, line.split())
        # lê o valor de cinza
        max_val = int(f.readline())
        ## lê os dados da foto
        image = []
        for line in f:
            image.extend([int(i) for i in line.split()])
        image = np.array(image).reshape((height, width))
    return image

## função que salva a imagem no formato P2
def save_pgm(image, filename):
    height, width = image.shape
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")  # maior valor de cinza
        for row in image:
            f.write(" ".join(map(str, row)) + '\n')

## nomes de arquivos PGM
image_files = ['cameraman.pgm', 'einstein.pgm', 'kid.pgm']
filtered_files = ['filtered_cameraman.pgm', 'filtered_einstein.pgm', 'filtered_kid.pgm']

## Loop para filtrar e salvar as imagens
fig, axes = plt.subplots(3, 2, figsize=(10, 15))  ## 3 imagens, 2 colunas 

for i, image_file in enumerate(image_files):
    image = load_pgm(image_file)
    
    ## aplica o filtro da mediana 3x3
    filtered_image = median_filter(image, size=3)
    
    save_pgm(filtered_image, filtered_files[i])
    
    ## coloca a imagem original e a filtrada no tela 
    axes[i, 0].imshow(image, cmap='gray')
    axes[i, 0].set_title(f'Original - {image_file}')
    axes[i, 0].axis('off')
    
    axes[i, 1].imshow(filtered_image, cmap='gray')
    axes[i, 1].set_title(f'Filtrada - {filtered_files[i]}')
    axes[i, 1].axis('off')

plt.tight_layout()
plt.show()
