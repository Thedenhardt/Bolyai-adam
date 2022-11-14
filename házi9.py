t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június',  'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
t3 = []
for index, honap in enumerate(t2):
    t3.append(f"{honap}, {t1[index]}")
print(t3)
