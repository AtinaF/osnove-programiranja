import datetime
from os.path import exists


#ogranicenja
MIN_CODE_LENGTH = 1
MAX_CODE_LENGTH = 28
MIN_SEAT_LENGTH = 7
MAX_SEAT_LENGTH = 20
MIN_START_TIME_LENGTH = 1
MAX_START_TIME_LENGTH = 27
MIN_END_TIME_LENGTH = 1
MAX_END_TIME_LENGTH = 27
MIN_MOVIE_LENGTH = 1
MAX_MOVIE_LENGTH = 17
MIN_DATE_LENGTH = 1
MAX_DATE_LENGTH = 30
MIN_NAME_AND_SURNAME_LENGTH = 1
MAX_NAME_AND_SURNAME_LENGTH = 25
MIN_RESERVATION_STATUS = 1
MAX_RESERVATION_STATUS = 15

#ispis u zaglavlju tabele
HEADER_CODE = "Sifra termina projekcije"
HEADER_SEAT = "Oznaka sedista"
HEADER_START_TIME = "Vreme pocetka projekcije"
HEADER_END_TIME = "Vreme zavrsetka projekcije"
HEADER_MOVIE = "Naziv filma"
HEADER_DATE = "Datum rezervacije/kupovine"
HEADER_NAME_AND_SURNAME = "Ime i prezime korisnika"
HEADER_RESERVATION_STATUS = "Stanje karte"


def reserved_ticket_info2str(info):
    return '|'.join([info['screening_term_code'], info['movie'], info['seat'],
                     info['reservation_date'], info['start_time'],
                     info['end_time'], info['user_name_and_surname'],
                     info['reservation_status']])


def str2reserved_ticket_info(line):
    if line[-1] == '\n':
        line = line[:-1]
        screening_term_code, movie, seat, date, start_time, end_time, user_name_and_surname, reservation_status = line.split('|')
        reserved_ticket_info = {
            'screening_term_code': screening_term_code,
            'movie': movie,
            'seat': seat,
            'reservation_date': date,
            'start_time': start_time,
            'end_time': end_time,
            'user_name_and_surname': user_name_and_surname,
            'reservation_status': reservation_status
        }
        return reserved_ticket_info


def check_file():
    if not exists('data/reserved_tickets_info.txt'):
        open('data/reserved_tickets_info.txt', 'w').close()


def load_reserved_ticket_info():
    check_file()
    file = open("data/reserved_tickets_info.txt", 'r')
    for line in file.readlines():
        if len(line) > 1:
            reserved_ticket_info = str2reserved_ticket_info(line)
            reserved_tickets_info.append(reserved_ticket_info)
    file.close()


def save_reserved_ticket_info():
    file = open("data/reserved_tickets_info.txt", 'w')
    for reserved_ticket_info in reserved_tickets_info:
        line = reserved_ticket_info2str(reserved_ticket_info)
        file.write(line)
        file.write('\n')
    file.close()


def format_header():
    header = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}\n".format(HEADER_CODE.ljust(MAX_CODE_LENGTH),
                                                HEADER_MOVIE.ljust(MAX_MOVIE_LENGTH),
                                                HEADER_SEAT.ljust(MAX_SEAT_LENGTH),
                                                HEADER_DATE.ljust(MAX_DATE_LENGTH),
                                                HEADER_START_TIME.ljust(MAX_START_TIME_LENGTH),
                                                HEADER_END_TIME.ljust(MAX_END_TIME_LENGTH),
                                                HEADER_NAME_AND_SURNAME.ljust(MAX_NAME_AND_SURNAME_LENGTH),
                                                HEADER_RESERVATION_STATUS.ljust(MAX_RESERVATION_STATUS))

    lines = "{0}+{1}+{2}+{3}+{4}+{5}+{6}+{7}".format('_' * MAX_CODE_LENGTH,
                                         '_' * MAX_MOVIE_LENGTH,
                                         '_' * MAX_SEAT_LENGTH,
                                         '_' * MAX_DATE_LENGTH,
                                         '_' * MAX_START_TIME_LENGTH,
                                         '_' * MAX_END_TIME_LENGTH,
                                         '_' * MAX_NAME_AND_SURNAME_LENGTH,
                                         '_' * MAX_RESERVATION_STATUS)

    return "{}{}".format(header, lines)


def format_reserved_ticket_info(screening_term_search_result):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:{}}}|"
            "{{5:{}}}|"
            "{{6:{}}}|"
            "{{7:{}}}").format(MAX_CODE_LENGTH,
                               MAX_MOVIE_LENGTH,
                               MAX_SEAT_LENGTH,
                               MAX_DATE_LENGTH,
                               MAX_START_TIME_LENGTH,
                               MAX_END_TIME_LENGTH,
                               MAX_NAME_AND_SURNAME_LENGTH,
                               MAX_RESERVATION_STATUS).format(screening_term_search_result["screening_term_code"],
                                                         screening_term_search_result["movie"],
                                                         screening_term_search_result["seat"],
                                                         screening_term_search_result["reservation_date"],
                                                         screening_term_search_result["start_time"],
                                                         screening_term_search_result["end_time"],
                                                         screening_term_search_result["user_name_and_surname"],
                                                         screening_term_search_result["reservation_status"])


def format_reserved_tickets_info(reserved_ticket_info_list):
    result = ""
    for reserved_ticket_info in reserved_ticket_info_list:
        result += format_reserved_ticket_info(reserved_ticket_info) + '\n'
    return result


def format_all_reserved_ticket_info():
    return format_reserved_tickets_info(reserved_tickets_info)


def add_reserved_ticket_info(results):
    reserved_tickets_info.clear()
    for result in results:
        reserved_tickets_info.append(result)


reserved_tickets_info = []