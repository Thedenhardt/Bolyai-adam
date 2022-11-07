oktettek = input("Írja be az ipv4-es címet: ").strip().split(".")
ipcim = '.'.join(oktettek)
binarisOktettek = []
for oktett in oktettek:
    oktett = int(oktett)
    eredmeny = ""
    while oktett >= 1:
        eredmeny += str(oktett % 2)
        oktett = oktett // 2
    binarisOktettek.append(eredmeny[::-1].zfill(8))

print(f"A {ipcim} ipv4 cím kettes számrendszerben kifejezve = {'.'.join(binarisOktettek)}")