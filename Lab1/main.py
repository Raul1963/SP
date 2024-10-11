from math import perm,factorial,comb
from itertools import permutations,combinations,islice,combinations_with_replacement
from more_itertools import distinct_permutations
import random

print(list(permutations("SICHER")))
print(len(list(permutations("SICHER"))))

print(list(islice(permutations("SICHER"),2)))

print(list(permutations("SICHER",2)))
print(len(list(permutations("SICHER",2))))

print(len(list(permutations("MATHE",3))))

print(list(combinations("MATHE",3)))
print(len(list(combinations("MATHE",3))))

M=list(distinct_permutations("AABB"))
print(M)
...
m=len(M)
print("Anzahl Permutationen von AABB mit Wiederholung:",m)

for p in distinct_permutations("1112"):
    print("".join(p))
n=len(list(distinct_permutations("1112")))
print("Anzahl Permutationen von 1112 mit Wiederholung:",n)

print("Alle Kombinationen von ABC je 2, mit Wiederholung")
print(list(combinations_with_replacement("ABC",2)))
k=len(list(combinations_with_replacement("ABC",2)))
print("Anzahl Kombinationen von ABC je 2 mit Wiederholung:",k)

print(len(list(combinations_with_replacement([1,2,3,4],6))))
print(list(combinations_with_replacement([1,2,3,4],6)))