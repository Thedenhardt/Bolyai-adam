def fajlOlvas():
    autok = []
    with open('autok.txt', 'r', encoding='utf-8') as f:
        fejlecek = f.readline().strip().split("\t")
        for sor in f:
            adat = sor.strip().split("\t")
            szotar = {}
            for index, adatDarab in enumerate(adat):
                szotar[fejlecek[index]] = adatDarab
            autok.append(szotar)
    return autok

def elsoFeladat(autokLista):
    tulajok = []
    for auto in autokLista:
        if auto['tulajdonos'] in tulajok:
            return True
        tulajok.append(auto['tulajdonos'])
    return False

def autoOsszehasonlit(auto1, auto2):
    auto1adatok = auto1['forgalomba'].split('.')
    auto2adatok = auto2['forgalomba'].split('.')
    if int(auto1adatok[0]) < int(auto2adatok[0]):
        return auto1
    elif int(auto1adatok[0]) > int(auto2adatok[0]):
        return auto2
    elif int(auto1adatok[1]) < int(auto2adatok[1]):
        return auto1
    elif int(auto1adatok[1]) > int(auto2adatok[1]):
        return auto2
    elif int(auto1adatok[2].split(' ')[0]) < int(auto2adatok[2].split(' ')[0]):
        return auto1
    elif int(auto1adatok[2].split(' ')[0]) > int(auto2adatok[2].split(' ')[0]):
        return auto2

def masodikFeladat(autokLista):
    legregebbiAuto = autokLista[0]
    for auto in autokLista[1:]:
        legregebbiAuto = autoOsszehasonlit(legregebbiAuto, auto)
    return legregebbiAuto

def harmadikFeladat(autokLista):
    autok = {}
    for auto in autokLista:
        if auto['szin'] not in autok.keys():
            autok[auto['szin']] = 1
        else:
            autok[auto['szin']] += 1
    maximumSzin = ''
    maximumSzam = 0
    for key, value in autok.items():
        if value > maximumSzam:
            maximumSzam = value
            maximumSzin = key
    return maximumSzin

def negyedikFeladat(autokLista):
    vanKat = 0
    nincsKat = 0
    for auto in autokLista:
        if auto['katalizator'] == '1':
            vanKat += 1
        else:
            nincsKat += 1
    return nincsKat

def otodikFeladat(autokLista:list):
    autokLista.sort(key=lambda x: int(x["cim"].split(' ')[0]))
    return autokLista



autok = fajlOlvas()
if elsoFeladat(autok):
    print("1. Feladat: Van ilyen tulajdonos")
else:
    print('1. Feladat: Nincs ilyen tulajdonos')

legoregebb = masodikFeladat(autok)
print(f"2. Feladat: Legöregebb autó:\n\tRendszáma: {legoregebb['rendszam']}\n\tTulajdonosa: {legoregebb['tulajdonos']}")

legtobbSzin = harmadikFeladat(autok)
print(f"3. Feladat: Leggyakoribb szin: {legtobbSzin}")

nincsKat = negyedikFeladat(autok)
print(f"4. Feladat: {nincsKat} db autónak nincs katalizátora")

rendezettSor = otodikFeladat(autok)
print(f"5. Feladat: Autók rendezett sorban:")
for auto in rendezettSor:
    print(f"\tRendszám: {auto['rendszam']}, Cím: {auto['cim']}")
