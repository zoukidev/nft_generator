from src.utils import dump, resolve_path
import json

bg_colors = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1']
asset_pack = {}

def load_asset_pack(profile, cb):
    with open('profiles/{}'.format(resolve_path(profile)) + 'profile.json') as f:
        asset_pack = json.loads(f.read())
        cb(asset_pack)