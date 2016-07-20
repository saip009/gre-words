import os, sys
import pickle
import requests
from bs4 import BeautifulSoup
import re

files = [x for x in os.listdir('Data') if x[-2:] == '.p']
# print x

for filename in files:
    path = 'Data/' + filename
    with open(path, 'rb') as handle:
        words = pickle.load(handle)

    print filename + '\t STARTING\n'
    word_count = 0

    for word in words:
        word_count += 1
        url = 'http://www.mnemonicdictionary.com/?word=' + word.lower()

        html = requests.get(url).text
        soup = BeautifulSoup(html)

        comments = soup.find_all("div", attrs={'class': 'span9'})
        ratings = soup.find_all("div", attrs={'class': 'span3', 'style':'float:right;border-left:1px solid #E3E3E3;padding-left:20px;'})

        # print len(comments)
        # print len(ratings)

        if len(comments) > 3:
            comments = comments[:3]

        i = 0
        ratings_final = []

        for comment in comments:
            rates = re.findall(r'[0-9]+', ratings[i].text.strip())
            ratings_final.append(rates[0])
            ratings_final.append(rates[1])
            i += 1
            mnemonic = comment.text.strip()
            # mnemonic = mnemonic.split('\n')
            # mnemonic = filter(None, mnemonic)
            # mnemonic = ''.join(mnemonic)                            # this block does not work due to carriage return
            mnemonic = mnemonic.splitlines()
            # print mnemonic
            mnemonic = filter(None, mnemonic)
            for _ in range(len(mnemonic)-1):
                mnemonic[_] += '. '
            mnemonic = ''.join(mnemonic)
            # print mnemonic                                            #need to correct this line thingy before moving on..
            # print
            words[word]['mnemonic_' + str(i)] = mnemonic

        words[word]['ratings'] = ratings_final              # alternate +ve and -ve

        # for k, v in words[word].items():
        #     print k
        #     print v

        print str(word_count) + ' words done...'
        # break

    with open(path, 'wb') as handle:
        pickle.dump(words, handle)
    print filename + '\n\t\t [DONE]\n\n'
    # break
