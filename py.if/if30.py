print("If 30")
a = int(input("1-999 oralig'idagi sonni kiriting = "))
if a%2==0 and a<100 and a>9:
    print("Berilgan son ikki xonali juft son")
elif a%2==1 and a<1000 and 1>99:
    print("Berilgan son uch xonali toq son")
elif a%2==1 and a<100 and a>9:
    print("Berilgan son ikki xonali toq son")
elif a%2==0 and a<1000 and a>99:
    print("Berilgan son uch xonali juft son")
elif a>0 and a<10 and a%2==1:
    print("Berilgan son bir xonali toq son")
elif a>0 and a<10 and a%2==0:
    print("Berilgan son bir xonali juft son")