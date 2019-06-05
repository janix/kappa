#!/usr/bin/python3.7
import csv
data=[]

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

number_limit = 1200

i=1
while i < number_limit:
  if(is_prime(i)):
    data.append(i)
    data.append(suma(i))
    data.append(suma(suma(i)))
    data.append("|")
  i+=1    
      


print(data)
with open('primes.csv', 'w') as csvout:
  writer = csv.writer(csvout, delimiter=',')
  writer.writerow(data)