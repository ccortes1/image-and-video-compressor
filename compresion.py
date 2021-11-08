""" functions for compression  of video and picture """
import subprocess
from PIL import Image

def change_file(name_file, new_name, direct):
    """ replace original file for compressed file """
    subprocess.run(['rm', f'{direct}/{name_file}'])
    subprocess.run(['mv', f'{direct}/{new_name}', f'{direct}/{name_file}'])

def video_compression(name_video, directory):
    """
    compression of vidoes
    """
    new_name = f'compressed_{name_video}'
    subprocess.run(['ffmpeg', '-i', f'{directory}/{name_video}', '-crf', '24', f'{directory}/{new_name}'], )
    change_file(name_video, new_name, directory)
    print('compresion terminada')

def image_compression(name_image, directory):
    """
    compression of image
    """
    picture = Image.open(f'{directory}/{name_image}')
    new_name = f'compressed_{name_image}'
    picture.save(f'{directory}/{new_name}', optimize=True, quality=85)
    change_file(name_image, new_name, directory)
    print('compresion terminada')
