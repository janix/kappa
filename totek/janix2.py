#!/usr/bin/python3.6

with open('dl_razem.txt','r') as fin:
    data = fin.readlines()

tmp=['  ' for x in range(49)]
new_data=[]

for n in range(len(data)):
    data[n] = data[n].split(' ',2)
    data[n][2] = data[n][2].split(',',5)
    data[n].append(tmp)

for i in range(len(data)):
    for j in range(0,6,1):
        k = 0
        while (k < 49): 
            if k == int(data[i][2][j])-1:
                data[i][3][k] = data[i][2][j].zfill(2)
            else:
                pass
            k+=1

print(data[2][3])
