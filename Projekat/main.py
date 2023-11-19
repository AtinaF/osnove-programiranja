import users

logged_in_username = ""
logged_in_password = ""

def main():
    print()
    print("Evidencija rada bioskopa")
    print("========================")
    print()
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            register()
        elif komanda == '2':
            while not login():
                print("Uneli ste pogresnu kombinaciju korisnickog imena i lozinke.")
            print("Uspesna prijava.\n")
            logged_in_user = users.find_user(logged_in_username, logged_in_password)
            if logged_in_user["role"] == '1':
                print_manager_menu()
            elif logged_in_user["role"] == '2':
                print_seller_menu()
            elif logged_in_user["role"] == '3':
                print_buyer_menu()
        elif komanda == '3':
            logout()

    print("Dovidjenja.")


def register():
    print("[1] Registracija novog korisnika\n")
    usr = {}
    usr['username'] = input("Unesite korisnicko ime >> ")
    usr['password'] = input("Unesite lozinku >> ")
    usr['name'] = input("Unesite ime >> ")
    usr['surname'] = input("Unesite prezime >> ")
    usr['role'] = '3'
    is_valid = users.is_valid_input(usr)
    if is_valid == -1:
        print("Neuspesna registracija.\n")
        print("Korisnicko ime mora sadrzati izmedju {} i {} karaktera.\n".format(users.min_username_length, users.max_username_length))
    elif is_valid == -2:
        print("Neuspesna registracija.\n")
        print("Lozinka mora sadrzati bar {} karaktera i mora sadrzati bar jedno slovo.\n".format(users.min_password_length))
    elif is_valid == -3:
        print("Neuspesna registracija.\n")
        print("Ime mora sadrzati izmedju {} i {} karaktera.\n".format(users.min_name_length, users.max_name_length))
    elif is_valid == -4:
        print("Neuspesna registracija.\n")
        print("Prezime mora sadrzati izmedju {} i {} karaktera.\n".format(users.min_surname_length, users.max_surname_length))
    else:
        is_added = users.add_user(usr)
        if is_added == -1:
            print("Neuspesna registracija.\n")
            print("Korisnik sa tim korisnickim imenom vec postoji u sistemu.\n")
        else:
            print("Uspesna registracija korisnika: ")
            print("{}".format(users.usr2str(usr)))  #todo delete comment, ovo je samo za test
            users.save_users()

def login():
    print("[1] Prijava na sistem\n")
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    #sacuvam usrname i pass ulogovanog za kasnije
    logged_in_username = username
    logged_in_password = password
    return users.login(username, password)

def logout():
    users.logout()

def menu():
    print_menu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        print_menu()
        command = input(">> ")
    return command.upper()


def print_menu():
    print("\nIzaberite opciju:")
    print(" 1 - registruj se")
    print(" 2 - uloguj se")
    print(" 3 - odjavi se")
    # print(" 4 - pregledaj dostupne filmove")
    # print(" 5 - pretrazi filmove po jednom kriterijumu")
    # print(" 6 - pretrazi filmove po vise kriterijuma")
    # print(" 7 - pretrazi termine bioskopskih")
    print(" x - izlaz iz programa")

def print_manager_menu():
    pass


def print_seller_menu():
    pass


def print_buyer_menu():
    pass


if __name__ == '__main__':
    main()