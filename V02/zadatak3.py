# Napiši program koji od korisnika traži da unosi brojeve sve dok ne unese
# neparni broj. Kada korisnik unese neparni broj, izvršavanje programa se prekida
# i korisniku se ispisuje suma prethodno unetih (parnih) brojeva.
user_input = 2
total = 0

while user_input % 2 != 1:
    user_input = eval(input("Enter a number: "))
    if user_input % 2 == 0:
        total += user_input

print(f"total = {total}")