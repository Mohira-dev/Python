print("Boolean 22")
a = int(input("A sonini kiriting = "))
birlik = a%10
onlik = a//10%10
yuzlik = a//100
natija = (yuzlik<onlik<birlik) or (yuzlik>onlik>birlik)
print("Raqamlar ketma-ketligi o'suvchi yoki kamayuvchi tartibda bo'lsin = ", natija)
