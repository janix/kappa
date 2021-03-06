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
		for j in range(len(row)):
			if (j>3) and (int(row[j]) == i):
				string[i] = row[0]+'|'
				string[i] += str(row[1])+'.'+str(row[2])+'.'+str(row[3])
				
	return string

new_data=[]
for row in data:
	new_data.append(line(row))

with open('grouping.csv', 'w', newline='') as csvout:
	writer = csv.writer(csvout, delimiter=',')
	writer.writerows(new_data[-126:])