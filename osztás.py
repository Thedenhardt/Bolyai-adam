szam = int(input('Kérem adjon meg egy egész számot: '))
szamlalo = 1

while szam > 1:
    if szam % 2 == 0:
        szam /= 2
    else:
        szam += 1
    print('A', szamlalo, 'elem:', int(szam))
    szamlalo += 1