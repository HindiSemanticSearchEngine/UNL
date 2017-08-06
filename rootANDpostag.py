import os
import re

class RootPostag:
    '"Class to find grammatical data about a hindi sentence(pre-processing for UNL)"'

    # This function will find the root-words and pos-tags for each word of the sentence passed as a parameter
    def rootWORD_and_posTAG(self, query):
        # The sentence is written in a text file
        with open('Hindi_Pos_Root_Tagger/hindi.input.txt','w') as f:
            f.write(query)
        f.close()
        # The model finds root-words and pos-tags
        os.system("cd Hindi_Pos_Root_Tagger && make tag")

        actual_wordlist = []
        pos_taglist = []
        root_wordlist = []

        # All the required information is written/stored in text file, hence we need to extract data from that...
        with open("Hindi_Pos_Root_Tagger/hindioutput.txt",'r') as q:
            for line in q:
                fullLine = re.sub('\t', " ", line)
                wordList = fullLine.split(" ")
                actual_wordlist.append(wordList[0])
                root_wordlist.append(wordList[1])
                pos_taglist.append(wordList[2])

        q.close()

        # Finally we return the two lists containing root-words and pos-tags
        return root_wordlist,pos_taglist
