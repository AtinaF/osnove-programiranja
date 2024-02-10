from Projekat import (users, movie, screening_term, screening as screening_module,
                      hall, screening_term_search_result, ticket,
                      reserved_tickets_info)

logged_in_user_data = {
    'logged_in_username': "",
    'logged_in_password': "",
    'logged_in_role': ""
}

def main():
    global logged_in_user_data
    print("\nEvidencija rada bioskopa")
    print("========================\n")
    komanda = '0'
    while komanda != 'X':
        if is_logged_in():
            komanda = handle_logged_in_user()           
        else:
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
                    elif logged_in_user["role"] == '2':
                        logged_in_user_data['logged_in_role'] = '2'
                    elif logged_in_user["role"] == '3':
                        logged_in_user_data['logged_in_role'] = '3'
                else:
                    print("Korisnik sa datim korisnickim imenom i lozinkom ne postoji")
            elif komanda=='3':
                list_movies()
                # reserve_ticket_as_buyer()
            elif komanda=='4':
                search_movies_by_one_criterion()
            elif komanda=='5':
                search_movies_by_multiple_criteria()
            elif komanda=='6':
                search_screening_terms()

    print("Dovidjenja.")


def add_seller():
    if logged_in_user_data["logged_in_role"] == '1':
        print("[5]  Dodavanje prodavca ili menadzera")
        user = {}
        user["username"] = input("Unesite korisnicko ime >>").strip()
        user["password"] = input("Unesite lozinku >>").strip()
        user["name"] = input("Unesite ime >>").strip()
        user["surname"] = input("Unesite prezime >>").strip()
        user["role"] = input("Unesite ulogu [1] menadzer, [2] prodavac >>").strip()
        if not(user["role"] == "2") and not(user["role"] == "1"):
            print("Neuspesno dodavanje korisnika.\n")
            print("Uneli ste nepostojecu ulogu.\n")
        elif (is_validated(user)):
            is_added = users.add_user(user)
            if is_added == -1:
                print("Neuspesno dodavanje korisnika.\n")
                print("Korisnik sa tim korisnickim imenom vec postoji u sistemu.\n")
            elif is_added == -2:
                print("Neuspesno dodavanje korisnika.\n")
            else:
                #users.save_users()
                print("Uspesno dodavanje korisnika: ")
                print(users.format_header())
                print(users.format_user(user))
    else:
        print("Samo menadzer ima mogucnost dodavanja novog menadzera ili korisnika u sistem.")


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
        print("Ime i prezime smeju sadrzati samo slova. Korisnicko ime i lozinka moraju sadrzati bar jedno slovo, a smeju sadrzati i slova i brojeve.")
        return False
    else:
        return True


def register():
    if not is_logged_in():
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
            else:
                users.save_users()
                print("Uspesna registracija korisnika: ")
                print(users.format_header())
                print(users.format_user(usr))
    else:
        print("Vec ste prijavljeni na sistem. Odjavite se za mogucnost registracije.")


def login():
    if not is_logged_in():
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
        #print(user_to_update)

        if is_validated(user_to_update):
            users.update_user_data(user_to_update)
            logged_in_user_data["logged_in_user_password"] = password
        else:
            print("Neuspesna izmena podataka.")
    else:
        print("Morate biti prijavljeni, da bi izmenili podatke.")


def list_movies():
    print(movie.format_header())
    print(movie.format_all_movies())


def get_user_criterion():
    available_criteria = {
        "title": "naziv filma",
        "genre": "zanr",
        "duration": "trajanje",
        "director": "reziser",
        "main_roles": "glavne uloge",
        "country": "zemlja porekla",
        "year": "godina proizvodnje",
        "description": "opis"
    }

    # available_criteria_sr = ["naziv filma", "zanr", "trajanje", "reziser", "glavne uloge", "zemlja porekla", "godina proizvodnje", "opis"]
    # available_criteria_en = ["title", "genre", "duration", "director", "main_roles", "country", "year", "description"]

    print("Dostupni kriterijumi:")
    for index, criterion in enumerate(available_criteria.values(), start=1):
        print(f"{index}. {criterion}")

    while True:
        try:
            choice = int(input("Izaberi kriterijum (unesi odgovarajuci broj): "))
            if 1 <= choice <= len(available_criteria.values()):
                return list(available_criteria.keys())[choice - 1]
            else:
                print("Pogresan izbor. Unesite ispravan broj.")
        except ValueError:
            print("Pogresan izbor. Unesite broj.")


