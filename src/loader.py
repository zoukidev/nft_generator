import os

bg_colors = [
    '#1abc9c',
    '#2ecc71',
    '#3498db',
    '#9b59b6',
    '#34495e',
    '#f1c40f',
    '#e67e22',
    '#e74c3c',
    '#ecf0f1'
]

assets = {
    'face': [],
    'eye': [],
    'mouth': [],
    'hair': [],
}

def load_assets(directories):
    for dir in directories:
        for asset in os.listdir(dir):
            dir_type = dir.split('/')[1]
            assets[dir_type].append('{}/{}'.format(dir, asset))