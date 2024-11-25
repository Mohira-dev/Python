print("If 20")
a = int(input("Sonlar o'qidagi A nuqtani  kiriting = "))
b = int(input("Sonlar o'qidagi B nuqtani  kiriting = "))
c = int(input("Sonlar o'qidagi C nuqtani  kiriting = "))
farq = abs(a-b)
farq1 = abs(a-c)
if farq > farq1:
    print("A nuqtaga yaqin nuqta C va uni orasidagi masofa = ", farq1)
elif farq1 > farq:
    print("A nuqtaga yaqin nuqta B va uning orasidagi masofa = ", farq)