from src.utils import generate_unique_filename, generate_hash
from PIL import Image
from src.loader import bg_colors
import random

class NFT:
    def __init__(self, asset_pack) -> None:
        self.assets = asset_pack.get('assets')
        self.conditions = self.load_conditions(asset_pack.get('conditions'))
        self.layers = list()
        self.random_properties()
        self.hash = None

    def random_properties(self):
        for asset_config in sorted(self.assets, key=lambda x : x['index'], reverse=False):
            if asset_config.get('conditions'):
                for condition in asset_config.get('conditions'):
                    if self.conditions.get(condition):
                        self.layers.append(random.choice(asset_config.get('assets')))
            else:
                self.layers.append(random.choice(asset_config.get('assets')))

    def load_conditions(self, conditions):
        conditions_dict = {}
        for condition_key, condition in conditions.items():
            if condition.get('type') == 'random':
                conditions_dict[condition_key] = random.choice(condition.get('choices'))
                if condition.get('dependsOn') is not None:
                    for dependsOn in condition.get('dependsOn').split(','):
                        key, cond = dependsOn.split('=')
                        if conditions_dict.get(key) and conditions_dict.get(key) != cond:
                            conditions_dict[condition_key] = False
        return conditions_dict

    def get_hash(self):
        self.hash = generate_hash(self.layers)
        return self.hash

    def save(self, ouput, i):
        filename = '{}{}.png'.format(ouput, generate_unique_filename())
        new_image = Image.new('RGBA', (32, 32), random.choice(bg_colors))

        for layer in self.layers:
            image = Image.open(layer)
            new_image.paste(image, (0, 0), image)

        new_image = new_image.resize((300, 300), resample=Image.NEAREST)
        new_image.save(filename)

        print('#{}: {} (Hash: {}, {} Layers)'.format(i, filename, self.hash, len(self.layers)))

    def debug(self):
        print('genre={}, haveBeard={}'.format(self.conditions['genre'], True if self.conditions['haveBeard'] else False))