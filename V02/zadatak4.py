# Napišite Python program koji će korisnika pitati za vrednosti naelektrisanja i rastojanja
# između dve tačkaste naelektrisane čestice i zatim izračunati i ispisati elektrostatičku silu
# izmeđunjih. Kulonov zakon kaže da je elektrostatička sila između dve tačkaste naelektrisane
# čestice:
# 𝐹=𝑘∗|𝑞1∗𝑞2|𝑟2
# gde je:
# F elektrostatička sila,
# k elektrostatička konstanta (≈8.99∗109)
# q1 naelektrisanje prve čestice,
# q2 naelektrisanje druge čestice,
# r rastojanje između čestica.

distance = eval(input("Enter the distance: "))
charge1, charge2 = eval(input("Enter 2 charges: "))

k = 8.99*109
force = k * abs(charge1 * charge2) * distance

print(f"Electro static force between charges {charge1} and {charge2} "
      f"is {force} for distance {distance}")