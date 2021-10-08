from src.random import *

new_image = Image.new('RGBA', (32, 32), get_random_bg())

random_face = get_random_face()
new_image.paste(random_face, (0, 0), random_face)

random_eye = get_random_eye()
new_image.paste(random_eye, (0, 0), random_eye)


new_image = new_image.resize((300, 300), resample=Image.NEAREST)
new_image.save('new_image.png')