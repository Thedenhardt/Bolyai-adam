def ir(nyelvek, fajlnev, h1, h2):
    with open(f'{fajlnev}.txt', 'w', encoding='utf-8') as f:
        f.write(h1)
        f.write(h2)
        for nyelv in nyelvek:
            f.write(f"{nyelv['year']};{nyelv['lang']};{nyelv['fn']};{nyelv['ln']}\n")

def dupekeres(nyelvek):
    seen = []
    dupeok = []
    for nyelv in nyelvek:
        if nyelv["lang"] not in seen:
            seen.append(nyelv["lang"])
        elif nyelv not in dupeok:
            dupeok.append(nyelv)
    return dupeok

def main():
    nyelvek = []
    with open('programnyelv_1feladat.txt', 'r', encoding='utf-8') as f:
        h1 = f.readline()
        h2 = f.readline()
        for line in f:
            sor = line.strip().split(';')
            nyelvek.append({"year": int(sor[0]), "lang": sor[1], "fn": sor[2], "ln": sor[3]})
    nyelvek.sort(key=lambda x: x["year"])
    ir(nyelvek, "evszamok", h1, h2)
    nyelvek.sort(key=lambda x: x["ln"].strip())
    ir(nyelvek, "programozo", h1, h2)
    ir(dupekeres(nyelvek), "ismetles", h1, h2)
    
main()
    


