def ucitaj_datoteku(ime_datoteke: str) -> list:
    with open(ime_datoteke, "r") as datoteka:
        podaci = datoteka.read().splitlines()
    return podaci

def obradi_u_brojeve(podaci: list) -> list:
    podaci_kao_brojevi = list()
    for podatak in podaci:
        lijevi, drugi = podatak.split(",")
        podaci_kao_brojevi.append((int(lijevi), int(drugi)))
    return podaci_kao_brojevi

def djeljiv(broj, djelitelj) -> bool:
    return broj % djelitelj == 0

def izbroji_koliko_zadovoljava_uvjet(podaci, uvjet) -> int:
    zadovoljavaju = 0
    for (prvi, drugi) in podaci:
        if uvjet(prvi, drugi):
            zadovoljavaju += 1
    return zadovoljavaju


podaci = obradi_u_brojeve(ucitaj_datoteku("podaci.txt"))

broj_djeljivih = izbroji_koliko_zadovoljava_uvjet(podaci, djeljiv)

print(f"Od {len(podaci)} parova (a,b), postoji samo {broj_djeljivih} parova gdje je a djeljiv sa b.")
