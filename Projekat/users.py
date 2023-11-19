# from enum import Enum
# Role = Enum('Role', {'MANAGER' : 1, 'SELLER' : 2, 'BUYER' : 3})
# print(role.MANAGER)         #Role.MANAGER
# print(role.MANAGER.value)   #1
# print(role.SELLER.value)   #2
# print(role.BUYER.value)   #3
from os.path import exists
import re
# # Example dictionary
# user_data = {
#     'username': 'john_doe',
#     'role': 2  # Numeric representation for 'SELLER'
# }
#
# # Checking if the 'role' field corresponds to enum values
# if user_data['role'] in [role.value for role in Role]:
#     print(f"The role '{user_data['role']}' is a valid numeric representation.")
# else:
#     print(f"The role '{user_data['role']}' is not a valid numeric representation.")

min_username_length = 1
max_username_length = 20
min_password_length = 7
max_password_length = 20    # samo za inicijalno formatiranje tabele
min_name_length = 1
max_name_length = 15
min_surname_length = 1
max_surname_length = 15

#for dynamic table creation
#todo sacuvaj rad sa dinamickom tabelom u drugom fajlu
#sirine kolona u tabeli
# username_column_length = 0
# password_column_length = 0
# name_column_length = 0
# surname_column_length = 0
role_column_length = 10

#ispis u hzaglavlju tabele
hearder_username = "Korisnicko ime"
header_password = "Lozinka"
header_name = "Ime"
header_surname = "Prezime"
header_role = "Uloga"


def usr2str(usr):
    return '|'.join([usr['username'], usr['password'], usr['name'], usr['surname'], usr['role']])


def str2usr(line):
    if line[-1] == '\n':
        line = line[:-1]
        username, password, name, surname, role = line.split('|')
        user = {
            'username': username,
            'password': password,
            'name': name,
            'surname': surname,
            'role': role
        }
        return user
# TODO vrati None i u pozivu funkcije proveri sta je vratila, ili pazi gde je pozivas


def check_file():
    if not exists('users.txt'):
        open('users.txt', 'w').close()


def load_users():
    check_file()
    users_file = open("users.txt", 'r')
    for line in users_file.readlines():
        if len(line) > 1:
            usr = str2usr(line)
            users.append(usr)
    users_file.close()


def save_users():
    users_file = open("users.txt", 'w')
    for user in users:
        line = usr2str(user)
        users_file.write(line)
        users_file.write('\n')

    users_file.close()

# #for dynamic table creation (if max field lengths change)
# def set_table_column_sizes():
#     # Read lines from the file
#     check_file()
#     with open("users.txt", 'r') as file:
#         for line in file:
#             username, password, name, surname, role = line.strip().split('|')
#             # Update maximum lengths
#             username_column_length = max(username_column_length, len(username), hearder_username)
#             password_column_length = max(password_column_length, len(password), header_password)
#             name_column_length = max(name_column_length, len(name), header_name)
#             surname_column_length = max(surname_column_length, len(surname), header_surname)
# TODO
# ZAHTEVA DA CUVAS OVE 4 VREDNOSTI POREFERENCI, I IZMENIS KOD - >SACUVAS IH U LISTU PA IM PRISTUPAS PREKO ODGOVARAJUCEG INDEKSTA U LISTI, UMESTO U samih polja "colume_leng"
#     return username_column_length, password_column_length, name_column_length, surname_column_length

