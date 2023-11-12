# import math
# print(math.sin(2))
#
# from math import sin, cos, sqrt, tan
# print(sin(2))
# print(cos(5), sqrt(14), tan(8))
#
# from math import *
# print(sqrt(8))
#
# print(range(5))
# print(range(2,7))
# print(range(3, 20, 2))
import math
import random
from array import array


# zadatak 2
from math import sqrt, cos, sin

print((3+4)*5)
n = 5
print(n*(n-1)/2)
r = 3
r2 = r**2
print(4!=r2)
a = 15
print(sqrt(r*cos(a)**2+r*sin(a)**2))
y1 = 3
y2 = 2
x2 = 4
x1 = 12
print((y2-y1)/(x2-x1))


# zadatak 3

# [0-4]
print(list(range(5)))

# [3-9]
print(list(range(3, 10)))

# {4, 6, 8, 10, YES 12}
print(list(range(4, 13, 2)))

# {15, 13, 11, 9, 7, NOT 5}
print(list(range(15, 5, -2)))

# []
print(list(range(5, 3)))

# zadatak 4

for i in range(1, 11):
    print (i*i)
# 1, 4, 9, 16, 25, 36, 49, ..., 100

for i in [1,3,5,7,9]:   # i = 1, 3, 5, 7, 9
    print (i, ":", i**3)
    print (i)


x = 2
y = 10
for j in range(0, y, x):
    print (j)   # 0 2 4 6 8
    print (x + y) # 12
print ("done") # done


ans = 0
for i in range(1, 11):
    ans = ans + i*i
    print (i)   # 1 2 3 4...10
print (ans)

# zadatak 5
# Napiši program koji izračunava zapreminu i površinu sfere za dati poluprečnik.
# Zapremina sfere V = 4/3 PI r^3
# Povrsina sfere A = 4 PI r^2
from math import pi
poluprecnik = eval(input("Unesite poluprecnik sfere: "))
zapremina_sfere = (4/3)*pi*poluprecnik**3
povrsina_sfere = 4*pi*poluprecnik**2

print(zapremina_sfere, povrsina_sfere)

#zadatak 6
#Napiši program koji izračunava cenu pice po kvadratnom centimetru za
# dati poluprečnik i cenu cele pice.
# A = r^2 PI

poluprecnik_pice = eval(input("Unesi poluprecnik pice [cm]: "))
cena_pice = eval(input("Unesi cenu pice: "))
povrsina_pice = poluprecnik_pice**2*math.pi
cena_pice_po_centimetru_kvadratnom = cena_pice / povrsina_pice
print("Cena pice po cm^2 je: ", cena_pice_po_centimetru_kvadratnom)

# zadatak 7
# Napiši program koji izračunava molekularnu masu molekula ugljovodonika zavisno od broja
# atoma ugljenika i vodonika koji ga čine. Mase atoma su sledeće:
# atom - masa
# H - 1.0079
# C - 12.011

broj_ugljenika = eval(input("Unesi broj ugljenika u ugljovodoniku: "))
broj_vodonika = eval(input("Unesi broj vodonika u ugljovodoniku: "))
masa_ugljenika = 12.011
masa_vodonika = 1.0079
masa_molekula = broj_vodonika*masa_vodonika+broj_ugljenika*masa_ugljenika

print("Masa celog molekula je: ", masa_molekula)

# zadatak 8
# Napiši program koji određuje udaljenost posmatrača od munje na bazi vremenske
# razlike trenutka pojavljivanja munje i trenutka kada zvuk stigne do posmatrača.
# Brzina zvuka iznosi 340 m/s.

#u sekundama su
trenutak_pojavljivanja_munje = 0    #[s]
trenutak_pristizanja_zvuka_do_posmatraca = 12 #[s]
brzina_rasprostiranja_zvuka = 340   #[m/s]

predjen_put = trenutak_pristizanja_zvuka_do_posmatraca-trenutak_pojavljivanja_munje
udaljenost_posmataca = predjen_put*brzina_rasprostiranja_zvuka

print("Udaljenost posmatraca", udaljenost_posmataca)

