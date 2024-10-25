print("Begin21")
import math
x1 = int(input("X1 kordinatani kiriting = "))
y1 = int(input("Y1 kordinatani kiriting = "))
x2 = int(input("X2 kordinatani kiriting = "))
y2 = int(input("Y2 kordinatani kiriting = "))
x3 = int(input("X3 kordinatani kiriting = "))
y3 = int(input("Y3 kordinatani kiriting = "))

a = math.sqrt(pow((x1-x2), 2) + pow((y1-y2),2))
b = math.sqrt(pow((x2-x3), 2) + pow((y2-y3),2))
c = math.sqrt(pow((x1-x3), 2) + pow((y1-y3),2))

p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Uchburchakning perimetri P = " , p)
print("Uchburchakning yuzi S = " , s)