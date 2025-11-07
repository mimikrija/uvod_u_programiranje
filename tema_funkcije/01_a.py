with open("podaci.txt", "r") as datoteka:
    podaci = datoteka.read().splitlines()

pravi_podaci = list()

for p in podaci:
    a, b = p.split(",")
    pravi_podaci.append((int(a), int(b)))

rezultat = 0

for (a, b) in pravi_podaci:
    if a % b == 0:
        rezultat += 1

print(f"Od {len(podaci)} parova (a,b), postoji samo {rezultat} parova gdje je a djeljiv sa b.")