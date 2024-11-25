print("If 9")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
if a>b:
    temp = a
    a = b
    b = temp 
    print(a, "- A")
    print(b, "- B")
elif a<b:
    temp = b
    b = a
    a = temp
    print(a, "- A")
    print(b, "- B")
    