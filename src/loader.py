from src.utils import resolve_path
import json

# bg_colors = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1']
bg_colors = ['#3498db', '#2980b9', '#9b59b6', '#8e44ad', '#34495e', '#2c3e50']

def load_asset_pack(profile, cb):
    with open('profiles/{}'.format(resolve_path(profile)) + 'profile.json') as f:
        cb(json.loads(f.read()))