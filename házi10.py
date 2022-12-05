t1 = [-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
count = 0
even= 0
max = 0
ten = []
all = 0
th = 0
index = -1
for i in range(len(t1)):
    count += 1
print("1. ", count, "szám van a listában.")
for j in t1:
    if j < 0:
        print("2. ","Van negatív szám.")
        break
for k in t1:
    if k % 2 == 0:
        even += 1
print("3. ",even,"páros szám van a listában.")
max = t1[0]
for elem in t1:
    if elem > max:
        max = elem
print("4. ",max,"a lista legnagyobb értéke.")
for l in t1:
    if l % 10 == 0:
        ten.append(l)
print("5. ","Tízzel osztható számok:",ten)
for g in t1:
    index+=1
    if g % 29 == 0:
        print("6. ",g,"a legelső 29-el osztható szám, indexe:",index)
        break
for t in t1:
    if t % 2 != 0:
        print("7. ","Nem minden szám páros.")
        break
for n in t1:
    all+=n
print("8. ",all/count, "a számok átlaga.")

index =- 1
for m in t1:
    index += 1
    if m % 17 == 0:
        th = m
if th == 0:
    print("10. ","Nincs 17-tel osztható szám")
else:
    print("10. ",th, "a legutolsó 17-tel osztható szám, az indexe:", index)
