""" compression of multimedia """

# standard
from datetime import datetime
import subprocess
import os

# own
import compresion

DIRECTORIES = ['./pruebas']

def compression_system(direc):
    """ gestion of compression """
    # files = os.listdir(direc)
    files = subprocess.run([f'find {direc} -type f -mtime -1'], stdout=subprocess.PIPE, shell=True)
    files = str(files.stdout).split('\\')
    list_files = []
    for file in files:
        list_files.append(file.split('/')[-1])
        print(file.split('/')[-1])
    print(list_files)

    for file in list_files:
        if os.path.isfile(os.path.join(direc, file)) and file.endswith(('.jpg', '.png', 'jpg', 'jpeg')):
            compresion.image_compression(file, direc)
        elif os.path.isfile(os.path.join(direc, file)) and file.endswith('.mp4'):
            compresion.video_compression(file, direc)
    

if __name__ == '__main__':

    for directory in DIRECTORIES:
        compression_system(directory)