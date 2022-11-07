oktettek = []

for i in range(1,5):
    while True:
        oktett = int(input(f"Kérem az {i}. oktettet: "))
        if oktett >= 0 and oktett < 256:
            oktettek.append(str(oktett))
            break
        else:
            print("Ez az oktett nem szabványos! Kérem, adja meg újra. ")
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