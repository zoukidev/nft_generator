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
    'beard': [],
    'glasses': [],
    'hair': [],
}

def load_assets(directories):
    for dir in directories:
        dir_type = str(dir.split('/')[1])
        for asset in os.listdir(dir):
            assets[dir_type].append('{}/{}'.format(dir, asset))