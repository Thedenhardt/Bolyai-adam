# Open the file in read mode
with open("vers.txt", "r") as file:
    vers = file.read()

betuk = len(vers)
mh = 0
for betu in vers:
    if betu.lower() in "aeiou":
        mh += 1
szavak = len(vers.split())

print("betűk:", betuk)
print("magánhangzók:", mh)
print("szavak:", szavak)
