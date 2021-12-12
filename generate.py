import argparse
import os
from src.nft import NFT
from src.loader import load_asset_pack
from src.utils import resolve_path

parser = argparse.ArgumentParser(description='Generate random NFT.')
parser.add_argument('-p','--profile', help='The profile you wish to use', default='cryptopunk', required=True)
parser.add_argument('-s','--size', help='Size of input images', default=512, required=True)
parser.add_argument('-n','--number', help='The number of NFTs you wish to generate', default=1, required=False)
parser.add_argument('-o','--output', help='The output directory', default='nft/', required=False)
nfts = []
args = parser.parse_args()

def create_nft(asset_pack):
    for x in range(int(args.number)):
        nft = NFT(asset_pack, int(args.size))
        if nft.get_hash() not in nfts:
            nft.save(args.output, x)
            nfts.append(nft.hash)
        else:
            continue

if __name__ == '__main__':
    args.output = resolve_path(args.output)

    if not os.path.exists(args.output):
        os.mkdir(args.output)

    load_asset_pack(args.profile, create_nft)