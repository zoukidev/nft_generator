import argparse
from src.random import *

want_nft=0
parser = argparse.ArgumentParser(description='Generate random NFT.')
parser.add_argument('-n','--number', help='The number of NFTs you wish to generate', default=1, required=True)

args = parser.parse_args()
print(args)

def generate_random_nft(x):
    new_image = Image.new('RGBA', (32, 32), get_random_bg())

    random_face = get_random_face()
    new_image.paste(random_face, (0, 0), random_face)

    # random_face_color = get_random_face_color()
    # new_image.paste(random_face_color, (0, 0), random_face_color)

    random_eye = get_random_eye()
    new_image.paste(random_eye, (0, 0), random_eye)

    random_mouth = get_random_mouth()
    new_image.paste(random_mouth, (0, 0), random_mouth)


    new_image = new_image.resize((300, 300), resample=Image.NEAREST)
    new_image.save(str(x) + '.png')


for x in range(int(args.number)):
    generate_random_nft(x)