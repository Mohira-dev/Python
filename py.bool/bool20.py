print("Boolean 20")
a = int(input("A sonini kiriting = "))
birlik = a%10
onlik = a//10%10
yuzlik = a//100
natija = birlik!=onlik and onlik!=yuzlik and birlik!=yuzlik
print("Shu sonning barcha raqamlari xar hil = ", natija)