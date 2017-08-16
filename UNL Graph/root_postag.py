import os
import re

PUNCTUATION = ('.')


def rootword_and_postag(query):
    '''This function will find the root-words and pos-tags\
    for each word of the sentence passed as a parameter'''

    # The sentence is written in a text file
    with open('hindi-part-of-speech-tagger/hindi.input.txt', 'w') as input_file:
        input_file.write(query)
    input_file.close()
    # The model finds root-words and pos-tags
    os.system("cd hindi-part-of-speech-tagger && make tag")

    actual_wordlist = []
    pos_taglist = []
    root_wordlist = []

    # All the required information is written/stored in text file, hence we need to extract data from that...
    with open("hindi-part-of-speech-tagger/hindi.output", 'r') as q:
        for line in q:
            full_line = re.sub('\t', ' ', line)
            full_line = re.sub(' +', ' ', full_line)
            word_list = full_line.split(' ')
            try:
                pos_taglist.append(word_list[2])
                root_wordlist.append(word_list[1])
                actual_wordlist.append(word_list[0])
            except IndexError:
                print 'Invalid Symbol'

    q.close()

    # Finally we return the two lists containing root-words and pos-tags
    return root_wordlist, pos_taglist
