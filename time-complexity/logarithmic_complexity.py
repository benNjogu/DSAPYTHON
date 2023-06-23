# An algorithm is o(logn) if it takes a constant time to cut the problem size by a fraction(usually 1/2).

def Logarithms(n):
    i = 1
    while i < n: # n/2 times
        i = i * 2 # constant time
        print(i) # constant time

Logarithms(10)

def _Logarithms(n):
    i = n
    while i >= 1: # n/2 times
        i = i / 2 # constant time
        print(i) # constant time

_Logarithms(10)