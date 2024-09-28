#import os
import time

# Obtém o número de núcleos lógicos (threads)
#num_threads = os.cpu_count()
#print(f"Seu computador possui {num_threads} threads.")

#import multiprocessing

# Obtém o número de núcleos lógicos (threads)
#num_threads = multiprocessing.cpu_count()
#print(f"Seu computador possui {num_threads} threads.")

#import os

# Obtém o número de núcleos lógicos (threads)
#num_threads = os.cpu_count()
#print(f"Seu computador possui {num_threads} threads.")

#import multiprocessing

# Obtém o número de núcleos lógicos (threads)
#num_threads = multiprocessing.cpu_count()
#print(f"Seu computador possui {num_threads} threads.")

from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor
start_time = time.time()  # Inicia o cronômetro

# Função para comprimir uma única imagem
def compress_image(input_image_path, output_image_path, quality=5):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, "JPEG", quality=quality)


# Função para comprimir todas as imagens da pasta usando multithreading
def compress_images_in_folder(folder_path, output_folder_path, quality=5, num_threads=4):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Lista de imagens na pasta de origem
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Função interna para ser usada em cada thread
    def process_image(filename):
        input_image_path = os.path.join(folder_path, filename)
        output_image_path = os.path.join(output_folder_path, filename)
        compress_image(input_image_path, output_image_path, quality)

    # Usa ThreadPoolExecutor para comprimir as imagens em paralelo
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(process_image, image_files)


# Defina o caminho da pasta de origem e da pasta de saída
folder_path = r'C:\Users\84246626\Documents\Python-Pandas-master\Excel\POIMG'
output_folder_path = r'C:\Users\84246626\Documents\Python-Pandas-master\Excel\saida'

# Chama a função para comprimir as imagens usando threads
compress_images_in_folder(folder_path, output_folder_path, quality=5, num_threads=4)

end_time = time.time()  # Para o cronômetro
elapsed_time = end_time - start_time  # Calcula o tempo gasto
print(f"Tempo gasto para comprimir a imagem: {elapsed_time:.2f} segundos")
minutos = elapsed_time / 60
print(f'tempo em minutos: {minutos}')

