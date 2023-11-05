print("Ovaj program ilustruje haoticno ponasanje")
x = eval(input("Unesite broj izmedju 0 i 1: "))
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)

#zadatak 7
#izmeni program chaos.py tako da koristi konstantu 2.0 umesto 3.9

y = eval(input("Unesi broj izmedju 0 i 1:"))
for i in range(10): #0,1,2...,9
    y = 2.0 * y * (1-y)
    print(y)

#zadatak 8
#izmeni program chaos.py tako da ispisuje 20 vrednosti umesto 10

y = 0.2
for i in range(20): #0,1,2...,9
    y = 2.0 * y * (1-y)
    print(y)

#zadatak 9
#izmeni program chaos.py tako da ucitava 2 podatka i ispisuje tabelu sa dve kolone
# (poravnavanje teksta u tabeli sada nije vazno).

print("Ovaj program ilustruje haoticno ponasanje")
p = eval(input("Unesite broj izmedju 0 i 1: "))
q = eval(input("Unesite broj izmedju 0 i 1: "))
for i in range(10):
    p = 3.9 * p * (1 - p)
    q = 3.9 * q * (1 - q)
    print(p.__str__() + "\t | \t" + q.__str__())

# bolji pristup:
print("Ovaj program ilustruje haoticno ponasanje")
p,q = eval(input("Unesite 2 broja izmedju 0 i 1, odvojena zarezom: ")) #odvojena zarezom
print(p,q)
for i in range(10):
    p = 3.9 * p * (1 - p)
    q = 3.9 * q * (1 - q)
    print(p,q)

#zad 8.2
ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
visina, masa = eval(input("Unesite visinu i masu: "))

print("Uneti podaci su: ", ime, prezime, visina, masa)
