kolicina_vode_u_buretu = 121 # u litrima
zapremina_kante = 5

broj_kanti  = 0

while kolicina_vode_u_buretu > 0:
    kolicina_vode_u_buretu -= zapremina_kante
    broj_kanti += 1

print(f"Za praznjenje celog bureta, potrebno je {broj_kanti} kanti")