print("Begin34")
x = int(input("Necha kg shokolad olshingizni kiritng = "))
a = int(input("Shu olgan shokoladingiz necha so'm turishini kiriting = "))
y = int(input("Endi necha kg konfet olshingizni kiriting = "))
b = int(input("Ana endi shu olgan konfetingiz necha so'm turishini kiriting = "))
bir_kg_sh = int(a/x)
bir_kg_k = int(b/y)
print("1 kg shokolad 1 kg konfetdan qanchaha qimmatligini aniqlash uchun = " ,  abs(bir_kg_sh - bir_kg_k))