def osszeadas(a, b):
    return a + b


def kivonas(a, b):
    return a - b


def szorzas(a, b):
    return a * b


def osztas(a, b):
    return a / b


def hatvany(a, b):
    return a ** b


def faktorialis(a):
    szum = 1
    for i in range(1, a + 1):
        szum *= i
    return szum


def main():
    sor = input("Számolás: ")
    muvelet = ''
    muveletek = ['+', '-', '*', '/', '^', '!']
    for i in sor:
        if i in muveletek:
            muvelet = i
    if '!' != muvelet:
        a, b = list(map(int, sor.strip().split(muvelet)))
        eredmeny = 0
        if muvelet == '+':
            eredmeny = osszeadas(a, b)
        elif muvelet == '-':
            eredmeny = kivonas(a, b)
        elif muvelet == '*':
            eredmeny = szorzas(a, b)
        elif muvelet == '/':
            eredmeny = osztas(a, b)
        elif muvelet == '^':
            eredmeny = hatvany(a, b)
    else:
        a = int(sor.strip().split(muvelet)[0])
        eredmeny = faktorialis(a)
    print(f"Eredmény: {eredmeny}")


main()