# zadatak 9
# Prodavnica kafe prodaje kafu za 105 dinara za kilogram. Za kućnu dostavu naplaćuje se
# 18 dinara po kilogramu i 15 dinara fiksnih troškova. Napiši program koji izraćunava ukupnu cenu kućne
# porudžbine.

kolicina_kafe = eval(input("Unesite koliko kilograma kafe zelite da narucite: "))

cena_kafe_po_kilogramu = 105
cena_dostave_po_kilogramu = 18
fiksni_troskovi = 15

cena_porudzbine = (kolicina_kafe * cena_kafe_po_kilogramu +
                   kolicina_kafe * cena_dostave_po_kilogramu) + fiksni_troskovi

print("Cena porudzbine je: ", cena_porudzbine)

# zadatak 10
# Dve tačke u ravni date su koordinatama x1 ; y1 i x2 ; y2 . Napiši program koji izračunava
# nagib prave koja prolazi kroz date tačke. m [y2 - y1 / x2 - x1]

x1, y1 = eval(input("Unesi koordinate prve tacke, odvojene zarezom: "))
x2, y2 = eval(input("Unesi koordinate druge tacke, odvojene zarezom: "))

nagib = (y2-y1) / (x2-x1)
print("Nagib prave je ", nagib)

# zadatak 11
# Za dve tačke u ravni (vidi prethodni zadatak) izračunati rastojanje između njih.
# d = sqrt((x2-x1)**2 + (y2-y1)**2)

x1, y1 = eval(input("Unesi koordinate prve tacke, odvojene zarezom: "))
x2, y2 = eval(input("Unesi koordinate druge tacke, odvojene zarezom: "))

rastojanje_izmedju_tacaka = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Rastojanje izmedju datih tacaka je ", rastojanje_izmedju_tacaka)

# zadatak 12
# Epakt predstavlja starost meseca u danima na dan 1. januara. Koristi se za izračunavanje
# termina Uskrsa. Gregorijanski epakt se izračunava po sledećim formulama (int aritmetika):
# C = year/100
# epakt = (8 + C/4 - C + ((8C + 13)/25) + 11 (year%19))%30
# Napiši program koji od korisnika traži godinu kao 4-cifreni broj i izračunava epakt po gregorijanskom
# kalendaru.

godina = eval(input("Unesi neku cetvorocifrenu godinu: "))
c = godina/100
epakt = (8+c/4-c+((8*c+13)/25)+11*(godina%19))%30
print("Epakt za datu godinu je: ", epakt)

# zadatak 13 Napiši program koji izračunava površinu trougla za date dužine stranica a, b i c.
# s = a+b+c / 2
# A = sqrt( s(s - a)(s - b)(s - c) )
#
# stranica_a, stranica_b, stranica_c = eval(input("Unesi stranice trougla, odvojene zarezom: "))
# s = (stranica_a+stranica_b+stranica_c) / 2
# povrsina_trougla = math.sqrt(s*(s-stranica_a)*(s-stranica_b)*(s-stranica_c))
#
# print("Povrsina trougla je: ", povrsina_trougla)

# zadatak 14 Napiši program koji izračunava dužinu merdevina za datu visinu koju treba dostići i ugao
# kojim se meri nagib merdevina. d = visina/sin(ugla)

visina = eval(input("Unesite visinu na koju se treba popeti: "))
ugao_nagiba = eval(input("Unesite nagib merdevina: "))
duzina_merdevina = visina / math.sin(ugao_nagiba)

print("Potrebna duzina merdevina je: ", duzina_merdevina)

# Zadatak 15. Napiši program koji izračunava zbir prvih n prirodnih brojeva, gde se n unosi sa tastature.
n = math.floor(eval(input("Koliko prirodnih brojeva zelis da sumiramo: ")))
zbir = n*(n+1)/2
print(f"Suma prvih {n} prirodnih brojeva je {zbir}")

#zadatak 16. Napiši program koji izračunava zbir kvadrata prvih n prirodnih brojeva, gde se n unosi sa
#tastature.
n = math.floor(eval(input("Za koliko prirodnih brojeva zelis da sumiramo njihove kvadrate: ")))
zbir = n*(n+1)*(2*n+1)/6
print(f"Suma kvadrata prvih {n} prirodnih brojeva je {zbir}")

