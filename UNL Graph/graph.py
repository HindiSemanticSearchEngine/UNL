from format_and_get_relations import get_relations, sort_words, read_whole_file
from py2neo import Node, Relationship, Graph

GRAPH = Graph(password='harry123')
# GRAPH.delete_all()


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


def save_graph():
    file_contents = read_whole_file()
    trans = GRAPH.begin()

    for i in xrange(0, len(file_contents)):
        line = file_contents[i].strip()
        word_list = sort_words(line)
        relations = get_relations(word_list)
        make_graph(relations, line, trans)

    trans.commit()


def query_graph(query):
    word_list = sort_words(query)
    relations = get_relations(word_list)

    results = []
    for i in xrange(0, len(relations)):
        query_string = 'MATCH (a:Word) WHERE a.name="' + relations[i]['word_1'] + '"' + \
            ' MATCH (b:Word) WHERE b.name="' + relations[i]['word_2'] + '"' + \
            ' MATCH (doc_1:Document)-[:ROOT_LINE]-(a)' + \
            ' MATCH (doc_2:Document)-[:ROOT_LINE]-(b)' + \
            ' MATCH (a)-[:' + relations[i]['relation'] + ']-(b)' + \
            ' RETURN doc_1.name, doc_2.name'

        data = GRAPH.data(query_string)
        results.append(data)

    return results


def word_compare(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        return 0
    else:
        return 1


def main():
    print 'Now Querying Graph'
    line = raw_input('Enter a line: ')
    data = query_graph(line)

    frequency = dict()
    for i in xrange(0, len(data)):
        for item in data[i]:

            if item['doc_1.name'] in frequency:
                frequency[item['doc_1.name']] += 1
            else:
                frequency[item['doc_1.name']] = 1

            if item['doc_2.name'] in frequency:
                frequency[item['doc_2.name']] += 1
            else:
                frequency[item['doc_2.name']] = 1

    frequency_list = [(k, v) for k, v in frequency.items()]
    frequency_list.sort(word_compare)

    print 'The documents in most frequent order is:'
    for i in xrange(0, len(frequency_list)):
        print 'Document: ' + frequency_list[i][0] + ', Frequency: ' + str(frequency_list[i][1])


if __name__ == '__main__':
    main()
