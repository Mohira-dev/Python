print("Boolean 39")
print("Oraliqlar (1,8) da joylashgan butun sonlar")
x1 = int(input("Shaxmat doskasidagi X1 koordinatasini kiriting = "))
y1 = int(input("Endi Y1 koordinatasini kiriting = "))
x2 = int(input("Shaxmat doskasidagi X2 koordinatasini kiriting = "))
y2 = int(input("Endi Y2 koordinatasini kiriting = "))
print("Farzin ikkinchi joyga ham o'ta oladi = ", abs(x2-x1)==abs(y2-y1) or x1==x2 or y1==y2)