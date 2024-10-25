print("Begin39")
import math
a = int(input("Nolga teng bo'lmagan A koeffisentini kiriting = "))
b = int(input("B koeffitsentini kiriting = "))
c = int(input("Endi C koeffitsentini kiriting = "))
d = math.sqrt(b*b-(4*a*c))
print("Ax2+bx+c=0 tenglamaning diskeriminanti 0 dan katta bo'lsa, 1-yechimi aniqlansin = ", str(int((-b+d)/2*a)))
print("Ana endi 2-yechimi  = " + str(int((-b-d)/2*a)))