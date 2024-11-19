print("Boolean 21")
a = int(input("A sonini kiriting = "))
birlik = a%10
onlik = a//10%10
yuzlik = a//100
natija = (yuzlik<onlik<birlik)
print("Shu sonning raqamlari ketma-ket o'suvchi tartibda bo'lsin = ", natija)
