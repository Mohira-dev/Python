print("Boolean 35")
print("Oraliqlar (1,8) da joylashgan butun sonlar")
x1 = int(input("Shaxmat doskasidagi X1 koordinatasini kiriting = "))
y1 = int(input("Endi Y1 koordinatasini kiriting = "))
x2 = int(input("Shaxmat doskasidagi X2 koordinatasini kiriting = "))
y2 = int(input("Endi Y2 koordinatasini kiriting = "))
natija = ((x1+y1)%2==0 and (x2+y2)%2==0) or ((x1+y1)%2==1 and (x2+y2)%2==1)
print("Berilgan maydon bir xil rangda = ", natija)