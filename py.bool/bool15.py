print("Boolean 15")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C osnini kiriting = "))
natija = (a>0 and b>0 and c<0) or (a<0 and b>0 and c>0) or (a>0 and b<0 and c>0)
print("Faqat ikkitasi musbat = ", natija)