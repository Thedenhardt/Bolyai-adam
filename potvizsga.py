x=(input("x:"))
y=(input("y:"))

if x > y:
    print("x a nagyobb")
else:
    print("y a nagyobb")
def kodolas(_text,_a):
    ntext =""
    for betu in text:
        if betu == a:
            ntext += str(ord(betu))
        else:
            ntext+=betu
    return ntext
text = input("mondat:")
a = input("betű:")

print(kodolas(text,a))

acc = 0
_acc = 0
with open('autok.csv','r',encoding='utf-8') as s:
     #a, feladat
    s.readline()
    cars = [lines.strip().split(';') for lines in s]
    #b, feladat
    for car in cars:
        if car[0] == 'Munkács' and car[1] == 'Záhony':
            acc += int(car[4])
    print(acc)
    #c, feladat
    for car in cars:
        if car[4]:
            _acc += int(car[4])
            average = _acc/len(cars)
    print(round(average,1))
    #d, feladat
    with open("budapestrol.dat",'w',encoding='utf-8')as f:
        for car in cars:
            if car[0] == 'Budapest':
                print(";".join(car),file=f)
