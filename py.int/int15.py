print("Integer15")
a = int(input("Uch xonali sonni kiriting = "))
print("Shu sonni o'nliklar xonasidagi raqam bilan yuzliklar xonasidagi raqamni almashtrish orqali hosil bo'lgan sonni aniqlang  (123, 213)= " +str(int(a/10%10)) + str(int(a/100)) + str(int(a%10)))