print("Boolean 37")
print("Oraliqlar (1,8) da joylashgan butun sonlar")
x1 = int(input("Shaxmat doskasidagi X1 koordinatasini kiriting = "))
y1 = int(input("Endi Y1 koordinatasini kiriting = "))
x2 = int(input("Shaxmat doskasidagi X2 koordinatasini kiriting = "))
y2 = int(input("Endi Y2 koordinatasini kiriting = "))

print("Shoh maydonni ikkinchi tomoniga o'ta oladi = ", (y2 == y1 and (x2 == x1 + 1 or x2 == x1 -1)) or (y2 == y1 + 1 and (x2 == x1 or x2 == x1-1 or x2 == x1+1)) or (y2 == y1-1 and (x2==x1 or x2 == x1-1 or x1 == x1+1)))