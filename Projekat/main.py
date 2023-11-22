import users

logged_in_user_data = {
    'logged_in_username': "",
    'logged_in_password': "",
    'logged_in_role': ""
}


def main():
    global logged_in_user_data
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
            logged_in_user = users.find_user(logged_in_user_data['logged_in_username'], logged_in_user_data['logged_in_password'])
            if logged_in_user != None:
                if logged_in_user["role"] == '1':
                    logged_in_user_data['logged_in_role'] = '1'
                    # while userinput != 'logout':
                    print_manager_menu()
                elif logged_in_user["role"] == '2':
                    logged_in_user_data['logged_in_role'] = '2'
                    print_seller_menu()
                elif logged_in_user["role"] == '3':
                    logged_in_user_data['logged_in_role'] = '3'
                    print_buyer_menu()
            else:
                print("Korisnik sa datim korisnickim imenom i lozinkom ne postoji")
        elif komanda == '3':
            logout()
        elif komanda == '4':
            update_user()
        elif komanda == '5':
            add_seller()

    print("Dovidjenja.")


def add_seller():
    if logged_in_user_data["logged_in_role"] == '1':
        print("[5]  Dodavanje prodavca")
        seller = {}
        seller["username"] = input("Unesite korisnicko ime >>").strip()
        seller["password"] = input("Unesite lozinku >>").strip()
        seller["name"] = input("Unesite ime >>").strip()
        seller["surname"] = input("Unesite prezime >>").strip()
        seller["role"] = input("Unesite ulogu [1] menadzer, [2] prodavac >>").strip()
        if seller["role"] != "2" and seller["role"] != "1":
            print("Neuspesno dodavanje prodavca.\n")
            print("Uneli ste nepostojecu ulogu.\n")
        if (is_validated(seller)):
            is_added = users.add_user(seller)
            if is_added == -1:
                print("Neuspesno dodavanje prodavca.\n")
                print("Korisnik sa tim korisnickim imenom vec postoji u sistemu.\n")
            elif is_added == -2:
                print("Neuspesno dodavanje prodavca.\n")
            else:
                users.save_users()
                print("Uspesno dodavanje prodavca: ")
                print(users.format_header())
                print(users.format_user(seller))

def is_validated(user):
    is_valid = users.is_valid_input(user)
    if is_valid == -1:
        print("Korisnicko ime mora sadrzati izmedju {} i {} karaktera.\n".format(users.MIN_USERNAME_LENGTH, users.MAX_USERNAME_LENGTH))
        return False
    elif is_valid == -2:
        print("Lozinka mora sadrzati izmedju {} i {} karaktera i mora sadrzati bar jedno slovo.\n".format(users.MIN_PASSWORD_LENGTH, users.MAX_PASSWORD_LENGTH))
        return False
    elif is_valid == -3:
        print("Ime mora sadrzati izmedju {} i {} karaktera.\n".format(users.MIN_NAME_LENGTH, users.MAX_NAME_LENGTH))
        return False
    elif is_valid == -4:
        print("Prezime mora sadrzati izmedju {} i {} karaktera.\n".format(users.MIN_SURNAME_LENGTH, users.MAX_SURNAME_LENGTH))
        return False
    elif is_valid == -5:
        print("Ime i prezime smeju sadrzati samo slova. Korisnicko ime i lozinka smeju sadrzati i slova i brojeve.")
        return False
    else:
        return True


def register():
    print("[1] Registracija novog korisnika\n")
    usr = {}
    usr['username'] = input("Unesite korisnicko ime >> ").strip()
    usr['password'] = input("Unesite lozinku >> ").strip()
    usr['name'] = input("Unesite ime >> ").strip()
    usr['surname'] = input("Unesite prezime >> ").strip()
    usr['role'] = '3'
    if(is_validated(usr)):
        is_added = users.add_user(usr)
        if is_added == -1:
            print("Neuspesna registracija.\n")
            print("Korisnik sa tim korisnickim imenom vec postoji u sistemu.\n")
        elif is_added == -2:
            print("Neuspesna registracija.\n")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        else:
            users.save_users()
            print("Uspesna registracija korisnika: ")
            print(users.format_header())
            print(users.format_user(usr))


def login():
    print("[2] Prijava na sistem\n")
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    is_login_successful = users.login(username, password)
    if is_login_successful:
        #sacuvam usrname i pass ulogovanog za kasnije
        logged_in_user_data['logged_in_username'] = username
        logged_in_user_data['logged_in_password'] = password
    return is_login_successful


def logout():
    # ako je ulogovan
    if logged_in_user_data['logged_in_username'] != "" and logged_in_user_data['logged_in_password'] != "":
        result = users.logout()
        logged_in_user_data["logged_in_user_username"] = ""
        logged_in_user_data["logged_in_user_password"] = ""
        logged_in_user_data["logged_in_role"] = ""
        print(result)
    else:
        print("Neprijavljen korisnik se ne moze odjaviti.")


def is_logged_in():
    return logged_in_user_data['logged_in_username'] != "" and \
            logged_in_user_data['logged_in_password'] != "" and \
            logged_in_user_data['logged_in_role'] != ""


def update_user():
    if is_logged_in():
        name = input("Unesite novo ime >> ").strip()
        surname = input("Unesite novo prezime >> ").strip()
        password = input("Unesite novu lozinku >> ").strip()
        user_to_update = {
            "username" : logged_in_user_data["logged_in_username"],
            "password" : password,
            "name" : name,
            "surname" : surname,
            "role" : logged_in_user_data["logged_in_role"]
        }
        if is_validated(user_to_update):
            users.update_user_data(user_to_update)
            logged_in_user_data["logged_in_user_password"] = password
        else:
            print("Neuspesna izmena podataka.")
    else:
        print("Morate biti prijavljeni, da bi izmenili podatke.")

def menu():
    print_menu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        print_menu()
        command = input(">> ")
    return command.upper()


def print_menu():
    print("\nIzaberite opciju:")
    print(" 1 - registruj se")
    print(" 2 - uloguj se")
    print(" 3 - odjavi se")
    print(" 4 - izmeni licne podatke")
    print(" 5 - dodaj prodavca")
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