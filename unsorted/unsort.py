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
		if i < 3:
			pass
		elif (i == 3):
			new_data.append(row)
		else:
			new_data.append(line(row[i]))


with open('formatted.csv', 'w', newline='') as csvout:
	writer = csv.writer(csvout)
	writer.writerows(new_data)