# zadataak 17. Napiši program koji izračunava zbir brojeva koje unosi korisnik. Prvo je potrebno uneti
# broj brojeva koje treba sabrati. Potom treba uneti sve brojeve i na kraju ispisati vrednost zbira.

brojevi = list()
broj_unosa = eval(input("Koliko brojeva zelis da uneses: "))
for i in range(broj_unosa):
    brojevi.append(eval(input(f"Unesi cifru {i}: ")))

suma = sum(brojevi)
print(f"Zbir unesenih vrednosti je: {suma}")

# zadatak 18 Napiši program koji izračunava prosek brojeva koje unosi korisnik (slično prethodnom
# zadatku). Prosek bi trebalo da bude float.

brojevi = list()
broj_unosa = eval(input("Koliko brojeva zelis da uneses: "))
for i in range(broj_unosa):
    brojevi.append(eval(input(f"Unesi cifru {i}: ")))

prosek = sum(brojevi)/brojevi.__len__()
print(f"Prosek za unesene vrednosti je: {prosek}")

# zadatak 19 Napiši program koji izračunava aproksimaciju broja PI kao delimičnu sumu ovog reda:
# 4/1 - 4/3 + 4/5 - 4/7 + 4/9  - 4/11 + : : : Program treba da zatraži broj članova ovog niza koje treba
# sabrati.

broj_unosa = eval(input("Koliko clanova niza uzimas u obzir pri aproksimaciji vrednosti broja PI: "))
pi = 0
znak = 1
for i in range(broj_unosa):
    pi += znak * 4/(2*i+1)
    znak *= -1
print(f"izracunata vrednost pi je {pi}")

# Zadatak 20 Fibonačijev niz brojeva je niz kod koga svaki broj predstavlja zbir prethodna dva. Ovaj
# niz počinje sa 1, 1, 2, 3, 5, 8, 13, ... Napiši program koji izračunava n-ti Fibonačijev broj gde n unosi
# korisnik. Fibonačijevi brojevi rastu vrlo brzo, program mora da rukuje vrlo velikim brojevima.

n = eval(input("Koliko Fibonacijevih brojeva zelis da ispises: "))

def get_fibbonaci_sequence(n):
    trazeni = 0
    tekuci = 1
    for i in range(n):
        prethodni = tekuci
        tekuci = trazeni + tekuci
        trazeni = prethodni
    return  trazeni

print(f"Fibbonaci sequence returned: {get_fibbonaci_sequence(n)}")

# zadatak 21 Paket math sadrži funkciju za izračunavanje kvadratnog korena. Potrebno je napisati
# sopstvenu funkciju za izračunavanje kvadratnog korena pomoću PiP („probaj-i-ponovo“) pristupa. Prvo
# pokušamo da pogodimo vrednost korena i uporedimo je sa pravom vrednošću (koju vraća sqrt). Onda
# napravimo sledeći pokušaj i približimo se rešenju. Postupak ponavljamo dok ne naiđemo na pravu
# vrednost korena ili njenu dovoljno dobru aproksimaciju. Za ovaj posao možemo koristiti Njutnov metod.
# Neka je x broj čiji koren tražimo, i guess broj kojim pokušavamo da pogodimo koren. Pokušaj se
# može popraviti korišćenjem vrednosti guess+2x=guess u sledećem krugu. Napiši program koji implementira
# Njutnov metod. Program od korisnika traži broj čiji koren tražimo (x) i broj pokušaja. Početna vrednost
# za pokušaj je x= . Na kraju rada ispisati dobijenu vrednost Njutnovom metodom i vrednost koju vraća
# sqrt.

def calculate_sqrt(num, attempts):
    if(num<0):
        print("Number must be positive")
        return -1

    offset = 0.5
    guess = random.randint(1, math.floor(num/2))
    actual_sqrt = math.sqrt(num)
    while guess != actual_sqrt and attempts != 0:
        guess = (guess+num/guess)/2
        attempts-=1
        print(guess)

    return guess

num, attempts = eval(input("Enter value to check sqrt of, and number of attempts: "))
my_sqrt = calculate_sqrt(num, attempts)
print(my_sqrt)