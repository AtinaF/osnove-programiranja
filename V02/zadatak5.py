# Implementirati program koji postiže prikazano ponašanje:
# a) Koliko brojeva zelite >> 3
# Unesite broj: 2
# Unesite broj: 3
# Unesite broj: 4
# -----------------------
# Prosek je: 3.0

# prosek = 0
# count = eval(input("Koliko brojeva zelite? "))
# inputs = []
#
# while count != 0:
#     inputs.append(eval(input("Unesite broj: ")))
#     count -= 1
#
# prosek = sum(inputs)/inputs.__len__()
#
# print(f"Prosek je {prosek}")

# b) Unesite broj: 2
# Još? "da"
# Unesite broj: 4
# Još? "da"
# Unesite broj: 3
# Još? "ne"
# ------------------------
# Prosek je: 3.0

# inputs = []
# inputs.append(eval(input("Unesite broj: ")))
# user_input = "da"
# while True:
#     user_input = input("Jos? (da : ne)")
#     if user_input == "da":
#         inputs.append(eval(input("Unesite broj: ")))
#     else:
#         break
#
# prosek = sum(inputs)/inputs.__len__()
#
# print(f"Prosek je {prosek}")


# c) Unesite broj (ili 'x' za kraj): 2
# Unesite broj (ili 'x' za kraj): 3
# Unesite broj (ili 'x' za kraj): 4
# Unesite broj (ili 'x' za kraj): 'x'
# ------------------------
# Prosek je: 3.0

user_input = "asd"
inputs = []
while True:
    user_input = input("Unesite broj (ili 'x' za kraj): ")
    if user_input != 'x':
        inputs.append(eval(user_input))
    else:
        break

averge = sum(inputs)/inputs.__len__()
print(f"Prosek je {averge}")
