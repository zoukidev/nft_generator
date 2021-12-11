import datetime
import random
import hashlib
import json

def generate_unique_hash():
    yymmss = datetime.datetime.now().strftime('%y-%m-%s')
    datehash = hashlib.md5('{}-{}'.format(random.randrange(0, 9999), yymmss).encode('utf-8')).hexdigest()

    return datehash

def resolve_path(path):
    if path[-1] != '/':
        path = path + '/'
    
    return path