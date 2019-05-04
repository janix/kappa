#!/usr/bin/python

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

number_limit = 1000
vector = []

for i in range(4,number_limit,1):
    if(is_prime(i)):
        j = suma(suma(suma(i)))
        vector.append([i,j])

#for n in range(1,9,1):
#    for item in vector:
#        if item[1] == n:
#            print item

index = 0
for item in vector:
    index += 1
    print (item[1]),
    if index % 6 == 0:
        print(" ")

#print(vector)
