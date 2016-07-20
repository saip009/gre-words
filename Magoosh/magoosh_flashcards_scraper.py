from selenium import webdriver
import time
import pickle
import re

start_time = time.time()
print '\nStarted at ' + time.strftime("%Y-%m-%d %H:%M:%S")
print 'start_time = ' + str(start_time - start_time) + 's\n'

driver = webdriver.Firefox()
# driver.set_window_size(1366,768)
driver.maximize_window()
driver.get('https://gre.magoosh.com/flashcards/vocabulary/decks')
elems_len = driver.find_elements_by_class_name('card-footer')
# lim_card = driver.find_elements_by_class_name('card-text')
# x = 0

# decks = ['common', 'basic', 'advanced']             #common words deck 1 is named high frequency in url

for x in range(len(elems_len)-1):

    if x < 17:                                   # skip completed ones
        continue

    driver.get('https://gre.magoosh.com/flashcards/vocabulary/decks')
    elems = driver.find_elements_by_class_name('card-footer')
    lim_card = driver.find_elements_by_class_name('card-text')

    deck = {}
    word_count = 0
    lim_text = lim_card[x].text
    lim = int(re.findall(r'of (5[01]) words', lim_text)[0])

    card_title = driver.find_elements_by_class_name('card-title')[x].text.lower()
    card_title = re.sub(r'\s', '_', card_title )

    # print card_title
    # break

    # y = x+1
    # if y == 20:
    #     y += 1

    # filename = decks[(y)/7] + '_' + str((y)%8) + '.p'
    print '\nSTARTING ' + card_title + ' file...\n'
    # elems[x].location_once_scrolled_into_view
    # driver.execute_script("window.scrollTo(0, " + str(elems[x].location['y']) + ")")
    # print 'start'
    # time.sleep(10)
    # print ' over'
    # print elems[x].get_attribute('href')
    driver.get(elems[x].get_attribute('href'))

    # elems[x].click()

    while word_count < lim:

        clickables = []
        time.sleep(3)
        clickables = driver.find_elements_by_class_name('card-footer')

        while len(clickables) == 0:
            print 'WAITING...'
            time.sleep(3)
            clickables = driver.find_elements_by_class_name('card-footer')

        time.sleep(3)
        clickables[0].click()
        word = driver.find_element_by_class_name('flashcard-word').text

        if word not in deck:
            word_count += 1
            deck[word] = {}

            meanings = driver.find_elements_by_class_name('flashcard-text')
            egs = driver.find_elements_by_class_name('flashcard-example')

            for tmp in range(len(meanings)):
                deck[word]['meaning_' + str(tmp+1)] = meanings[tmp].text
                try:
                    deck[word]['eg_' + str(tmp+1)] = egs[tmp].text
                except IndexError:
                    pass

            note = driver.find_elements_by_class_name('flashcard-note')

            if len(note):
                deck[word]['note'] = note[0].text

        # knew.click()
        clickables[1].click()
        print str(word_count) + '\t words saved'

    with open('Data/' + card_title + '.p', "wb") as write:
        pickle.dump(deck, write)

    file_ = open('Data/' + card_title + '.txt', 'w')
    file_.write(str(deck))

    print '\n' + card_title + '\t\t SUCCESS\t\t at ' + time.strftime("%Y-%m-%d %H:%M:%S")
    print 'Elapsed Time: ' + str((time.time() - start_time)) + 's\n\n'
