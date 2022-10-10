from itertools import *
def virat(str):
     k= permutations(str)
     for i in list(k):
         print (''.join(i))
str=input()
virat(str)