#!/usr/bin/python3.6

import csv
data=[]
with open('wyniki-lotto.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=';')
	next(csvfile)
	for row in reader:
		data.append(row)

def line(item):
	string = []
	for i in range(51):
		string.append('  ')
		if (int(item) == i):
			string[i] = str(i).zfill(2)
		else:
			pass
	return string

new_data=[]
for row in data:
	for i in range(len(row)):
		if i < 4:
			pass
		elif (i == 3):
			new_data.append('  ')
		else:
			new_data.append(line(row[i]))

with open('formatted.csv', 'w', newline='') as csvout:
	writer = csv.writer(csvout, delimiter=',')
	writer.writerows(new_data[-162:])