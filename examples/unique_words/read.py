import re
import numpy as np


def read_file(read_file):
    list_words = []
    with open(read_file, 'r', encoding='UTF-8') as f:
        for line in f:
            list_words = np.concatenate((list_words, re.findall(r'[a-zа-я]+', line.lower())), axis=0)

    return list(set(list_words))
