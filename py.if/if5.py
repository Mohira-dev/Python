print("If 5")
a = int(input("A sonini kiriting = "))
b = int(input("B sonini kiriting = "))
c = int(input("C sonini kiriting = "))
counter = 0
if a > 0:
    counter += 1
if b > 0:
    counter += 1
if c > 0:
    counter += 1
print(counter, "- Musbat sonlar qanchaligi")
sum = 0
if a < 0:
    sum += 1
if b < 0:
    sum += 1
if c < 0:
    sum += 1
print(sum, "- Manfiy sonlar qanchaligi")