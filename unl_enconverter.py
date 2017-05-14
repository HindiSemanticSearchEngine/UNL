# -*- coding: UTF-8 -*-

# Importing RootPostag class from rootANDpostag module
from rootANDpostag import RootPostag
# Importing Relations class from relation module
from relation import Relations

# importing from neo4j driver
from py2neo import Graph
from py2neo import Node, Relationship

class Enconversion:
    '"Class for enconverting a sentence into unl format"'

    def enconversion(self, query):
        # Spliting the sentence into words/tokens
        input_words = query.split(' ')

        # Creating an object of class RootPostag
        rp = RootPostag()

        # Getting root-words and corresponding pos-tags for the tokens/words
        # root_words is list which will store the corresponding root-words for each token
        # pos_tags is list which will store the corresponding pos-tags for each token
        root_words, pos_tags = rp.rootWORD_and_posTAG(query)

        # Making a list of dictionaries, where each dictionary will contain properties of the individual word
        word_dic = []
        for i, j, k in zip(input_words, root_words, pos_tags):
            word_dic.append({"word":i, "root_word":j, "pos_tag":k})

        graph = Graph("http://<username>:<password>@localhost:7474/db/data/")

        rel = Relations()

        word = []
        for i in xrange(0, len(word_dic)):
            print word_dic[i]['word'],word_dic[i]['root_word'],word_dic[i]['pos_tag']
            try:
                word.append(Node(word_dic[i]['word'], Word = word_dic[i]['word'], RootWord = word_dic[i]['root_word'], PosTag = word_dic[i]['pos_tag']))
            except:
                word.append(Node('InvalidIdentifier', Word = 'InvalidIdentifier', RootWord = 'InvalidIdentifier', PosTag = 'InvalidIdentifier'))
            graph.create(word[i])

        # Checking for unl relations between a pair of words in the sentence
        for i in xrange(0, len(word_dic)):
            for j in xrange(0, len(word_dic)):
                # If same words are not chosen together
                if i != j:
                    if rel.qua_relation(word_dic[i], word_dic[j]):
                        qua = Relationship(word[i], 'QUA', word[j])
                        graph.create(qua)

                    if rel.qua_relation(word_dic[j], word_dic[i]):
                        qua = Relationship(word[j], 'QUA', word[i])
                        graph.create(qua)

                    if rel.dur_relation(word_dic[i], word_dic[j]):
                        dur = Relationship(word[i], 'DUR', word[j])
                        graph.create(dur)

                    if rel.dur_relation(word_dic[j], word_dic[i]):
                        dur = Relationship(word[j], 'DUR', word[i])
                        graph.create(dur)

                    if rel.agt_relation(word_dic[i], word_dic[j]):
                        agt = Relationship(word[i], 'AGT', word[j])
                        graph.create(agt)

                    if rel.agt_relation(word_dic[j], word_dic[i]):
                        agt = Relationship(word[j], 'AGT', word[i])
                        graph.create(agt)


'''
# Taking input of a sentence
query = raw_input("Enter your search query: ")
enc = Enconversion()
enc.enconversion(query)
'''
