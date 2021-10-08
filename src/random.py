import random
from .loader import bg_colors, faces, eyes
from PIL import Image, ImageColor

def get_random_bg(mode='RGBA'):
    return ImageColor.getcolor(random.choice(bg_colors), mode)

def get_random_face():
    return Image.open(random.choice(faces))

def get_random_eye():
    return Image.open(random.choice(eyes))