print("If 12")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
if a>b and c>b:
    print(b, "- Kichigi B")
elif a>c and b>c:
    print(c, "- Kichigi C")
else:
    print(a, "- Kichigi A")