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

number_limit = 201

i = 1

def test(i,b):
    return int(base(i, 10, b, string=True))

def reduction(i):
    return suma(suma(suma(suma(i))))
def mark_prime(i):
    if(is_prime(i)):
        return "*"
    else:
        return ""
def n6(i):
    if (i%6==1):
        return "+"
    elif (i%6==5):
        return "-"
    else:
        return ""
def n5(i):
    if (i%5==0):
        return "|"
    else:
        return ""

while i < number_limit:
    print(i,n6(i),mark_prime(i))
    i += 1
