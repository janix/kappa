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

i = 1

def test8(i):
    return int(base(i, 10, 8, string=True))

def test9(i):
    return int(base(i, 10, 9, string=True))

def reduction(i):
    return suma(suma(suma(suma(i))))

while i < number_limit:
    if(is_prime(i)):
        print(i, test8(i),reduction(test8(i)),"+")
    else:
        print(i, test8(i),reduction(test8(i)))
    i += 1
