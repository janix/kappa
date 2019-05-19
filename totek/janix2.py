#!/usr/bin/python3.6

with open('dl_razem.txt','r') as fin:
    data = fin.readlines()

tmp=['  ' for x in range(49)]
new_data=[]

for n in range(len(data)):
    data[n] = data[n].split(' ',2)
    data[n][2] = data[n][2].split(',',5)
    data[n][2][5] = data[n][2][5].strip()
    data[n].append(tmp)

    for j in data[n][2]:
        k = 0
        while (k < 49): 
            if k == int(j)-1:
                data[n][3][k] = j.zfill(2)
            else:
                data[n][3][k] = '  '
            k+=1

print(data[:][3])
