print("Boolean 32")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriitng = "))
print("A, B, C uchburchak burchaklari")
print("Uchburchak to'g'ri burchak = ", (a==90 and b!=90 and c!=90) or (b==90 and a!=90 and c!=90) or (c==90 and a!=90 and b!=90))