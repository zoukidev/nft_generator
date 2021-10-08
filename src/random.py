import random
from .loader import bg_colors, assets
from PIL import Image, ImageColor
import os
import datetime
import hashlib

def get_random_bg(mode='RGB'):
    return ImageColor.getcolor(random.choice(bg_colors), mode)

def get_random_face():
    return Image.open(random.choice(assets['face']))

def get_random_eye():
    return Image.open(random.choice(assets['eye']))

def get_random_mouth():
    return Image.open(random.choice(assets['mouth']))

def generate_random_images(count):
    if not os.path.exists('nft/'):
        os.mkdir('nft')

    for x in range(int(count)):
        print('Random Boolean', True if random.randint(0, 1) else False)
        yymmss = datetime.datetime.now().strftime('%y-%m-%s')
        datehash = hashlib.md5('{}-{}'.format(random.randrange(0, 9999), yymmss).encode('utf-8')).hexdigest()
        generate_random_image('nft/{}.png'.format(datehash))

def generate_random_image(filename):
    new_image = Image.new('RGBA', (32, 32), get_random_bg())

    random_face = get_random_face()
    new_image.paste(random_face, (0, 0), random_face)

    random_eye = get_random_eye()
    new_image.paste(random_eye, (0, 0), random_eye)

    random_mouth = get_random_mouth()
    new_image.paste(random_mouth, (0, 0), random_mouth)

    new_image = new_image.resize((300, 300), resample=Image.NEAREST)
    new_image.save(filename)