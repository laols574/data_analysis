import csv
import re

with open('AG_150.csv', newline='') as csvfile:
    file_array = list(csv.reader(csvfile))

with open('hpc_test1.csv', newline='') as csvfile:
    info_array = list(csv.reader(csvfile))

type = 5
#type = 2
type_confidence = 6
counterspeech = 7
counterspeech_confidence = 8
source = 11
text = 12


info_text = 3
info_reaction = 4
info_likes = 5
info_ahah = 7
info_love = 8
info_wow = 9
info_sigh = 10
info_grr = 11
info_gender = 13
info_birthday = 14
info_city = 15
info_home = 16
info_work = 17
info_education = 18
info_interest = 19

cs_confidences = [f[counterspeech_confidence] for f in file_array]
cs_confidences = cs_confidences[1:-1]

#type_confidences = [f[type_confidence] for f in file_array]
#type_confidences = type_confidences[1:-1]
type_confidences = cs_confidences

types = [f[type] for f in file_array]
types = types[1:-1]

corpus = [f[text] for f in file_array]
corpus = corpus[1:-1]

info_corpus = [f[info_text] for f in info_array]
info_corpus = info_corpus[1:-1]

sources = [f[source] for f in file_array]
sources = sources[1:-1]

counterspeeches = [f[counterspeech] for f in file_array]
counterspeeches = counterspeeches[1:-1]

info_genders = [f[info_gender] for f in info_array]
info_genders = info_genders[1:-1]

info_reactions = [f[info_reaction] for f in info_array]
info_reactions = info_reactions[1:-1]

info_likesa = [f[info_likes] for f in info_array]
info_likesa = info_likesa[1:-1]

info_ahaha = [f[info_ahah] for f in info_array]
info_ahaha = info_ahaha[1:-1]

info_loves = [f[info_love] for f in info_array]
info_loves = info_loves[1:-1]

info_wows = [f[info_wow] for f in info_array]
info_wows = info_wows[1:-1]

info_sighs = [f[info_sigh] for f in info_array]
info_sighs = info_sighs[1:-1]

info_grrs = [f[info_grr] for f in info_array]
info_grrs = info_grrs[1:-1]

info_educations = [f[info_education] for f in info_array]
info_educations = info_educations[1:-1]

info_e = []

for e in info_educations:
	hs = re.compile("[0-9A-Za-z]*[H-h]igh [S-s]chool[0-9A-Za-z]*")
	c = re.compile("[0-9A-Za-z]*[C-c]ollege[0-9A-Za-z]*")
	u = re.compile("[0-9A-Za-z]*[U-u]niversity[0-9A-Za-z]*")
	hs_s = hs.search(e)
	c_s = c.search(e)
	u_s = u.search(e)
	if(hs_s != None):
		info_e.append(hs_s[0])
	if(u_s != None):
		info_e.append(u_s[0])
	if(c_s != None):
		info_e.append(c_s[0])
	else:
		info_e.append("none")

output = []
for i in range(0, len(corpus)):
	entry = {}
	for j in range(0, len(info_corpus)):
		if(corpus[i] == info_corpus[j]):
			entry["gender"] = info_genders[j]
			entry["reactions"] = info_reactions[j]
			entry["likes"] = info_likesa[j]
			entry["ahah"] = info_ahaha[j]
			entry["wow"] = info_wows[j]
			entry["grr"] = info_grrs[j]
			entry["love"] = info_loves[j]
			entry["sigh"] = info_sighs[j]
			entry["education"] = info_e[j]

	entry["type_confidence"] = type_confidences[i]
	entry["cs_confidence"] = cs_confidences[i]
	entry["counterspeech"] = counterspeeches[i]
	entry["type"] = types[i]
	entry["text"] = corpus[i]
	entry["source"] = sources[i]
	output.insert(i, entry)

#len_f = len(filename) - 4
#out_file = filename[0:len_f] 
file = open("ag150.out", "w+")

file.write(str(output))

file.close()

