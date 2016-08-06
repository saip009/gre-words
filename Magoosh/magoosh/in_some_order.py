#All the best for your test :)  -saip009

import pickle
import random

def search_key(term, word):
    keys = [key for key, value in words[word].items() if key[:-1] == term + '_']
    keys.reverse()
    # for key in words[word].items():
    #     print key
    # print words[word]
    # print keys
    if len(keys) != 0:
        for key in keys:
            print key + ': ' + words[word][key].encode('ascii', 'ignore')

            if term == 'meaning':
                try:
                    key2 = 'eg_' + key[-1]
                    raw_input(key2 + ': ' + words[word][key2].encode('ascii', 'ignore'))
                except KeyError:
                    pass

                print

        if term != 'meaning':
            raw_input()
    else:
        # print 'No ' + term + 's for this word.'
        raw_input('No ' + term + 's for this word. ')

while True:

    decks = ['common_words_', 'basic_', 'advanced_', 'end']
    print decks

    x = raw_input('Select one [1-3]: ')
    try:
        if int(x) < 1 or int(x) > 3:
            break
    except ValueError:
        break

    y = raw_input('Enter roman numeral for deck: ')
    path = 'Data/' + decks[int(x)-1] + y + '.p'

    with open(path, 'rb') as handle:
        words = pickle.load(handle)
    print

    freq = [0 for x in range(len(words))]
    all_words = [k for k,v in words.items()]
    random.shuffle(all_words)

    print str(len(all_words)) + ' WORDS.'
    print

    for ind in range(len(all_words)):

        word = all_words[ind]
        freq[ind] += 1

        done = [ _ for _ in freq if _ == 4]
        seen = [ _ for _ in freq if _ != 0]

        raw_input(str(ind+1) + '. ' + word)
        search_key('meaning', word)
        search_key('mnemonic', word)
        raw_input('Press Enter to continue... ')

        print

    print 'DECK is done. Congrats! :)'
    print
    print

#https://github.com/saip009
