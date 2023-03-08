countries=[]
def founder(_founders):
    return _founders['Accesion']

with open("eu.csv",'r',encoding="utf-8") as forras:

    for line in forras:
        country_list=line.strip().split(',')
        country={"country":country_list[0],'capital':country_list[1],'Accesion':country_list[2]}
        countries.append(country)

countries.sort(key=founder)
