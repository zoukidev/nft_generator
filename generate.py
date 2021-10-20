import argparse
import os
import hashlib
import random
import datetime
from src.profil import Profile
from src.loader import load_assets

parser = argparse.ArgumentParser(description='Generate random NFT.')
parser.add_argument('-n','--number', help='The number of NFTs you wish to generate', default=1, required=True)
args = parser.parse_args()

load_assets([
    'assets/face',
    'assets/eye',
    'assets/mouth',
    'assets/hair',
    'assets/beard',
    'assets/glasses',
])

if __name__ == '__main__':
    if not os.path.exists('nft/'):
        os.mkdir('nft')

    for x in range(int(args.number)):
        yymmss = datetime.datetime.now().strftime('%y-%m-%s')
        datehash = hashlib.md5('{}-{}'.format(random.randrange(0, 9999), yymmss).encode('utf-8')).hexdigest()
        new_profile = Profile()
        filename = 'nft/{}.png'.format(datehash)
        print(filename)
        new_profile.saveImage(filename)