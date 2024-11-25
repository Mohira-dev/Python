print("If 18")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
if a == b:
    print("A va B sonlari o'zaro teng, C soni esa uchinchi bo'lib kiritiladi C = ", c)
elif a==c:
    print("A va C sonlari o'zaro teng, B soni esa ikkinchi bo'lib kiritiladi B = ", b)
elif b == c:
    print("B va C sonlari o'zaro teng, C soni esa birinchi bo'lib kiritiladi A = ", a)