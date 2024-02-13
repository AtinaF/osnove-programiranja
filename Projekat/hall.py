from os.path import exists

from Projekat import ticket

#ogranicenja
MIN_CODE_LENGTH = 1
MAX_CODE_LENGTH = 20
MIN_NAME_LENGTH = 7
MAX_NAME_LENGTH = 20
MIN_NUM_ROWS_LENGTH = 1
MAX_NUM_ROWS_LENGTH = 15
MIN_SEAT_MARKING_LENGTH = 1
MAX_SEAT_MARKING_LENGTH = 25

#ispis u zaglavlju tabele
HEADER_CODE = "Sifra sale"
HEADER_NAME = "Naziv sale"
HEADER_NUM_ROWS = "Broj redova"
HEADER_SEAT_MARKING = "Oznaka sedista"


def hall2str(hall):
    return "|".join([hall["code"], hall["name"], hall["num_rows"], hall["seat_marking"]])


def str2hall(line):
    code, name, num_rows, seat_marking = line.split('|')
    hall = {
        "code":code,
        "name":name,
        "num_rows":num_rows,
        "seat_marking":seat_marking[:-1]
    }
    return hall


def check_file():
    if not exists('data/halls.txt'):
        open('data/halls.txt', 'w').close()


def load_halls():
    check_file()
    halls_file = open("data/halls.txt", 'r')
    for line in halls_file.readlines():
        if len(line) > 1:
            hall = str2hall(line)
            halls.append(hall)
    halls_file.close()


def save_halls():
    halls_file = open("data/halls.txt", 'w')
    for hall in halls:
        line = hall2str(hall)
        halls_file.write(line)
        halls_file.write('\n')

    halls_file.close()


def format_header():
    header = "{0}|{1}|{2}|{3}\n".format(HEADER_CODE.ljust(MAX_CODE_LENGTH),
                                            HEADER_NAME.ljust(MAX_NAME_LENGTH),
                                            HEADER_NUM_ROWS.ljust(MAX_NUM_ROWS_LENGTH),
                                            HEADER_SEAT_MARKING.ljust(MAX_SEAT_MARKING_LENGTH))
    lines = "{0}+{1}+{2}+{3}".format('_' * MAX_CODE_LENGTH,
                                         '_' * MAX_NAME_LENGTH,
                                         '_' * MAX_NUM_ROWS_LENGTH,
                                         '_' * MAX_SEAT_MARKING_LENGTH)

    return "{}{}".format(header, lines)


def format_hall(hall):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}").format(MAX_CODE_LENGTH,
                                MAX_NAME_LENGTH,
                                MAX_NUM_ROWS_LENGTH,
                                MAX_SEAT_MARKING_LENGTH).format(hall["code"],
                                                                       hall["name"],
                                                                       hall["num_rows"],
                                                                       hall["seat_marking"])


def format_halls(halls_list):
    result = ""
    for hall in halls_list:
        result += format_hall(hall) + "\n"
    return result


def format_all_halls():
    return format_halls(halls)


def format_hall_rows(hall, screening_term):
    num_rows = int(hall['num_rows'])
    seat_markings = hall['seat_marking'].split(',')
    formatted_rows = []

    for r in range(num_rows):
        formatted_row = "{}{:3} ".format("Red", r+1)
        for s in range(len(seat_markings)):
            seat = f"{r+1}{seat_markings[s]}"
            if ticket.is_seat_occupied(seat, screening_term):
                seat_marking = 'X'
            else:
                seat_marking = seat_markings[s]
            formatted_row = f"{formatted_row} {seat_marking}"

        formatted_rows.append(formatted_row)

    return formatted_rows


def format_rows(rows):
    formatted_rows = ""
    for row in rows:
        formatted_rows = f"{formatted_rows}{row}\n"
    return formatted_rows


def get_hall_by_code(code):
    for hall in halls:
        if code.upper() == hall['code'].upper():
            return hall
    return {}


def hall_code_exists(code):
    for hall in halls:
        if code.upper() == hall['code'].upper():
            return True
    return False


halls = []
load_halls()
print(format_header())
print(format_all_halls())