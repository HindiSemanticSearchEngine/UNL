# -*- coding: UTF-8 -*-

class Relations:
    '"Class for identifying unl relation between two words"'


    def qua_relation(self, w1, w2):
    	if w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'QF':
    		return True

    	elif w1['pos_tag'] == 'NST' and w2['pos_tag'] == 'QF':
    		return True

    	elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'QF':
    		return True

    	else:
    		return False


    def dur_relation(self, w1, w2):
        if w1['pos_tag'] == 'VM' and w2['pos_tag'] == 'QF':
            return True

        elif w1['pos_tag'] == 'VAUX' and w2['pos_tag'] == 'QF':
            return True

        else:
            return False


    def agt_relation(self, w1, w2):
        if w1['pos_tag'] == 'VM' and w2['pos_tag']=='NN':
            return True

        elif w1['pos_tag'] == 'VM' and w2['pos_tag'] == 'NNP':
            return True

        elif w1['pos_tag'] == 'VM' and w2['pos_tag'] == 'PRP':
            return True

        elif w1['pos_tag'] == 'VAUX' and w2['pos_tag'] == 'NNP':
            return True

        elif w1['pos_tag'] == 'VAUX' and w2['pos_tag'] == 'PRP':
            return True

        elif w1['pos_tag'] == 'VAUX' and w2['pos_tag'] == 'NN':
            return True

        else:
            return False


    def aoj_relation(self, w1, w2):
        if w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'PRP':
            return True

        elif w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'PRP':
            return True

        elif w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'JJ':
            return True

        else:
            return False


    def and_relation(self, w1, w2, w3):
        if w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'CC' and  w3['pos_tag'] == 'NN':
            return True

        elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'NNP':
            return True

        elif w1['pos_tag'] == 'RB' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'RB':
            return True

        elif w1['pos_tag'] == 'JJ' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'JJ':
            return True

        else:
            return False


    def nam_relation(self, w1, w2):
        if w1['pos_tag'] == 'NN' and  w2['pos_tag'] == 'NNP':
            return True

        elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'PRP':
            return True

        else:
            return False


    def obj_relation(self, w1, w2):
        if w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'VM':
            return True

        elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'VM':
            return True

        elif w1['pos_tag'] == 'VAUX' and w2['pos_tag'] == 'NNP':
            return True

        else:
            return False


    def ant_relation(self, sentence):
        if 'नहीं' not in l:
            return False

        for i in l:
            for j in l:
                if i!=j:
                    if i['pos_tag'] == 'NN' and j['pos_tag'] == 'NN':
                        return True

                    elif i['pos_tag'] == 'PRP' and j['pos_tag'] == 'PRP':
                        return True

                    elif i['pos_tag'] == 'JJ' and j['pos_tag'] == 'JJ':
                        return True

                    else:
                        return False


    def or_relation(self, w1, w2, w3):
        if w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'CC' and  w3['pos_tag'] == 'NN':
            return True

        elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'NNP':
            return True

        elif w1['pos_tag'] == 'RB' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'RB':
            return True

        elif w1['pos_tag'] == 'JJ' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'JJ':
            return True

        elif w1['pos_tag'] == 'INJ' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'NEG':
            return True

        elif w1['pos_tag'] == 'VV' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'JJ':
            return True

        else:
            return False
