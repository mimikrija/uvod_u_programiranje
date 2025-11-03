# ucitajmo podatke iz datoteke imena.txt u listu
# r (read) citaj iz datoteke

with open("imena.txt", "r") as datoteka:
    podaci = datoteka.read().split("\n")

# isprintajmo podatke
print(podaci)

# isprintajmo jedan po jedan podatak (for petlja kroz listu)
for podatak in podaci:
    print(podatak)


# ucitajmo podatke iz dadoteke brojevi.txt
# oprez, brojevi su odvojeni zarezom!

with open("brojevi.txt", "r") as datoteka:
    brojevi = datoteka.read().split(",")

print(brojevi) # navodnici upucuju na to da su brojevi stringovi

# pretvorimo listu "brojeva" u integere

pravi_brojevi = list()

for broj in brojevi:
    pravi_broj = int(broj)
    pravi_brojevi.append(pravi_broj)

# izracunajmo sumu i prosjek svih pravih brojeva

suma_svih_brojeva = sum(pravi_brojevi)
kolicina_svih_brojeva = len(pravi_brojevi) # duljina liste


prosjek_svih_brojeva = suma_svih_brojeva / kolicina_svih_brojeva

print(f"suma svih brojeva u listi je {suma_svih_brojeva}!")
print(f"prosjek brojeva u listi je {prosjek_svih_brojeva}!")


