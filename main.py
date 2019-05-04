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

index = 0
for i in range(1,number_limit,1):
    if(is_prime(i)):
        index += 1
        j = suma(suma(suma(i)))
        vector.append([str(index).zfill(3),str(i).zfill(3),j,bin(i).zfill(12)])

for item in vector:
    print(item),
    if int(item[0]) % 3 == 0:
        print("")
