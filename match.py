import re

data_file = open("UNL_KB.txt","r")
word=[]
r = raw_input("Enter the word to find matching word\n")
for line in data_file:
	if re.match("(.*)"+r,line):
		for i in line.split(")"):
			if "(" in i:
				print i.split("(")[-1]

