print("Ovaj program ilustruje haoticno ponasanje")
x = eval(input("Unesite broj izmedju 0 i 1: "))
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)

# 3 User-friendly program bi trebalo da ispiše uvodni tekst koji korisniku objašnjava šta program
# radi. Izmeni program convert.py tako da ispiše uvodnu poruku.
# convert.py
# Konverzija temperature iz Celzijusa u Farenhajte

print("Ovaj program prima temperaturu u celzijusima i konvertuje je i ispisuje, kao temperaturu u farenhajtima ")
celsius = eval(input("Unesite temperaturu u C >> "))
fahrenheit = 9/5 * celsius + 32
print("Temperatura je", fahrenheit, "stepeni Farenhajta.")

# 4 Izmeni program avg2.py tako da izračunava prosek tri ocene.
# avg2.py
# Izracunava prosek dve ocene
# Ilustruje unos vise podataka odjednom

print("Izracunava prosek dve ocene.")

score1, score2, score3 = eval(input("Unesite tri ocene razdvojene zarezom: "))
average = (score1 + score2 + score3) / 3

print("Prosecna ocena je:", average)

# 5. Izmeni program futval.py tako da broj godina bude unet sa tastature. Ispis rezultata
# takođe treba da obuhvati korektan broj godina.
# futval.py
# Izracunava buduce stanje orocenog novca
# za rok od 10 godina

print("Ovaj program izracunava stanje stednog racuna")
broj_godina = eval(input("Unesite broj godina: "))
print("nakon isteka roka od " + str(broj_godina) + " godine/a.")

principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))

for i in range(broj_godina):
    principal = principal * (1 + apr)

print("Stanje nakon 10 godina:", principal)

# 6 izmeni program convert.py tako da izračunava i ispisuje tabelu stepeni Celzijusa i Faren-
# hajta za svakih 10 stepeni od 0o C do 100o C.

celsius = [1, 10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
fahrenheit = []
for i in celsius:
    fahrenheit.append(9/5 * i + 32)
print("celsius | fahrenhait")
for i in range(len(celsius)):
    print(celsius[i].__str__() + " | " + fahrenheit[i].__str__())

# 7 Napiši program za konverziju iz Farenhajta u Celzijuse.

fahrenheit = eval(input("Unesi farenhajte: "))
celsius = (fahrenheit - 32) * 5/9
print("Zadata temperatura u celzijusima iznosi: " + celsius.__str__())


# 8. Izmeni program futval.py tako da izračunava realnu dobit, uzimajući u obzir i inflaciju.
# Godišnji stepen inflacije se takođe unosi sa tastature. Formula koja uključuje uticaj inflacije je sledeća:
# principal = principal/(1 + inflation)

print("Ovaj program izracunava stanje stednog racuna")

broj_godina = eval(input("Unesite broj godina: "))
principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))
inflation = eval(input("Unesite godisnju inflaciju: "))

for i in range(broj_godina):
    principal = principal * (1 + apr)
    principal = principal/(1+inflation)

print("Stanje nakon ",broj_godina," godina:", principal)