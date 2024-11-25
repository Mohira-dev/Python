print("If 14")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
if a>b and c>b:
    print(b, "- Kichigi ")
    if a>c:
        print(a, "- Kattasi ")
    elif c>a:
        print(c, "- Kattasi ")
elif a>c and b>c:
    print(c, "- Kichigi ")
    if a>b:
        print(a, "- Kattasi ")
    elif b>a:
        print(b, "- Kattasi ")
else:
    print(a, "- Kichigi ")
    if b>c:
        print(b, "- Kattasi ")
    elif c>b:
        print(b, "- Kattasi ")