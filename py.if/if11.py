print("If 11")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
if a!=b:
    if a>b:
        b = a
        print(a)
    elif a<b:
        a = b
        print(b)
elif a==b:
    a = 0
    b = 0
    print(a, "- A")
    print(b, "- B")