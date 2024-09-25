# Atividade-P1---Computa-o-Gr-fica-Filtro-de-medianas-e-Arquivo-PGM-
Atividade P1 - Computação Gráfica (Filtro de medianas e Arquivo PGM) 

# Nome: Arthur Torres - RA: 740410 

Esse projeto tem como objetivo aplicar o filtro de mediana em imagens no formato PGM.
O filtro mediana tem como função substituir os valores de cada pixel pela mediana dos valores de pixels vizinhos. Isso faz com que a imagem seja suavizada e tenha sua qualidade aumentada.

Tecnologias usadas: Python (NumPy, SciPy e Matplotlib)

Funcionalidades: 
- Leitura de imagens PGM;
- Aplicação do filtro de mediana;
- Salvar a imagem;
- Exibição das imagens (original e filtrada);

Pré requisitos:
Certifique-se de ter instalado o Python no computador e as bibliotecas utilizadas:
*pip install numpy scipy matplotlib* - comando para instalar as bibliotecas

Estrutura do projeto: 
- cameraman.pgm: Imagem de exemplo 1.
- einstein.pgm: Imagem de exemplo 2.
- kid.pgm: Imagem de exemplo 3.
- filtered_cameraman.pgm: Imagem filtrada 1.
- filtered_einstein.pgm: Imagem filtrada 2.
- filtered_kid.pgm: Imagem filtrada 3.
- filtro_mediana.py: Código Python que aplica o filtro de mediana.
- README.md: Este arquivo de instruções.


Conclusão
Após a execução do códigos, as imagens serão exibidas em uma nova janela e salvas na pasta do projeto com o prefixo "filtred_".
O código principal é divido em três partes: Leitura das imagens (load_pgm), aplicação do filtro (process_image) e exibição (display_images).
