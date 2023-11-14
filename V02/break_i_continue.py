# break - prekida izvrsavanje petlje
# continue - prekida tekucu iteraciju i prelazi na sledecu

# pr1
print("Odaberi neku opciju ili x za izlaz")
user_input = input(">>")
while user_input != 'x':
    print("Odaberi neku opciju ili x za izlaz")
    user_input = input(">>")

# pr2
user_input = ""
while user_input != 'x':
    print("Odaberi neku opciju ili x za izlaz")
    user_input = input(">>")

# pr3
while True:
    print("Odaberi neku opciju ili x za izlaz")
    user_input = input(">>")
    if user_input == 'x':
        break

