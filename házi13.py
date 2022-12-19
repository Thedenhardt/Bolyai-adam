operations = ['+', '-', '*', '/']


def calculate(input_string):
    resz = input_string.split(' ')
    if resz[1] in operations:
        szam1 = float(resz[0])
        szam2 = float(resz[2])

        if resz[1] == '+':
            return szam1 + szam2
        elif resz[1] == '-':
            return szam1 - szam2
        elif resz[1] == '*':
            return szam1 * szam2
        elif resz[1] == '/':
            if szam2 == 0:
                return "Nullával nem lehet osztani"
            else:
                return szam1 / szam2
    else:
        return "Helytelen művelet"


input_string = input("adj meg egy számolást: ")
result = calculate(input_string)
print(result)