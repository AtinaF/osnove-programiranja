from os.path import exists
import re


#ogranicenja
MIN_USERNAME_LENGTH = 1
MAX_USERNAME_LENGTH = 20
MIN_PASSWORD_LENGTH = 7
MAX_PASSWORD_LENGTH = 20
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 15
MIN_SURNAME_LENGTH = 1
MAX_SURNAME_LENGTH = 15
ROLE_COLUMN_LENGTH = 5

#ispis u zaglavlju tabele
HEADER_USERNAME = "Korisnicko ime"
HEADER_PASSWORD = "Lozinka"
HEADER_NAME = "Ime"
HEADER_SURNAME = "Prezime"
HEADER_ROLE = "Uloga"


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


def check_file():
    if not exists('data/users.txt'):
        open('data/users.txt', 'w').close()


def load_users():
    check_file()
    users_file = open("data/users.txt", 'r')
    for line in users_file.readlines():
        if len(line) > 1:
            usr = str2usr(line)
            users.append(usr)
    users_file.close()


def save_users():
    users_file = open("data/users.txt", 'w')
    for user in users:
        line = usr2str(user)
        users_file.write(line)
        users_file.write('\n')

    users_file.close()


def format_header():
    #ispis sa kolonom lozinke
    header = "{0}|{1}|{2}|{3}|{4}\n".format(HEADER_USERNAME.ljust(MAX_USERNAME_LENGTH),
                                            HEADER_PASSWORD.ljust(MAX_PASSWORD_LENGTH),
                                            HEADER_NAME.ljust(MAX_NAME_LENGTH),
                                            HEADER_SURNAME.ljust(MAX_SURNAME_LENGTH),
                                            HEADER_ROLE.ljust(ROLE_COLUMN_LENGTH))
    lines = "{0}+{1}+{2}+{3}+{4}".format('_' * MAX_USERNAME_LENGTH,
                                         '_' * MAX_PASSWORD_LENGTH,
                                         '_' * MAX_NAME_LENGTH,
                                         '_' * MAX_SURNAME_LENGTH,
                                         '_' * ROLE_COLUMN_LENGTH)

    return "{}{}".format(header, lines)


def format_user(usr):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:>{}}}").format(MAX_USERNAME_LENGTH,
                                MAX_PASSWORD_LENGTH,
                                MAX_NAME_LENGTH,
                                MAX_SURNAME_LENGTH,
                                ROLE_COLUMN_LENGTH).format(usr["username"],
                                                           usr["password"],
                                                           usr["name"],
                                                           usr["surname"],
                                                           usr["role"])


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
    if len(password) < MIN_PASSWORD_LENGTH or not contains_number(password):
        return False
    return True


def has_at_least_one_letter(text):
    pattern = re.compile(r'[a-zA-Z]')
    return bool(pattern.search(text))


def has_only_letters(text):
    pattern = re.compile(r'^[a-zA-Z]+$')
    return bool(pattern.match(text))


def has_only_numbers_and_letters(text):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(pattern.match(text))


def is_valid_input(user):
    # proveri da li ima neke nedozvoljene karaktere
    if not has_only_numbers_and_letters(user["username"]) or \
        not has_only_numbers_and_letters(user["password"]) or \
        not has_at_least_one_letter(user["username"]) or \
        not has_at_least_one_letter(user["password"]) or \
        not has_only_letters(user["name"]) or \
        not has_only_letters(user["surname"]):
        return -5
    # proveri da li izlazi iz opsega duzine podatka
    if len(user["username"]) < MIN_USERNAME_LENGTH or len(user["username"]) > MAX_USERNAME_LENGTH:
        return -1
    elif not is_password_valid(user["password"]):
        return -2
    elif len(user["name"]) < MIN_NAME_LENGTH or len(user["name"]) > MAX_NAME_LENGTH:
        return -3
    elif len(user["surname"]) < MIN_SURNAME_LENGTH or len(user["surname"]) > MAX_SURNAME_LENGTH:
        return -4
    return 1


def add_user(user):
    if is_valid_input(user):
        for usr in users:
            if usr["username"] == user["username"]:
                return -1
        users.append(user)
        save_users()
    else:
        return -2


def login(username, password):
    for usr in users:
        if usr["username"] == username and usr["password"] == password:
            return True
    return False


def logout():
    return "Uspesno ste se izlogovali"


def find_user(username, password):
    for usr in users:
        if usr["username"] == username and usr["password"] == password:
            return usr
    return None


def get_user_by_username(username):
    for usr in users:
        if usr["username"] == username:
            return usr
    return None


def update_user_data(user_to_update):
    usr = get_user_by_username(user_to_update["username"])
    if usr is not None:
        users.remove(usr)
        users.append(user_to_update)
        save_users()
    else:
        print("Ovde puca")


users = []
load_users()

print(format_header())
print(format_all_users())


# user_to_update = {
#             "username" : "bsmith",
#             "password" : "pass221",
#             "name" : "jkljkljkl",
#             "surname" : "iopioiop",
#             "role" : "2"
#         }
# update_user_data(user_to_update)
