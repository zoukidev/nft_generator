import random

from PIL.Image import new
from .random import *

class Profile:
    def __init__(self) -> None:
        self.sex = random.randint(0, 1)
        self.def_custom_properties()

    def get_sex(self):
        if self.sex == 0:
            return 'Female'
        elif self.sex == 1:
            return 'Male'

    def def_custom_properties(self):
        self.bg = get_random_bg()
        self.face = get_random_face()
        self.eye = get_random_eye()
        self.mouth = get_random_mouth()
        self.hair = None
        self.beard = None
        self.glasses = None

        if self.get_sex() == 'Male':
            if random.randint(0, 1):
                self.beard = get_random_hair()

            if random.randint(0, 1):
                self.beard = get_random_beard()

            if random.randint(0, 1):
                self.glasses = get_random_glasses()
    
    def saveImage(self, filename):
        new_image = Image.new('RGBA', (32, 32), self.bg)
        new_image.paste(self.face, (0, 0), self.face)
        new_image.paste(self.eye, (0, 0), self.eye)
        new_image.paste(self.mouth, (0, 0), self.mouth)

        if self.hair:
            new_image.paste(self.hair, (0, 0), self.hair)

        if self.beard:
            new_image.paste(self.beard, (0, 0), self.beard)

        if self.glasses:
            new_image.paste(self.glasses, (0, 0), self.glasses)

        new_image = new_image.resize((300, 300), resample=Image.NEAREST)
        new_image.save(filename)