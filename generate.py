import argparse
from src.random import generate_random_images
from src.loader import load_assets

parser = argparse.ArgumentParser(description='Generate random NFT.')
parser.add_argument('-n','--number', help='The number of NFTs you wish to generate', default=1, required=False)
args = parser.parse_args()

load_assets([
    'assets/face',
    'assets/eye',
    'assets/mouth',
    'assets/hair',
])

generate_random_images(args.number)