def calculate_life_digit(bday: str) -> int:
    szam = [int(d) for d in bday if d.isdigit()]
    while len(szam) > 1:
        szam = [int(d) for d in str(sum(szam))]
    return szam[0]

bday = input("írd be a születési éved YYYY.MM.DD: ")
life_digit = calculate_life_digit(bday)
print("a számod:", life_digit)