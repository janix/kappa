#!/usr/bin/python3.7

from baseconvert import base

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def suma(g):
    sum = 0
    while g > 0:
        d = g%10
        g = g//10
        sum += d
    return sum

number_limit = 300
vector = []

index = 0
for i in range(1,number_limit,1):
    if(is_prime(i)):
        index += 1
#       j = suma(suma(suma(i)))
#       vector.append([index,i,j, base(i,10,9)])
        vector.append(i)

item = 0
while item < len(vector) - 3:
#    var = vector[item] + vector[item+3]
#    print(var, end=" ")
    prime = vector[item]
    j = suma(suma(suma(suma(vector[item]))))
    j3 = suma(suma(suma(suma(vector[item+3]))))
    nine = int(base(vector[item], 10, 9, string=True))
    eight = int(base(vector[item], 10, 8, string=True))
    seven = int(base(vector[item], 10, 7, string=True))
    six = int(base(vector[item], 10, 6, string=True))
    i_nine = int(base(item+1, 10, 9, string=True))
    i_eight = int(base(item+1, 10, 8, string=True))
    i_seven = int(base(item+1, 10, 7, string=True))
    i_six = int(base(item+1, 10, 6, string=True))
    l = suma(suma(suma(suma(int(nine)))))
    diff1 = vector[item+1] - vector[item]
    diff2 = vector[item+2] - vector[item]
    diff3 = vector[item+3] - vector[item]
    i_ten = item+1
    test = nine + int(base(vector[item+3], 10, 9, string=True))
    test2 = vector[item] + vector[item+1]
    test3 = vector[item] + vector[item+2]
    test4 = vector[item] + vector[item+3]
    test5 = int(base(vector[item+1], 10, 9, string=True))
    test6 = int(base(vector[item+2], 10, 9, string=True))
    test7 = int(base(vector[item+3], 10, 9, string=True))-nine
    test9 = int(base(vector[item+3], 10, 9, string=True))

#    print("[",item+1,prime,l,diff,k-prime,"]",end=" ")
#    print(j,end=" ")
#    print("[", i_ten,prime,"|",nine,"]", test2,test3,test4)
#    if item%3 == 0:
#        print("")
    print(prime,nine,nine-vector[item+3])
    
    item += 1