def get_user_criteria():
    criteria = []
    command = '0'
    print("Dodavanje kriterijuma pretrage")
    while command.upper() != "X":
        criteria.append(get_user_criterion())
        command = input("Unesite 'x' - za kraj unosa, ili bilo sta drugo za nastavak>> ")
    # print(criteria)
    return list(set(criteria))


def search_movies_by_one_criterion():
    criterion = get_user_criterion()
    search_term = input("Unesite izraz za pretragu >> ")
    filtered_movies = movie.filter_movies_by_criterion(criterion, search_term)
    print(movie.format_header())
    print(movie.format_movies(filtered_movies))


def search_movies_by_multiple_criteria():
    en_sr_criteria = {
        "title": "naziv filma",
        "genre": "zanr",
        "duration": "trajanje",
        "director": "reziser",
        "main_roles": "glavne uloge",
        "country": "zemlja porekla",
        "year": "godina proizvodnje",
        "description": "opis"
    }
    criteria = get_user_criteria()
    search_terms = []

    for criterion in criteria:
        search_terms.append(input(f"Unesite izraz za pretragu po kriterijumu {en_sr_criteria[criterion]} >> "))
    filtered_movies = movie.filter_movies_by_criteria(criteria, search_terms)

    print(movie.format_header())
    print(movie.format_movies(filtered_movies))


def get_search_results(screening_terms):
    results = []

    for term in screening_terms:
        screening_code = term['code'][:4]
        screening = screening_module.get_screening_by_code(screening_code)

        search_result = {
            'code': term['code'],
            'date': term['date'],
            'movie': screening['movie'],
            'hall': screening['hall'],
            'start_time': screening['start_time'],
            'end_time': screening['end_time']
        }

        results.append(search_result)

    return results


def get_search_option(num_options):
    while True:
        try:
            command = int(input("Izaberite neku od ponudjenih opcija >> "))
            if 1 <= int(command) <= num_options:
                return command
            else:
                print("Pogresan izbor. Unesite ispravan broj.")
        except ValueError:
            print("Pogresan izbor.Unesite broj.")


def search_screening_terms():
    available_criteria = {
        "movie":"naslov filma",
        "code":"sifra projekcije",
        "hall":"sifra sale",
        "date":"datum odrzavanja",
        "start_time":"vreme pocetka projekcije",
        "end_time":"vreme zavrsetka projekcije"
    }

    print("Dostupni kriterijumi:")
    for index, option in enumerate(available_criteria.values(), start=1):
        print(f"{index}. {option}")

    command = get_search_option(len(available_criteria.keys()))

    criteria = list(available_criteria.keys())[command-1]
    criteria_sr = list(available_criteria.values())[command-1]
    search_term = input(f"Unesite vrednost za pretragu po kriterijumu pretrage: {criteria_sr} >> ")
    screening_terms = screening_term.get_screening_terms_by_criteria(criteria, search_term.strip())

    results = get_search_results(screening_terms)
    screening_term_search_result.add_screening_term_search_results(results)

    print(screening_term_search_result.format_header())
    print(screening_term_search_result.format_all_screening_term_search_results())


def is_valid_screening_term_code(code):
    if not screening_term.code_exists_in_screening_terms(code):
        return False
    return True


def get_seat(hal, screening_term_code):
    while True:
        try:
            seat_row = int(input("Unesite red zeljenog sedista >> "))
            seat_column = input("Unesite oznaku sedista >> ").upper()
            seat = f"{seat_row}{seat_column}"

            if (1 <= seat_row and seat_row <= int(hal['num_rows'])
                    and not ticket.is_seat_occupied(seat, screening_term_code)):
                return seat
            else:
                print("Izabrani red je izvan opsega sale ili ste izabrali zauzeto sediste.")
        except ValueError:
            print("Red mora biti broj.")


