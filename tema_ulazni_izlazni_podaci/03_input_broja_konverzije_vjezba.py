# ucitajmo broj s ekrana, pomnozimo ga s 2 i ispisemo rezultat

# ucitavanje u varijablu broj
broj = input("Unesite broj: ")

# racunanje rezultata

rezultat = 2 * broj

# isprintajmo rezultat koristeci formatirani string sa ubacivanjem varijabli, npr:
print(f"rezultat operacije 2 x {broj} je {rezultat}")
print(f"2 x {broj} = {rezultat}")

# rezultat radi sa stringovima!

pravi_broj = int(broj)
rezultat = 2 * pravi_broj

print(f"2 x {pravi_broj} = {rezultat}")

