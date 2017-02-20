# -*- coding: UTF-8 -*-

# importing the root word and postag finding module
import rootwordANDpostag

# Sure words
SureWords = []

# Dictionary to relate the postags of UNL-dictonary and IIIT Hyderabad pos-tagger
POStags = {
"NNP":"N",
"NN":"N",
"N": "N",
"NST":"N",
"PRP":"PRP",
"VM":"V",
"VAUX":"VAUX",
"JJ":"ADJ",
"RB":"ADV",
"RP":"RP",
"CC":"CC",
"WQ":"QW",
"QF":"QF",
"INJ":"UH",
"NEG":"NEG",
"XC":"N"
}

query = raw_input("Enter your search query: ")
input_words = query.split(' ')

# Getting root-words and corresponding pos-tags for them
root_words, pos_tags = rootwordANDpostag.rootWORD_and_posTAG(query)

# Dictionary to store words(tokens) and postags
PT1_dic = {}
for token,pt in zip(input_words, pos_tags):
    PT1_dic[token] = pt

# Dictionary to store root-words of tokens and postags
PT2_dic = {}
for token,pt in zip(root_words, pos_tags):
    PT2_dic[token] = pt

# List to store found words in first attempt
found_words1 = []

# Checking for words in first(main) UNL dictonary
print "\nInitial Query Words..."
for i in input_words:
    print i
print "Checking for words in UNL dictonary...\n"

with open('UW-Hindi_Dict-20131003.txt') as xtream:
    for line in xtream:
        word = line.split(']')[0]
        word = word.replace('[', '')
        for query_word in input_words:
            if query_word == word:
                if query_word not in found_words1:
                    found_words1.append(query_word)

                Line = line.strip().split('" ')[1]
                Tag = line.strip('" ').split('" (')[1].split(",")[0]
                if Tag == POStags[PT1_dic[query_word]]:
                    print "Hurray!!!!!! " + Tag
                print "Line: " + Line
                print "POS-TAG:" + Tag
                print "Word: " + query_word
                print "Matched word: " + word
                #if PT_dic[query_word] == line.strip('" ')[1].strip("(").split(",")[0]:
                #    print line.strip('" ')[1].strip("(").split(",")[0]

xtream.close()

# Making a list of corresponding root words of the words which were not found in the UNL dictinary
final_list = []

print "\nFinal List of Query Words..."
for i,j in zip(input_words,root_words):
    if i not in found_words1:
        print j
print "Checking for root words in UNL dictonary...\n"

# List to store words whose root form is found in second attempt
found_words2 = []

# Last try to find words using their root forms in the UNL dictonary
with open('UW-Hindi_Dict-20131003.txt') as ytream:
    for line in ytream:
        word = line.split(']')[0]
        word = word.replace('[', '')
        for query_word,i in zip(input_words, root_words):
            if query_word not in found_words1:
                if i == word:
                    if query_word not in found_words2:
                        found_words2.append(query_word)
                    print "Line: " + line.strip().split('" ')[1]
                    print "POS-TAG: " + line.strip('" ').split('" (')[1].split(",")[0]
                    print "Word: " + query_word
                    print "Matched word: " + word

ytream.close()

print "\nNot-Found words..."
for i in input_words:
    if i not in found_words1 and i not in found_words2:
        print i
