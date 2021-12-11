import datetime
import random
import hashlib
import json

def resolve_path(path):
    if path[-1] != '/':
        path = path + '/'
    
    return path

def generate_unique_filename():
    yymmss = datetime.datetime.now().strftime('%y-%m-%s')
    datehash = hashlib.md5('{}-{}'.format(random.randrange(0, 9999), yymmss).encode('utf-8')).hexdigest()

    return datehash

def generate_hash(data) -> str:
    hash = hashlib.md5('-'.join(data).encode('utf-8')).hexdigest()
    return hash