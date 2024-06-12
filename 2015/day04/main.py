
from utils import *

seed = "bgvyzdsv"

def find(prefix):
    for i in range(1, 100000000):
        if md5hash(seed, i).startswith(prefix):
            return i
        
print(find("00000"), find("000000"))