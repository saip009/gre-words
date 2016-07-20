import os
import pickle

files = [x for x in os.listdir('Data') if x[-2:] == '.p']

word_list = open('word_list.txt','a+')

for filename in files:
    path = 'Data/' + filename
    with open(path, 'rb') as handle:
        words = pickle.load(handle)
        for word in words:
        	word_list.write(word + '\n')

print 'done'