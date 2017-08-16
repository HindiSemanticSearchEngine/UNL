from format_and_get_relations import get_relations, sort_words, read_whole_file
from py2neo import Node, Relationship, Graph
from random import randint

GRAPH = Graph(password='harry123')
GRAPH.delete_all()


def make_graph(relation_list, line, trans):

    header_node = Node('Document', name=line)
    for i in xrange(0, len(relation_list)):

        word_1 = Node('Word', name=relation_list[i]['word_1'])
        trans.create(word_1)
        node_match_1 = Relationship(word_1, 'ROOT_LINE', header_node)
        trans.create(node_match_1)

        word_2 = Node('Word', name=relation_list[i]['word_2'])
        trans.create(word_2)
        node_match_2 = Relationship(word_2, 'ROOT_LINE', header_node)
        trans.create(node_match_2)

        relation = Relationship(word_1, relation_list[i]['relation'], word_2)
        trans.create(relation)


def query_graph(query):
    word_list = sort_words(query)
    relations = get_relations(word_list)
    for i in xrange(0, len(relations)):
        query_string = 'MATCH (a:Word) WHERE a.name="' + relations[i]['word_1'] + '"' + \
            ' MATCH (b:Word) WHERE b.name="' + relations[i]['word_2'] + '"' + \
            ' MATCH (doc_1:Document)-[:ROOT_LINE]-(a)' + \
            ' MATCH (doc_2:Document)-[:ROOT_LINE]-(b)' + \
            ' MATCH (a)-[:' + relations[i]['relation'] + ']-(b)' + \
            ' RETURN doc_1, doc_2'

        data = GRAPH.data(query_string)
        return data


def main():
    file_contents = read_whole_file()
    trans = GRAPH.begin()

    for i in xrange(10, 15):
        line = file_contents[i].strip()
        word_list = sort_words(line)
        relations = get_relations(word_list)
        make_graph(relations, line, trans)

    trans.commit()

    print 'Now Querying Graph'
    random_line_index = randint(10, 15)
    line = file_contents[random_line_index].strip()
    query_graph(line)


if __name__ == '__main__':
    main()
