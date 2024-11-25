print("If 21")
x = int(input("X ni kiriting = "))
y = int(input("Y ni kiriting = "))
if x == 0 and y == 0:
    print(0)
elif (x!=0 and y==0) or (x==0 and y!=0):
    x=1
    y=2
    print(x)
    print(y)
elif x!=0 and y!=0:
    print(3)