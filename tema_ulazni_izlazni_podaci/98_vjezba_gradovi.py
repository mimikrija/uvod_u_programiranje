# ucitati gradove iz datoteke omiljeni_gradovi.txt u listu gradovi
# hint: prije pisanja koda za ucitavanje provjerite kako su gradovi u datoteci odvojeni
# (novi red, zarez, dvotocka..?)

with open("98_opcine_i_gradovi.txt", "r") as datoteka:
    podaci = datoteka.read().split("\n")

# napraviti novu listu koja sadrzi samo gradove koji nemaju u imenu slovo m (oprez, sto ako je slovo M?)

podaci = [grad for grad in podaci if "m" not in grad and "M" not in grad]



# zapisati gradove u datoteku 98_rezultat.txt, odvojene zarezom i razmakom
# otvorite datoteku, i potrazite sadrzi li slovo m ili M?


with open("98_rezultat.txt", "x") as datoteka:
    for grad in podaci:
        datoteka.write(grad + ", ")