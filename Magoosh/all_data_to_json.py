import pickle
import json
import os

files = [x for x in os.listdir('Data') if x[-2:] == '.p']

all_words = {}

for filename in files:
    path = 'Data/' + filename
    with open(path, 'rb') as handle:
        words = pickle.load(handle)

    all_words[filename[:-2]] = words

with open('./json/magoosh.json', 'w') as outfile:
    json.dump(all_words, outfile)