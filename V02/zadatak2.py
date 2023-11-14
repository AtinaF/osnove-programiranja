#Napiši program koji ispisuje sve brojeve između 1200 i 2500 koji su deljivi
# sa 7 i 11.
# Proširenje 1: Koristiti naredbu continue.
# Proširenje 2: Ukoliko se naiđe na broj koji je deljiv sa 1111, prekinuti
# potragu. Koristiti break naredbu

found = 0
for i in range(1200,2500):
    if i % 1111 == 0:
        break
    elif i % 17 == 0:
        print(f"7: {i}")
        found += 1
        #continue
    elif i % 11 == 0:
        print(f"11: {i}")
        found += 1

print(found)