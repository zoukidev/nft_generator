import argparse
import os
import json
from src.nft import NFT
from src.loader import load_asset_pack
from src.utils import resolve_path
from operator import itemgetter, attrgetter

parser = argparse.ArgumentParser(description='Generate random NFT.')
parser.add_argument('-p','--profile', help='The profile you wish to use', default='cryptopunk', required=False)
parser.add_argument('-n','--number', help='The number of NFTs you wish to generate', default=1, required=False)
parser.add_argument('-o','--output', help='The output directory', default='nft/', required=False)
args = parser.parse_args()

def create_nft(asset_pack):
    for x in range(int(args.number)):
        nft = NFT(asset_pack)
        nft.save(args.output)

if __name__ == '__main__':
    args.output = resolve_path(args.output)

    if not os.path.exists(args.output):
        os.mkdir(args.output)

    load_asset_pack(args.profile, create_nft)