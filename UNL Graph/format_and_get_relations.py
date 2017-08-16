from root_postag import rootword_and_postag
from relation import Relations


def read_whole_file():
    with open('./test_queries.txt') as test_file:
        file_contents = test_file.read()
        file_contents = file_contents.split('\n')

        return file_contents


def get_line_index(index):
    with open('./test_queries.txt') as test_file:
        file_contents = test_file.read()
        file_contents = file_contents.split('\n')
        first_line = file_contents[index].strip()

        return first_line


def sort_words(line):
    root_words, pos_tags = rootword_and_postag(line)
    word_list = []
    for i in xrange(0, len(root_words)):
        word_map = {
            'pos_tag': pos_tags[i],
            'word': root_words[i]
        }
        word_list.append(word_map)
    return word_list


def get_relations(word_list):
    word_relations_list = []
    relation = Relations()
    for i in xrange(0, len(word_list)):
        for j in xrange(i + 1, len(word_list)):

            result = relation.qua_relation(word_list[i], word_list[j])
            if result:
                word_relations_list.append({
                    'word_1': word_list[i]['word'],
                    'word_2': word_list[j]['word'],
                    'relation': 'QUA'
                })

            result = relation.dur_relation(word_list[i], word_list[j])
            if result:
                word_relations_list.append({
                    'word_1': word_list[i]['word'],
                    'word_2': word_list[j]['word'],
                    'relation': 'DUR'
                })

            result = relation.agt_relation(word_list[i], word_list[j])
            if result:
                word_relations_list.append({
                    'word_1': word_list[i]['word'],
                    'word_2': word_list[j]['word'],
                    'relation': 'AGT'
                })

            result = relation.aoj_relation(word_list[i], word_list[j])
            if result:
                word_relations_list.append({
                    'word_1': word_list[i]['word'],
                    'word_2': word_list[j]['word'],
                    'relation': 'AOJ'
                })

            result = relation.nam_relation(word_list[i], word_list[j])
            if result:
                word_relations_list.append({
                    'word_1': word_list[i]['word'],
                    'word_2': word_list[j]['word'],
                    'relation': 'NAM'
                })

            result = relation.obj_relation(word_list[i], word_list[j])
            if result:
                word_relations_list.append({
                    'word_1': word_list[i]['word'],
                    'word_2': word_list[j]['word'],
                    'relation': 'OBJ'
                })

    return word_relations_list


def main():
    line = get_line_index(0)
    word_list = sort_words(line)
    print get_relations(word_list)


if __name__ == '__main__':
    main()
