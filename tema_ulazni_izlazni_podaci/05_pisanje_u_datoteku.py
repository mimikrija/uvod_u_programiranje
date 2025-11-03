# pisanje podataka u datoteku


# 'w' (overwrite) - pisanje u postojecu datoteku (prebrisat ce sadrzaj pri svakom novom pisanju)
# 'x' - stvaranje nove datoteke i pisanje u nju - ne radi ako datoteka vec postoji!
# 'a' (append) - dodavanje u postojecu datoteku


# napravimo praznu datoteku 05_rezultat.txt u istom direktoriju kao ovaj python kod

# upisimo svoje ime u datoteku 05_rezultat.txt
# oprez, ako ista postoji u ovoj datoteci, bit ce prebrisana!

with open("05_rezultat.txt", 'w') as izlazna_datoteka:
    izlazna_datoteka.write("Maja")


omiljeni_gradovi = [
    "Barcelona",
    "Gouda",
    "Antwerpen",
    "Zabok"
]


# dodajmo listu omiljenih gradova na kraj iste datoteke
with open("05_rezultat.txt", 'a') as izlazna_datoteka:
    for grad in omiljeni_gradovi:
        izlazna_datoteka.write(grad)


# hrvaski dijakritici i posebni znakovi
# encoding="utf-8"


# with open("05_rezultat.txt", 'w') as izlazna_datoteka:
#     izlazna_datoteka.write(f"maja gaćeša")