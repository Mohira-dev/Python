print("If 19")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
d = int(input("D sonini kiriitng = "))
if a == b and b ==c:
    print("A, B va C sonlari o'zaro teng, D soni esa to'rtinchi bo'lib kiritiladi D = ", d)
elif a == c and c == d:
    print("A, C va D sonlari o'zaro teng, B soni esa ikkinchi bo'lib kiritiladi B = ", b)
elif b == c and c == d:
    print("B, C va D sonlari o'zaro teng, A soni esa birinchi bo'lib kiritiladi A = ", a)
elif a == b and b == d:
    print("A, B va D sonlari o'zaro teng, C soni esa uchinchi bo'lib kiritiladi C = ", c)