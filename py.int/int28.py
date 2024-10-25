print("Integer28")
k = int(input("1 va 365 oralig'ida son kiriting: "))
n = int(input("1 yanvar qaysi hafta kuniga to'g'ri kelishini bilish uchun son kiriting: "))
print("  " + str((k % 7 + n-1)%7))