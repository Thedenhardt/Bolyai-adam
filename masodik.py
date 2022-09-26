


print("a.)"," feladat:")
print("-"*20)
a = 2.7
b = 50
c = a / b

a2 = 7.9
b2 = 90
c2 = a2 / b2

a3 = 29.7
b3 = 130
c3 = a3 / b3

h=round(c+c2+c3,2)
h2= int((c+c2+c3)*60)
print("A szükséges idő az egyetemig:"   ,end=" ")
print(round(c+c2+c3,2),"óra")
print()
print("b.) feladat: ")
print("-"*20)
print("A szükséges idő az egyetemig:"   ,end=" ",)
print(round(int(h*60,)),"perc" ,)
print()
print("c.) feladat: ")
print("-"*20)
print("Az indulási idő:" ,end=" ")
print("07:",60-h2,sep="")


