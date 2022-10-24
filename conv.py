szam = - 1
while szam<0 or szam>255:
    szam = int(input('Kérem adjon meg egy számot (0-255)'))
    eredmeny = ''
    while szam >= 1:
        eredmeny += str(szam % 2)
        szam = szam // 2
    print(eredmeny[::-1])