év = int(input("irja be az évet:"))
kezd=1983-4*60
év=(év-kezd)%60
print(év)


if  1984 <=év<= 2043:
    év = év%10
    print(év)
    print("zöld év")
elif év == 3 or 4:
    print("piros év")
elif év == 5 or 6:
    print("sárga év")
elif év == 7 or 8:
    print("fehér év")
elif év == 9 or 0:
    print("fekete év")
else: print("nem a ciklus része")