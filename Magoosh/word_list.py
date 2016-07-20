import pickle

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

    print len(words)
    all_keys = words.keys()
    for k in all_keys:
        print k
        if all_keys.index(k)%4 == 3:
            print

    print
    print
