import re
import string
from stemming.porter2 import stem

def prettify(str):
    str = re.sub(r'http(s?)://([^ ]*)', '', str)
    str = re.sub(r'(.*?)\.png', '', str)
    str = re.sub(r'(.*?)\.jpg', '', str)
    str = re.sub(r'([\d\.]+)([MKB]+)', '', str)
    str = ''.join(ch for ch in str if ch not in string.punctuation)
    str = str.lower()
    ' '.join([stem(x) for x in str.split()])
    return str
