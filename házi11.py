lista=[ -14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

def elsoFeladat(lista):
    for szam in lista:
        if szam % 2 == 0:
            return True
    return False
def masodikFeladat(lista):
    return len(lista)

def harmadikFeladat(lista):
    minimum = 0
    for szam in lista:
        if szam < minimum:
            minimum = szam
    return minimum

def negyedikFeladat(lista):
    for index, szam in enumerate(lista):
        if szam % 33 == 0:
            return index

def otodikFeladat(lista):
    ossz = 0
    n = 0
    for szam in lista:
        ossz += szam
        n += 1
    return (ossz / n) / 2

def hatodikFeladat(lista):
    for szam in lista:
        if szam % 2 == 1:
            return False
    return True

def hetedikFeladat(lista):
    szam = 0
    for szam in lista:
        if szam % 2 == 1:
            szam += 1
    return szam

def nyolcadikFeladat(lista):
    elozoNegativVolt = False
    for szam in lista:
        if szam < 0:
            if elozoNegativVolt:
                return True
            elozoNegativVolt = True
    return False

def kilencedikFeladat(lista):
    utolso = 0
    for index, szam in enumerate(lista):
        if szam % 19 == 0:
            utolso = index
    return utolso

def tizedikFeladat(lista):
    ottelOszthato = []
    for szam in lista:
        if szam % 5 == 0:
            ottelOszthato.append(str(szam))
    return ottelOszthato
print(f"1. feladat: {'Van' if elsoFeladat(lista) else 'Nincs'} páros szám a sorozatban.")
print(f"2. feladat: {masodikFeladat(lista)} eleme van a sorozatnak.")
print(f"3. feladat: Legkisebb szám: {harmadikFeladat(lista)}")
print(f"4. feladat: Első 33-al osztható szám indexe: {negyedikFeladat(lista)}")
print(f"5. feladat: Számok átlagának a fele: {otodikFeladat(lista)}")
print(f"6. feladat: {'Igaz' if hatodikFeladat(lista) else 'Hamis'}, hogy minden szám pozitív.")
print(f"7. feladat: {hetedikFeladat(lista)} páratlan szám található.")
print(f"8. feladat: {'Van' if nyolcadikFeladat(lista) else 'Nincs'} olyan szám, amelyet újabb negatív szám követ.")
print(f"9. feladat: Utolsó 19-cel osztható szám indexe: {kilencedikFeladat(lista)}")
print(f"10. feladat: 5-el osztható számok: {' '.join(tizedikFeladat(lista))}")