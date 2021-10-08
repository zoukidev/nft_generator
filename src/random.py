import random
from .loader import bg_colors, assets
from PIL import Image, ImageColor

def get_random_bg(mode: str ='RGB') -> Image:
    return ImageColor.getcolor(random.choice(bg_colors), mode)

def get_random_face() -> Image:
    return Image.open(random.choice(assets['face']))

def get_random_eye() -> Image:
    return Image.open(random.choice(assets['eye']))

def get_random_mouth() -> Image:
    return Image.open(random.choice(assets['mouth']))

def get_random_beard() -> Image:
    return Image.open(random.choice(assets['beard']))

def get_random_glasses() -> Image:
    return Image.open(random.choice(assets['glasses']))

def get_random_hair() -> Image:
    return Image.open(random.choice(assets['hair']))