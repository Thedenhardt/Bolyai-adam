magasság =  float(input("Adja meg a magasságát m-ben:"))
testsuly = float(input("Adja meg a testtömegét kg-ban:"))
index = testsuly/(magasság**2)

min=(18.5)
max=(24.99)
kb = min*(magasság**2)
kb = round(kb,2)

kb1 = max*(magasság**2)
kb1 = round(kb1,2)
print("*"*30, "-"*5, "*"*30, sep="")
print("Az ön testtömegindexe:", round(index, 2), "%")
print("Az ön magasságához az ideális testtömeg:",kb,"kg","és",kb1,"kg között van")