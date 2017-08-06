# -*- coding: UTF-8 -*-

# Importing RootPostag class from rootANDpostag module
from rootANDpostag import RootPostag

# Importing Relations class from relation module
from relation import Relations

# importing neo4j python-driver and its classes
import py2neo
from py2neo import Graph, Node, Relationship, Rev

py2neo.authenticate("localhost:7474", "neo4j", "algo7917")
graph = Graph("http://localhost:7474/db/data/")

def createRelationshipWithProperties(query):
    # creating an object of class RootPostag
    rootPostag = RootPostag()

    # creating an object of class Relations
    rel = Relations()

    # Spliting the query/text into sentences
    sentences = query.split('।')

    for sentence in sentences:
        # Spliting the sentence into words/tokens
        sentence = sentence.replace('\n', '').replace('\r', '')
        input_words = sentence.split(' ')

        # Getting root-words and corresponding pos-tags for the tokens/words
        # root_words is list which will store the corresponding root-words for each token
        # pos_tags is list which will store the corresponding pos-tags for each token
        root_words, pos_tags = rootPostag.rootWORD_and_posTAG(sentence)

        # Making a list of dictionaries/nodes, where each dictionary/node will contain properties of the individual word/node
        nodes = []
        word_dic = []
        for i, j, k in zip(input_words, root_words, pos_tags):
            word_dic.append({"word":i, "root_word":j, "pos_tag":k})
            nodes.append(Node("UNL-Word", word=i, root_word=j, pos_tag=k))

        # Checking for unl relations between a pair of words in the sentence
        relationships = []
        for i in range(0, len(word_dic)):
            for j in range(0, len(word_dic)):
                if i != j: # If same words are not chosen together

                    label1 = word_dic[i]['pos_tag']#.encode('utf-8')
                    label2 = word_dic[j]['pos_tag']#.encode('utf-8')

                    if rel.qua_relation(word_dic[i], word_dic[j]):
                        relationships.append(Relationship(label1, 'QUA', label2))
                    if rel.qua_relation(word_dic[j], word_dic[i]):
                        relationships.append(Relationship(label1, Rev('QUA'), label2))

                    if rel.dur_relation(word_dic[i], word_dic[j]):
                        relationships.append(Relationship(label1, 'DUR', label2))
                    if rel.dur_relation(word_dic[j], word_dic[i]):
                        relationships.append(Relationship(label1, Rev('DUR'), label2))

                    if rel.agt_relation(word_dic[i], word_dic[j]):
                        relationships.append(Relationship(label1, 'AGT', label2))
                    if rel.agt_relation(word_dic[j], word_dic[i]):
                        relationships.append(Relationship(label1, Rev('AGT'), label2))

                    if rel.aoj_relation(word_dic[i], word_dic[j]):
                        relationships.append(Relationship(label1, 'AOJ', label2))
                    if rel.aoj_relation(word_dic[j], word_dic[i]):
                        relationships.append(Relationship(label1, Rev('AOJ'), label2))

                    if rel.nam_relation(word_dic[i], word_dic[j]):
                        relationships.append(Relationship(label1, 'NAM', label2))
                    if rel.nam_relation(word_dic[j], word_dic[i]):
                        relationships.append(Relationship(label1, Rev('NAM'), label2))

                    if rel.obj_relation(word_dic[i], word_dic[j]):
                        relationships.append(Relationship(label1, 'OBJ', label2))
                    if rel.obj_relation(word_dic[j], word_dic[i]):
                        relationships.append(Relationship(label1, Rev('OBJ'), label2))

        for r in relationships:
            resultNodes = graph.create(r)

if __name__ == '__main__':
    # Taking input of a sentence(s)
    query = raw_input("Enter your search query : ")
    createRelationshipWithProperties(query)
