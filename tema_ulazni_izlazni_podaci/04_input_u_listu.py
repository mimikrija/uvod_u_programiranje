# pomocu petlje upitati korisnika da unese 10 imena i sremiti ih u listu
# sortirati listu
# isprintati jedno po jedno sortirano ime

popis_imena = list() # kreiramo praznu listu


for n in range(1, 11):
    ime = input(f"Molim upisite {n}. ime: ")
    popis_imena.append(ime)


# sortirati imena
popis_imena.sort()

# razne for petlje na listi imena
for ime in popis_imena:
    print(ime)

