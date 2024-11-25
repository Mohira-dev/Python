print("If 22")
x = int(input("X koordinata o'qini kiriitng = "))
y = int(input("Y koordinata o'qini kiriitng = "))
print("X va Y koordinati o'qlari birlashmasi a nuqtani tashlik qiladi")
if x!=0 and y!=0:
    if x>0 and y>0:
        print("Birinchi chorakda yotadi")
    elif x<0 and y>0:
        print("Ikkinchi chorakda yotadi")
    elif x<0 and y<0:
        print("Uchinchi chorakda yotadi")
    elif x>0 and y<0:
        print("To'rtinchi chorakda yotadi")