def sell_tickets():
    command = ""
    while command.upper() != 'N':
        print(f"Pretraga termina projekcije\n{'-' * 27}")
        search_screening_terms()
        code = ""
        while not is_valid_screening_term_code(code):
            code = input("Unesite sifru zeljene projekcije >> ").strip().upper()

        hall_code = screening_module.get_hall_by_screening_code(code[:4])
        hal = hall.get_hall_by_code(hall_code)
        rows = hall.format_hall_rows(hal, code)
        print(f"Slobodni redovi\n{'_' * 15}\nSala: {hal['code']}\n")
        print(hall.format_rows(rows))

        seat = get_seat(hal, code)

        if logged_in_user_data['logged_in_role'] == '3':
            username = logged_in_user_data['logged_in_username']
        elif logged_in_user_data['logged_in_role'] == '2':
            username = input("Unesite ime i prezime, ili korisnicko ime korisnika >> ")
        else:
            username = input("Unesite ime i prezime >> ")

        ticket.sell_ticket(code, seat, username)
        command = input("Da li zelite da prodate jos karata? [y:n] >> ")




def reserve_ticket():
    command = ""
    while command.upper() != 'N':
        print(f"Pretraga termina projekcije\n{'-'*27}")
        search_screening_terms()
        code = ""
        while not is_valid_screening_term_code(code):
            code = input("Unesite sifru zeljene projekcije >> ").strip().upper()

        hall_code = screening_module.get_hall_by_screening_code(code[:4])
        hal = hall.get_hall_by_code(hall_code)
        rows = hall.format_hall_rows(hal, code)
        print(f"Slobodni redovi\n{'_'*15}\nSala: {hal['code']}\n")
        print(hall.format_rows(rows))

        seat = get_seat(hal, code)

        if logged_in_user_data['logged_in_role'] == '3':
            username = logged_in_user_data['logged_in_username']
        elif logged_in_user_data['logged_in_role'] == '2':
            username = input("Unesite ime i prezime, ili korisnicko ime korisnika >> ")
        else:
            username = input("Unesite ime i prezime >> ")

        ticket.reserve_ticket(code, seat, username)
        command = input("Da li zelite da rezervisete jos karata? [y:n] >> ")


def sell_reserved_tickets():
    show_reserved_tickets()
    print(f"Prodaja rezervisanih karata\n{'_'*27}")
    screening_term_code = input("Unesite sifru termina projekcije >> ")
    seat = input("Unesite oznaku sedista >> ")
    ticket.sell_reserved_ticket(screening_term_code, seat)


def get_reserved_tickets_info(reserved_tickets):
    reserved_tickets_info = []

    for reserved_ticket in reserved_tickets:
        screening_code = reserved_ticket['screening_term_code'][:4]
        screening = screening_module.get_screening_by_code(screening_code)

        username = reserved_ticket['username']
        user = users.get_user_by_username(username)

        if user is None: # karta pripada neregistrovanom korisniku
            name_and_surname = reserved_ticket['username']
        else:
            name = user['name']
            surname = user['surname']
            name_and_surname = f"{name} {surname}"

        reserved_ticket_info = {
            'screening_term_code': reserved_ticket['screening_term_code'],
            'movie': screening['movie'],
            'seat': reserved_ticket['seat'],
            'reservation_date': reserved_ticket['date'],
            'start_time': screening['start_time'],
            'end_time': screening['end_time'],
            'user_name_and_surname': name_and_surname,
            'reservation_status': reserved_ticket['reserved']
        }

        reserved_tickets_info.append(reserved_ticket_info)

    return reserved_tickets_info


def show_reserved_tickets():
    if logged_in_user_data['logged_in_role'] == '2':
        reserved_tickets = ticket.get_all_reserved_tickets()
    else:
        username = logged_in_user_data['logged_in_username']
        reserved_tickets = ticket.get_reserved_tickets_by_username(username)

    result = get_reserved_tickets_info(reserved_tickets)

    print(reserved_tickets_info.format_header())
    print(reserved_tickets_info.format_reserved_tickets_info(result))


# def is_valid_seat(seat):
#     return ticket.seat_belongs_to_user(seat, logged_in_user_data['logged_in_username'])

def show_all_tickets():
    tickets = ticket.get_all_tickets()
    result = get_reserved_tickets_info(tickets)
    print(reserved_tickets_info.format_header())
    print(reserved_tickets_info.format_reserved_tickets_info(result))


