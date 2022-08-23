""" compression of multimedia """
# standard
from datetime import datetime
import subprocess


# own
import compresion

DIRECTORIES = '.'

def compression_system(direc):
    """ gestion of compression """
    FORMATS = ['.mp4', '.jpg', '.png', 'jpg', 'jpeg']
    for formato in FORMATS:
        files = subprocess.run([f'find {direc} -name "*{formato}" -mtime -1'], stdout=subprocess.PIPE, shell=True)
        files = str(files.stdout)[2:-1].split('\\n')[0:-1]
        print(f'find {direc} -name "*{formato}" -mtime -1')
        print(files)
        for file in files:

            f = file.split('/')[-1]
            directorio = ('/').join(file.split('/')[0:-1])
            if formato == '.mp4':
                compresion.video_compression(f, directorio)
            else:
                compresion.image_compression(f, directorio)


if __name__ == '__main__':

    compression_system(DIRECTORIES)