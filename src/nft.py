from src.utils import generate_unique_hash

class NFT:
    def __init__(self, asset_pack, custom_filename=None) -> None:
        self.asset_pack = asset_pack
        self.name = custom_filename if custom_filename is not None and len(custom_filename) > 0 else generate_unique_hash()
        
        self.random_properties()

    def random_properties(self):
        for asset_config in self.asset_pack.get('assets'):
            print(asset_config)

    def save(self, ouput):
        filename = '{}{}.png'.format(ouput, self.name)
        print('saved:', filename)