def cancel_reservation():
    print(f"Brisanje rezervacija\n{'_'*20}")
    command = ""
    while command.upper() != 'N':
        show_reserved_tickets()

        screening_term_code = input("Unesite sifru projekcije za rezervaciju koju zelite da obrisete >> ").strip().upper()
        seat = input("Unesite oznaku sedista za rezervaciju koju zelite da obrisete >> ").strip().upper()
        result = ticket.cancel_reservation(screening_term_code, seat, logged_in_user_data['logged_in_username'])
        if result:
            print("Uspesno ponistavanje rezervacije.")
        else:
            print("Neuspelo brisanje rezervacije.")

        command = input("Da li zelite da nastavite sa otkazivanjem rezervacija? [y:n] >> ")


def cancel_tickets():
    print(f"Ponistavanje karte\n{'_'*20}")
    command = ""
    while command.upper() != 'N':
        show_all_tickets()

        screening_term_code = input("Unesite sifru projekcije za kartu koju zelite da ponistite >> ").strip().upper()
        seat = input("Unesite oznaku sedista za kartu koju zelite da ponistite >> ").strip().upper()
        result = ticket.cancel_ticket(screening_term_code, seat)
        if result:
            print("Uspesno ponistavanje karte.")
        else:
            print("Neuspelo ponistavanje karte.")

        command = input("Da li zelite da nastavite sa otkazivanjem rezervacija? [y:n] >> ")


def get_search_criteria_and_search_term(command, available_criteria):
    search_criteria = list(available_criteria.keys())[command-1]
    if command == 7:
        ticket_status = input("Izaberite opciju\n"
                              "1. rezervisane karte\n2. kupljene karte\n >> ")
        if ticket_status == '1':
            search_term = 'reserved'
        else:
            search_term = 'sold'
    else:
        search_term = input(f"Unesite izraz za pretragu po kriterijumu {list(available_criteria.values())[command-1]} >> ")
    return search_criteria, search_term


def search_tickets_by_criteria():
    available_criteria = {
        "screening_term_code": "sifra projekcije",
        "name": "ime kupca",
        "surname": "prezime kupca",
        "date": "datum",
        "start_time": "vreme pocetka projekcije",
        "end_time": "vreme kraja projekcije",
        "reserved": "da li je u pitanju rezervacija/kupovina"
    }

    for index, criteria in enumerate(available_criteria.values(), start=1):
        print(f"{index}.{criteria}")

    command = get_search_option(len(available_criteria.keys()))
    search_criteria, search_term = get_search_criteria_and_search_term(command, available_criteria)
    tickets = ticket.get_tickets_by_criteria(search_criteria, search_term)

    results = get_reserved_tickets_info(tickets)
    print(reserved_tickets_info.format_header())
    print(reserved_tickets_info.format_reserved_tickets_info(results))



def generate_screening_terms():
    screening_terms = screening_module.get_screening_terms()
    screening_term.generate_screening_terms(screening_terms)
    print(screening_term.format_header())
    print(screening_term.format_screening_terms(screening_terms))


def menu():
    print_menu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        print_menu()
        command = input(">> ")
    return command.upper()


def seller_menu():
    print_seller_menu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        print_seller_menu()
        command = input(">> ")
    return command.upper()


def buyer_menu():
    print_buyer_menu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        print_buyer_menu()
        command = input(">> ")
    return command.upper()


def manager_menu():
    print_manager_menu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'X'):
        print("\nUneli ste pogresnu komandu\n")
        print_manager_menu()
        command =  input(">> ")
    return command.upper()


def print_menu():
    print("\nIzaberite opciju:")
    print(" 1 - registruj se")
    print(" 2 - uloguj se")
    print(" 3 - pregledaj dostupne filmove")
    print(" 4 - pretrazi filmove po jednom kriterijumu")
    print(" 5 - pretrazi filmove po vise kriterijuma")
    print(" 6 - pretrazi termine bioskopskih projekcija")
    print(" X - izlaz iz programa")


