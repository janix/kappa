# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:00:29 2017

@author: janus
"""

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
#   print ('\t',f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

array_primes = []
array_diff = []

file = open("output.txt", 'w')
tmp_file = open("tmp_file.txt", 'w')
previous=0
for i in range(10000):
    if(is_prime(i)):
        diff = i - previous
        previous = i
        array_primes.append(i)
        array_diff.append(diff)
        file.write(str(i) + ':' + str(bin(i)).lstrip('-0b').zfill(16) + '\t')
        file.write(str(diff))
        file.write('\t')
        tmp_file.write(str(bin(i)).lstrip('-0b').zfill(16) + ' ')
file.close()

#print(array_primes)
#print(array_diff)    