import pickle

def search_key(term, word):
    keys = [key for key, value in words[word].items() if key[:-1] == term + '_']
    if term == 'mnemonic':
        keys.reverse()
    # for key in words[word].items():
    #     print key
    # print words[word]
    # print keys
    if len(keys) != 0:
        for key in keys:
            print key + ': ' + words[word][key]  # .encode('ascii', 'ignore')

            if term == 'meaning':
                try:
                    key2 = 'eg_' + key[-1]
                    raw_input(key2 + ': ' + words[word][key2])  # .encode('ascii', 'ignore'))
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

    while True:
        word = raw_input('Enter word: ').strip()
        if word not in words:
            end = raw_input('Do you wanna quit? [y/n]: ')
            if end.lower() == 'y':
                break
            elif end.lower == 'n':
                continue

        search_key('meaning', word)
        search_key('mnemonic', word)


        # keys = [key for key, value in words[word].items() if key[:-1] == 'mnemonic_']
        # keys.reverse()
        # # for key in words[word].items():
        # #     print key
        # # print words[word]
        # # print keys
        # if len(keys) != 0:
        #     for key in keys:
        #         print key + ': ' + words[word][key]

        print
