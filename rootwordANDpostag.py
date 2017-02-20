import os
import re

def rootWORD_and_posTAG(query):
    f = open('hindi_pos_root_tagger/hindi.input.txt','w')
    f.write(query)
    f.close()
    os.system("cd hindi_pos_root_tagger && make tag")

    actual_wordlist = []
    pos_taglist = []
    root_wordlist = []

    with open("hindi_pos_root_tagger/hindioutput.txt",'r') as q:
        for line in q:
            fullLine = re.sub('\t', " ", line)
            wordList = fullLine.split(" ")
            actual_wordlist.append(wordList[0])
            root_wordlist.append(wordList[1])
            pos_taglist.append(wordList[2])

    q.close()
    return root_wordlist,pos_taglist
