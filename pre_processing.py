# -*- coding: UTF-8 -*-

# Importing RootPostag class from rootANDpostag module
from rootANDpostag import RootPostag

# Taking input of a sentence
query = raw_input("Enter your search query: ")

# Spliting the sentence into words/tokens
input_words = query.split(' ')

# Creating an object of class RootPostag
rp = RootPostag()

# Getting root-words and corresponding pos-tags for the tokens/words
root_words, pos_tags = rp.rootWORD_and_posTAG(query)
# root_words is list which will store the corresponding root-words for each token
# pos_tags is list which will store the corresponding pos-tags for each token

# Giving a newline
print

# Printing the obtained data in a tabular format
print "Actual-Word  Root-Word   Pos-Tag"
for i,j,k in zip(input_words, root_words, pos_tags):
    print i + "   " + j + "   " + k
