# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:00:29 2017

@author: janus
"""

import matplotlib.pyplot as plt


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

array_helper1 = []
def helper(a):
    return (a - 1)/2

file = open("output.txt", 'w')
previous1=0
previous2=0
primes_range = 400000
try:
    for i in range(primes_range):
        if(is_prime(i)):
            diff1 = i - previous1
            previous1 = i
            array_helper1.append(diff1)
            diff2 = helper(i) - previous2
            previous2 = helper(i)
#            input()
#            print(str(bin(i)).lstrip('-0b').zfill(15))
#            file.write(str(bin(i)).lstrip('-0b').zfill(15) + ' ' + str(i).zfill(4) + ' ' + str(diff))
            file.write(str(i).zfill(4) + '\t' + str(diff1) + '\t' + str((i-1)/2) + '\t\t' + str(bin(int(diff2))).lstrip('-0b').zfill(4))
            file.write('\n')
    file.close()

except KeyboardInterrupt:
    pass

#print(array_helper1)
plt.hist(array_helper1)
plt.title("Primes range {}".format(primes_range))
plt.xlabel("Difference")
plt.ylabel("Frequency")

plt.show()
    

#print(array_primes)
#print(array_diff)    