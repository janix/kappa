#!/usr/bin/python3.6

with open('dl.txt','r') as fin:
    data = fin.readlines()

n = 0
substring=[]
while n < len(data):
    data[n] = data[n].split(' ',2)
    substring.append(data[n][2]) 
    n+=1
s = 0
while s < len(substring):
    substring[s] = substring[s].split(',',5)    
    substring[s][5] = str(substring[s][5]).strip() 
    s+=1
print(len(substring))

reformated_data = [['  ' for x in range(50)] for y in range(len(substring))]
print(len(reformated_data))

for i in range(len(substring)):
    for j in range(0,6,1):
        k = 0
        while (k < 49):
            if k == int(substring[i][j])-1:
                reformated_data[i][k] = substring[i][j].zfill(2)
            else:
                pass
            k+=1

with open('newfile.txt','w') as fout:
    for i in range(len(reformated_data)):
#        reformated_data[i] = str(reformated_data[i]).strip().replace(',','')
        lst = map(str,reformated_data[i])
        line = ",".join(lst)
        fout.write(line)
        fout.write("\n")






