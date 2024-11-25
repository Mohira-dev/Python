print("If 10") 
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
if a!=b:
    a = a+b
    b = a+b
    print(a, "- A")
    print(b, "- B")
elif a==b:
    a = 0
    b = 0
    print(a, "- A")
    print(b, "- B")
    