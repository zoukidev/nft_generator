import random
import PIL
from PIL import Image, ImageColor

bgColors = [
    ImageColor.getcolor('#3498db', 'RGB'),
    ImageColor.getcolor('#f1c40f', 'RGB'),
    ImageColor.getcolor('#e74c3c', 'RGB'),
    ImageColor.getcolor('#2ecc71', 'RGB'),
]

faces = [
    'assets/faces/001.png'
]

eyes = [
    'assets/eyes/001.png'
]

new_image = Image.new('RGBA', (32, 32), random.choice(bgColors))

random_face = Image.open(random.choice(faces))
new_image.paste(random_face, (0, 0), random_face)
random_eye = Image.open(random.choice(eyes))
new_image.paste(random_eye, (0, 0), random_eye)


new_image = new_image.resize((300, 300), resample=Image.NEAREST)
new_image.save('new_image.png')