def format_header():
    #ispis sa kolonom lozinke
    header = "{0}|{1}|{2}|{3}|{4}\n".format(hearder_username.ljust(max_username_length),
                                   header_password.ljust(max_password_length),
                                   header_name.ljust(max_name_length),
                                   header_surname.ljust(max_surname_length),
                                   header_role.ljust(role_column_length))
    lines = "{0}+{1}+{2}+{3}+{4}".format('_'*max_username_length,
                                         '_'*max_password_length,
                                         '_'*max_name_length,
                                         '_'*max_surname_length,
                                         '_'*role_column_length)

    #ZAHTEVA IZMENU U FORMATIRANJU KORISNIKA
    # ispis bez kolone lozinke:
    # header = "{0}|{1}|{2}|{3}\n".format(hearder_username.ljust(max_username_length),
    #                                     header_name.ljust(max_name_length),
    #                                     header_surname.ljust(max_surname_length),
    #                                     header_role.ljust(role_column_length))
    # lines = "{0}+{1}+{2}+{3}".format('_' * max_username_length,
    #                                      '_' * max_name_length,
    #                                      '_' * max_surname_length,
    #                                      '_' * role_column_length)
    # # dinamicka tabelasa lozinkom
    # # (velicine kolona su prilagodjene "nepoznatim" duzinama podataka u tim kolonama)
    # set_table_column_sizes()
    # header = "{0}|{1}|{2}|{3}|{4}\n".format(hearder_username.ljust(username_column_length),
    #                                         header_password.ljust(password_column_length),
    #                                         header_name.ljust(name_column_length),
    #                                         header_surname.ljust(surname_column_length),
    #                                         header_role.ljust(role_column_length))
    # lines = "{0}+{1}+{2}+{3}+{4}".format('_' * username_column_length,
    #                                      '_' * password_column_length,
    #                                      '_' * name_column_length,
    #                                      '_' * surname_column_length,
    #                                      '_' * role_column_length)
    # # dinamicka tabela bez lozinke
    # set_table_column_sizes()
    # header = "{0}|{1}|{2}|{3}\n".format(hearder_username.ljust(username_column_length),
    #                                         header_name.ljust(name_column_length),
    #                                         header_surname.ljust(surname_column_length),
    #                                         header_role.ljust(role_column_length))
    # lines = "{0}+{1}+{2}+{3}".format('_' * username_column_length,
    #                                      '_' * name_column_length,
    #                                      '_' * surname_column_length,
    #                                      '_' * role_column_length)

    return  "{}{}".format(header, lines)


def format_user(usr):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:>{}}}").format(max_username_length,
                                max_password_length,
                                max_name_length,
                                max_surname_length,
                                role_column_length).format(usr["username"],
                                                            usr["password"],
                                                            usr["name"],
                                                            usr["surname"],
                                                            usr["role"])
    # #format bez lozinke
    # return ("{{0:{}}}|"
    #         "{{1:{}}}|"
    #         "{{2:{}}}|"
    #         "{{3:{}}}").format(max_username_length,
    #                             max_name_length,
    #                             max_surname_length,
    #                             role_column_length).format(usr["username"],
    #                                                        usr["name"],
    #                                                        usr["surname"],
    #                                                        usr["role"])
    # # dinamicki format sa lozinkom
    # set_table_column_sizes()
    # return ("{{0:{}}}|"
    #         "{{1:{}}}|"
    #         "{{2:{}}}|"
    #         "{{3:{}}}|"
    #         "{{4:>{}}}").format(username_column_length,
    #                             password_column_length,
    #                             name_column_length,
    #                             surname_column_length,
    #                             role_column_length).format(usr["username"],
    #                                                        usr["password"],
    #                                                        usr["name"],
    #                                                        usr["surname"],
    #                                                        usr["role"])
    # #dinamicki format bez lozinke
    # return ("{{0:{}}}|"
    #         "{{1:{}}}|"
    #         "{{2:{}}}|"
    #         "{{3:{}}}").format(username_column_length,
    #                            name_column_length,
    #                            surname_column_length,
    #                            role_column_length).format(usr["username"],
    #                                                       usr["name"],
    #                                                       usr["surname"],
    #                                                       usr["role"])
def format_users(user_list):
    result = ""
    for usr in user_list:
        result += format_user(usr) + '\n'
    return result


def format_all_users():
    return format_users(users)


def contains_number(password):
    return bool(re.search(r'\d', password))


def is_password_valid(password):
    if len(password) < min_password_length or not contains_number(password):
        return False
    return True


#ogranicenja zbog formatiranja tabele
#neka korisnicko ime ima [1-10] karaktera
#neka password bude duzi od 6 i sadrzi broj
#neka je ime izmedju [1-15] karaktera
#neka je prezime izmedju [1-15] karaktera
def is_valid_input(user):
    if len(user["username"]) < min_username_length or len(user["username"]) > max_username_length:
        return -1
    elif not is_password_valid(user["password"]):
        return -2
    elif len(user["name"]) < min_name_length or len(user["name"]) > max_name_length:
        return -3
    elif len(user["surname"]) < min_surname_length or len(user["surname"]) > max_surname_length:
        return -4
    return 1

def add_user(user):
        for usr in users:
            if usr["username"] == user["username"]:
                return -1
        users.append(user)


def login(username, password):
    for usr in users:
        if usr["username"] == username and usr["password"] == password:
            return True
    return False


def find_user(username, password):
    for usr in users:
        if usr["username"] == username and usr["password"] == password:
            return usr
    return None


users = []
load_users()

print(format_header())
print(format_all_users())

