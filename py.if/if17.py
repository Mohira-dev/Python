print("If 17")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
if a<b and b<c:
    print("Sonlar o'sish tartibida ikkilansin A = ", 2*a)
    print("Sonlar o'sish tartibida ikkilansin B = ", 2*b)
    print("Sonlar o'sish tartibida ikkilansin C = ", 2*c)
elif c<b and b<a:
    print("Sonlar kamayish tartibida ikkilansin A = ", 2*a)
    print("Sonlar kamayish tartibida ikkilansin B = ", 2*b)
    print("Sonlar kamayish tartibida ikkilansin C = ", 2*c)
else:
    print("Sonlar ishora o'zgarsin A = ", a*(-1))
    print("Sonlar ishora o'zgarsin B = ", b*(-1))
    print("Sonlar ishora o'zgarsin C = ", c*(-1))