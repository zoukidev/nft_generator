import random
from .loader import bg_colors, faces, face_colors, eyes, mouths
from PIL import Image, ImageColor

def get_random_bg(mode='RGB'):
    return ImageColor.getcolor(random.choice(bg_colors), mode)

def get_random_face():
    return Image.open(random.choice(faces))

def get_random_face_color():
    return Image.open(random.choice(face_colors))

def get_random_eye():
    return Image.open(random.choice(eyes))

def get_random_mouth():
    return Image.open(random.choice(mouths))