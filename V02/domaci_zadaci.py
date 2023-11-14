import math
import random

# # 1 Napišite Python program koji će korisnika pitati za vreme (u sekundama) i
# # ubrzanje (u metrima po sekundi kvadratnom) i
# # zatim izračunati i ispisati krajnju brzinu objekta.
#
# vreme = eval(input("Unesite vreme u [s]]: "))
# ubrzanje = eval(input("Unesite ubrzanje u [m/s^2]: "))
# pocetna_brzina = 0
#
#
# brzina_objekta = pocetna_brzina + ubrzanje*vreme
# print("Krajnj brzina objekta je: ", brzina_objekta)
#
# # 2. Napišite Python program koji će korisnika pitati za visinu sa koje objekat pada (u metrima) i
# # zatim izračunati i ispisati brzinu objekta kada dotakne tlo.
# # Uputstvo:
# # Koristite zakon očuvanja energije da biste izračunali brzinu objekta na tlu. Zakon očuvanja energije
# # kaže da je početna potencijalna energija jednak krajnjoj kinetičkoj energiji:
# # PE=KE
# # gde je:
# # PE potencijalna energija na početku (masa * gravitaciono ubrzanje * visina),
# # KE kinetička energija na kraju (0.5 * masa * brzina^2).
#
# visina = eval(input("Unesite visinu sa koje objekat pada: "))
# masa = 15.2
# gravitaciono_ubrzanje = 9.81
#
# potencijalna_energija = masa * gravitaciono_ubrzanje * visina   # veca na vecoj visini
# kineticka_energija = potencijalna_energija # u trenutku dodira tla
#
# brzina_pri_kontaktu_sa_tlom = math.sqrt(kineticka_energija/(0.5*masa))
# print("Brzina objekta kada dotakne tlo, je: ", brzina_pri_kontaktu_sa_tlom)

# # 3 Program generiše nasumičan broj između 1 i 9, a zatim traži od korisnika da pogodi. Program
# # treba da obavesti da li je korisnički pogodak bio veći, manji ili jednak generisanom (odnosno
# # tačan). Potrebno je obavestiti korisnika u slučaju da je njegov predlog izašao iz mogućeg
# # opsega.
# # Proširenje 1: Korisnik na početku zadaje opseg brojeva za pogađanje, donju i gornju granicu.
# # Proširenje 2: Dozvoliti korisniku da zada maksimalni broj pokušaja. Pogađanje se prekida ili kad
# # korisnik potroši sve pokušaje ili kad pogodi tačan broj.
# # Proširenje 3: Kada se izvršavanje programa prekine, korisniku se ispisuje informacija o broju
# # iskorišćenih pokušaja pogađanja.
#
# donja_granica_opsega = eval(input("Unesite donju granicu opsega: "))
# gornja_granica_opsega = eval(input("Unesite gornju granicu opsega: "))
# broj_pokusaja = eval(input("Unesite broj pokusaja: "))
# broj = random.randint(donja_granica_opsega,gornja_granica_opsega)
# pogodjen = False
# utrosen_broj_pokusaja = 0
#
# while(not pogodjen and broj_pokusaja != 0):
#     pogodak = eval(input("Pogodite koji broj je generisao racunar "))
#     utrosen_broj_pokusaja += 1
#     if pogodak < donja_granica_opsega or pogodak > gornja_granica_opsega:
#         print("Izasli ste van granica opsega.")
#     elif pogodak == broj:
#         print("Pogodili ste.")
#         pogodjen = True
#     elif pogodak > broj:
#         print("Premasili ste pravu vrednost.")
#     else:
#         print("Vas pogodak je maji od generisanog broja.")
#
#     broj_pokusaja -= 1
#
# print("Iskoristili ste " + utrosen_broj_pokusaja.__str__() + " pokusaja.")

# 4 Korisnik zadaje proizvoljne granice, a zatim zamišlja broj u tom opsegu. Proverava se da li su
# zadate granice korektne, odnosno da li je donja manja od gornje. Računar pogađa broj na sličan
# način kao u prethodnom zadatku.
# Proširenje 1: Pokušajte da osmislite optimalan postupak dolaska do rešenja.

donja_granica = eval(input("Unesite donju granicu: "))
gornja_granica = eval(input("Unesite gornju granicu: "))
broj = eval(input("Unesite broj u zadatom intervalu: "))

pogodjen = False
broj_pokusaja = 0
brojevi_koji_ne_ulaze_u_dalja_pogadjanja = set([int])

def get_next_guess(donja, gornja, dosadasnji_pogodci):
    if dosadasnji_pogodci.__len__() == 0:
        naredni_pogodak =  random.randint(donja, gornja)
        print("bhjjkjhhkjhjk")
    else:
        naredni_pogodak = random.choice(list(set(range(donja, gornja)).difference(dosadasnji_pogodci)))

    return naredni_pogodak


while not pogodjen:
    pogodak = get_next_guess(donja_granica, gornja_granica, brojevi_koji_ne_ulaze_u_dalja_pogadjanja)
    brojevi_koji_ne_ulaze_u_dalja_pogadjanja.add(pogodak)
    broj_pokusaja += 1
    if pogodak == broj:
        print("Pogodili ste.")
        pogodjen = True
    elif pogodak > broj:
        #TODO figure out how, if possible, to do this in 1 line of code :) for fun
        #brojevi_koji_ne_ulaze_u_dalja_pogadjanja.add([num for num in tuple(range(pogodak, gornja_granica)) if pogodak != gornja_granica])
        for i in range(pogodak, gornja_granica):
            brojevi_koji_ne_ulaze_u_dalja_pogadjanja.add(i)
    else:
        for i in range(donja_granica, pogodak):
            brojevi_koji_ne_ulaze_u_dalja_pogadjanja.add(i)
print("Broj pokusaja: ", broj_pokusaja)
print(brojevi_koji_ne_ulaze_u_dalja_pogadjanja)