def print_manager_menu():
    print("MENADZER\nIzaberi opciju:")
    print("1 - Registruj novog prodavca")
    print("2 - Dobavi izvestaj")
    print("3 - Proveri popust za karticu lojalnosti")
    print("4 - Prikazi sedista kao matricu")
    print("5 - izmeni cenu karte")
    print("6 - izloguj se")
    print("7 - izmeni licne podatke")
    print("8 - pregledaj dostupne filmove")
    print("9 - pretrazi filmove po jednom kriterijumu")
    print("10 - pretrazi filmove po vise kriterijuma")
    print("11 - pretrazi termine bioskopskih projekcija")
    print("12 - generisi termine za bioskopske projekcije u naredne 2 nedelje")
    print("X - izlaz iz programa")


def print_seller_menu():
    print("PRODAVAC\nIzaberi opciju: ")
    print("1 - rezervisi kartu")
    print("2 - pregledaj rezervisane karte")
    print("3 - ponisti rezervaciju / prodaju")
    print("4 - pretrazi karte")
    print("5 - direktna prodaja karata")
    print("6 - prodaj rezervisanu kartu")
    print("7 - izmeni kartu")
    print("8 - ponisti rezervaciju 30 min pre pocetka projekcije")
    #todo p2
    print("9 - izloguj se")
    print("10 - izmeni licne podatke")
    print("11 - pregledaj dostupne filmove")
    print("12 - pretrazi filmove po jednom kriterijumu")
    print("13 - pretrazi filmove po vise kriterijuma")
    print("14 - pretrazi termine bioskopskih projekcija")
    print("X - izlaz iz programa")


def print_buyer_menu():
    print("\nIzaberite opciju: ")
    print("1 - rezervisi kartu")
    print("2 - pregledaj svoje rezervisane karte")
    print("3 - ponisti rezervaciju karte")
    print("4 - izloguj se")
    print("5 - izmeni licne podatke")
    print("6 - pregledaj dostupne filmove")
    print("7 - pretrazi filmove po jednom kriterijumu")
    print("8 - pretrazi filmove po vise kriterijuma")
    print("9 - pretrazi termine bioskopskih projekcija")
    print("X - izlaz iz programa")


def handle_manager_command(command):
    if command == '1':
        add_seller()
    elif command == '2':
        print("TODO")
    elif command == '3':
        print("TODO")
    elif command == '4':
        print("TODO")
    elif command == '5':
        print("TODO")
    elif command == '6':
        logout()
    elif command == '7':
        update_user()
    elif command == '8':
        list_movies()
    elif command == '9':
        search_movies_by_one_criterion()
    elif command == '10':
        search_movies_by_multiple_criteria()
    elif command == '11':
        search_screening_terms()
    elif command == '12':
        generate_screening_terms()


def handle_seller_command(command):
    if command == '1':
        reserve_ticket()
    elif command == '2':
        show_reserved_tickets()
    elif command == '3':
        cancel_tickets()
    elif command == '4':
        search_tickets_by_criteria()
    elif command == '5':
        sell_tickets()
    elif command == '6':
        sell_reserved_tickets()
    elif command == '7':
        print("TODO")
    elif command == '8':
        print("TODO")
    elif command == '9':
        logout()
    elif command == '10':
        update_user()
    elif command == '11':
        list_movies()
    elif command == '12':
        search_movies_by_one_criterion()
    elif command == '13':
        search_movies_by_multiple_criteria()
    elif command == '14':
        search_screening_terms()


def handle_buyer_command(command):
    if command == '1':
        reserve_ticket()
    elif command == '2':
        show_reserved_tickets()
    elif command == '3':
        cancel_reservation()
    elif command == '4':
        logout()
    elif command == '5':
        update_user()
    elif command == '6':
        list_movies()
    elif command == '7':
        search_movies_by_one_criterion()
    elif command == '8':
        search_movies_by_multiple_criteria()
    elif command == '9':
        search_screening_terms()


def handle_logged_in_user():
    global logged_in_user_data
    command = -1
    if logged_in_user_data['logged_in_role'] == '1':
        command = manager_menu()
        handle_manager_command(command)
    elif logged_in_user_data['logged_in_role'] == '2':
        command = seller_menu()
        handle_seller_command(command)
    elif logged_in_user_data['logged_in_role'] == '3':
        command = buyer_menu()
        handle_buyer_command(command)
    return command

if __name__ == '__main__':
    # date = datetime.date.today()
    # print(date)
    # print(date.strftime('%d.%m.%Y'))
    main()