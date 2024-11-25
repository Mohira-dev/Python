print("If 13")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
if (a>b and b>c) or (c>b and b>a):
    print(b, "- O'rtanchasi B")
elif (a>c and c>b) or (b>c and c>a):
    print(c, "- O'rtanchasi C")
elif (b>a and a>c) or (c>a and a>b):
    print(a, "- O'rtanchasi A")