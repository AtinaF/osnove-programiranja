print("Numerički kod za karakter a je",ord("a"))
print("Numerički kod za karakter A je",ord("A"))

print("Karakter za kod 35 je", chr(35))
print("Karakter za kod 80 je", chr(80))

# Numerički kod za karakter a je 97
# Numerički kod za karakter A je 65
# Karakter za kod 35 je #
# Karakter za kod 80 je P


#-*- coding: utf-8 -*-
print ("Ћирилична порука")
#Latinični komentar

# print(string_format % vrednosti)
print("My name is %s. I am %d years old." % ("John", 11))

# Greška u redosledu navođenja. Prvi karakter za zamenu je uspešno zamenjen brojem 11 (konverzija je uspela).
# Drugi karakter nije zamenjen jer se string ne može implicitno konvertovati u broj.
# print("My name is %s. I am %d years old." % (11, "John"))
# % znak_za_poravnanje broj_karaktera_za_poravnanje . broj_karaktera_za_odsecanje karakter_za_konverziju
# znak_za_poravnanje i broj_karaktera_za_poravnanje: Ukoliko želimo da tekst poravnamo ulevo
# za broj_karaktera_za_poravnanje, navodimo znak -. Za poravnanje udesno nije potrebno navesti znak.

# Bez navođenja poravnanja
print("Moje ime je: %s" % "Milica")
# Desno poravnanje
print("Moje ime je: %10s" % "Milica")
# Levo poravnanje
print("Moje ime je: %-10s i rođena sam %d. godine." % ("Milica", 1999))
# Zanemarivanje poravnanja
print("Moje ime je: %3s i rođena sam %d. godine." % ("Milica", 1999))

# Moje ime je: Milica
# Moje ime je:     Milica
# Moje ime je: Milica     i rođena sam 1999. godine.
# Moje ime je: Milica i rođena sam 1999. godine.

# broj_karaktera_za_odsecanje

# Primer formatiranja i zaokruživanja
print("Cena artikla je: %10.4f" % 33.19596)
# Primer brojeva sa manjim brojem decimala
print("Cena artikla je: %10.4f" % 33.19)
# Zaokruživanje bez navođenja paramtara za poravnanje
print("Cena artikla je: %.4f" % 33.19)

# Primer za stringove
print("Ispis: %.3s" % "Neki duži tekst")

# Cena artikla je:    33.1960
# Cena artikla je:    33.1900
# Cena artikla je: 33.1900
# Ispis: Nek

print("My name is {} {}.".format("John", "Smith"))
print("My name is {}.".format(1224))

# My name is John Smith.
# My name is 1224.

print("My name is {0} {1}.".format("John", "Smith"))
print("My name is {1}, {0} {1}.".format("John", "Smith"))

# My name is John Smith.
# My name is Smith, John Smith.

# Obe vrednosti poravnavamo ulevo
print("My name is {0:10} {1:10}.".format("John", "Smith"))
# Obe vrednosti poravnavamo udesno
print("My name is {0:>10} {1:>10}.".format("John", "Smith"))
# Nije neophodno navesti redni broj parametra.
print("My name is {:>10} {:>10}.".format("John", "Smith"))
# Eksplicitno poravnanje ulevo
print("My name is {0:<10} {1:<10}.".format("John", "Smith"))

# My name is John       Smith     .
# My name is       John      Smith.
# My name is       John      Smith.
# My name is John       Smith     .

# Prvu vrednost poravnavamo ulevo sa eksplicitnim navođenjem znaka < i na prazna mesta ubacujemo _
# Drugu vrednost poravnavamo udesno sa eksplicitnim navođenjem znaka > i na prazna mesta ubacujemo *
print("My name is {0:_<10} {1:*>10}.".format("John", "Smith"))

# My name is John______ *****Smith.
#
# Vrednost se može centrirati upotrebom karaktera ^.

print("My name is {0:^10} {1:^10}.".format("John", "Smith"))

# My name is    John      Smith   .


# print("nesto {} nesto drugo {}".format("abs", 223))
# Obe vrednosti poravnavamo ulevo - ispisi argument iz formata sa 0-tog indeksa, u 10 mesta, isto za drugi argument
# kazem koliko mesta zauzimam (10), i onda na koju stranu stavljam tekst u tih 10 mesta (levo, desno,..)
print("My name is {0:10} {1:10}.".format("John", "Smith"))
# Obe vrednosti poravnavamo udesno
print("My name is {0:>10} {1:>10}.".format("John", "Smith"))
# Nije neophodno navesti redni broj parametra.
print("My name is {:>10} {:>10}.".format("John", "Smith"))
# Eksplicitno poravnanje ulevo
print("My name is {0:<10} {1:<10}.".format("John", "Smith"))

# My name is John       Smith     .
# My name is       John      Smith.
# My name is       John      Smith.
# My name is John       Smith     .
print("a"*4)

print("neki lepi string.34 pesma o pesmi".split())
tekst = "ala je lep ovaj svet, onde potok, ovde cvet"
for char in tekst:
    print("{} ".format(char*2))


#
# Join
#
# Funkcija join konkatenira stringove iz zadate liste koristeći string nad kojim se poziva kao separator.

lista = ["Jan", "Feb", "Mar"]
s = ", "
print(s.join(lista))

# Jan, Feb, Mar

# Lower i upper
#
# Funkcija lower konvertuje sva slova stringa u mala. Karaktere koji nisu slova ne menja. Funkcija upper konvertuje sva slova stringa u velika. Karaktere koji nisu slova ne menja.

s = "Hello world!"
string_malim_slovima = s.lower()
string_velikim_slovima = s.upper()
print("String \'%s\' zapisan malim slovima je \'%s\'." % (s, string_malim_slovima))
print("String \'%s\' zapisan velikim slovima je \'%s\'." % (s, string_velikim_slovima))

# String 'Hello world!' malim slovima je 'hello world!'.
# String 'Hello world!' velikim slovima je 'HELLO WORLD!'.
#
# Strip
# Funkcija strip uklanja razmake (whitespace) sa početka (lstrip) odnosno kraja stringa (rstrip). Često se koristi kod obrade korisničkog unosa.

s = "    Hello  world!     "
s_bez_razmaka_levo = s.lstrip()
s_bez_razmaka_desno = s.rstrip()
print(s_bez_razmaka_levo)
print(s_bez_razmaka_desno)

# Hello  world!
#     Hello  world!

# Replace

# Funkcija za zamenu jednog podstringa drugim. Podstringovi mogu da imaju proizvoljno mnogo karaktera. Pomoću funkcije replace možemo dobiti efekat brisanja dela stringa.

s = "Hello world!"
novi_string = s.replace("lo", "WWW")
novi_string_sa_izbrisanim_l = s.replace("l", "")
print(novi_string)
print(novi_string_sa_izbrisanim_l)

# HelWWW world!
# Heo word!
#
