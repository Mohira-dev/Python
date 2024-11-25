print("If 28")
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("Bu yilda 366 kun bor (Kabisa yili)")
else:
    print("Bu yilda 365 kun bor (Kabisa yili emas)")