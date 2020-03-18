import csv
import statistics

# Program to find most frequent
# element in a list
# geeksforgeeks

def most_frequent(l):
    counter = 0
    num = l[0]

    for i in l:
        curr_frequency = l.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num, counter


with open('download.csv', newline='') as csvfile:
    file_array = list(csv.reader(csvfile))

counterspeech = 30
time = 23
text = 28
source = 27

corpus = [f[text] for f in file_array]
corpus = corpus[1:-1]

sources = [f[source] for f in file_array]
sources = sources[1:-1]

counterspeeches = [f[counterspeech] for f in file_array]
counterspeeches = counterspeeches[1:-1]

times = [f[time] for f in file_array]
times = times[1:-1]

output = []
dict = {}
d_sources = {}
tdict = {}

for i in range(0, len(corpus)):

	word = corpus[i]
	cs = counterspeeches[i]
	t = times[i]
	if( word not in dict.keys()):
		dict[word] = [cs]
		d_sources[word] = sources[i]
		tdict[word] = [int(t)]
	else:
		dict[word] = dict[word] + [cs]
		tdict[word] = tdict[word] + [int(t)]

m_con = {}
for d in dict:
	timeout = statistics.mean(tdict[d]) 
	type, count = most_frequent(dict[d])
	con = count / len(dict[d])

	m_con[d] = [timeout, type]

print(len(m_con))

with open('AGBIG_annotation.csv', mode='w+') as output:
	sent_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for c in dict:
		if(str(m_con[c][1]) == "Not Counterspeech"):
			sent_writer.writerow(["no", str(c)])
		else:
			sent_writer.writerow([ "yes", str(c)])
	
