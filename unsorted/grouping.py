#!/usr/bin/python3.6

import csv
data=[]
with open('wyniki-lotto.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=';')
	next(csvfile)
	for row in reader:
		data.append(row)

def line(row):
	string = []
	for i in range(50):
		string.append(str(i)+' ')
		for item in row:
			if (int(item) == i):
				string[i] = row[0]+'|'
				string[i] += str(row[1])+'.'+str(row[2])+'.'+str(row[3])
				
	return string

new_data=[]
for row in data:
	for i in range(len(row)):
		if i < 4:
			pass
		else:
#			line(row)
			new_data.append(line(row))
			break

with open('grouping.csv', 'w', newline='') as csvout:
	writer = csv.writer(csvout, delimiter=',')
	writer.writerows(new_data[-126:])