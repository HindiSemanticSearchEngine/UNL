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
        if w1['pos_tag'] == 'VM' and w2['pos_tag']=='QF':
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


    '''
    def and_relation(self, w1, w2):
        if w1['nxt'] == 'CC' and w2['prv'] == 'CC':
            if w1['pos_tag'] == 'NN' and w2['']
    '''
