import csv
import re


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


with open('hpc_test1.csv', newline='') as csvfile:
    file_array = list(csv.reader(csvfile))

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


current_city = 15
hometown = 16

cities = [f[current_city] for f in file_array]
cities = cities[1:-1]

towns = [f[hometown] for f in file_array]
towns = towns[1:-1]

output = []
count = {}
count2 = {}
d_sources = {}

for i in range(0, len(cities)):

	city = cities[i]
	town = towns[i]
	for state in states:
		s = re.compile("[0-9A-Za-z]*" + state + "[0-9A-Za-z]*")
		c = s.search(city)
		t = s.search(town)
		if(c != None):
			break
		if(t != None):
			break
	
	
	if(c != None):
		state = c[0]

		if(state not in count.keys()):
			count[state] = 1
		else:
			count[state] = count[state] + 1

	if(t != None):
		state = t[0]
		if(state not in count2.keys()):
			count2[state] = 1
		else:
			count2[state] = count2[state] + 1


with open('states.csv', mode='w+') as output:
	sent_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for c in states:
		if(c in count2.keys() and c in count.keys()):
			sent_writer.writerow([str(c), str(count[c]), str(count2[c])])
		if(c not in count2.keys() and c in count.keys()):
			sent_writer.writerow([str(c), str(count[c]), "0"])
		if(c not in count.keys() and c in count2.keys()):
			sent_writer.writerow([str(c),"0",str(count2[c])])
		if(c not in count.keys() and c not in count2.keys()):
			sent_writer.writerow([str(c),"0","0"])
			

