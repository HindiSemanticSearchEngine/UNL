import re
def mat(word):
    data_file = open("UNL_KB.txt","r")
    for line in data_file:
	if re.match("(.*)"+word,line):
		for i in line.split(")"):
		    if "(" in i:
		        print i.split("(")[-1]

