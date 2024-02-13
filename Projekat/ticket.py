#ogranicenja
import datetime
from os.path import exists
from Projekat import screening as screening_module, screening_term as screening_term_module, users


MIN_USER_LENGTH = 1
MAX_USER_LENGTH = 20
MIN_SCREENING_TERM_CODE_LENGTH = 1
MAX_SCREENING_TERM_CODE_LENGTH = 40
MIN_SEAT_LENGTH = 1
MAX_SEAT_LENGTH = 15
MIN_DATE_LENGTH = 1
MAX_DATE_LENGTH = 15
MIN_RESERVED_LENGTH = 1
MAX_RESERVED_LENGTH = 30


#ispis u zaglavlju tabele
HEADER_USER = "Korisnicko ime"
HEADER_SCREENING_TERM_CODE = "Termin bioskopske projekcije"
HEADER_SEAT = "Oznaka sedista"
HEADER_DATE = "Datum prodaje"
HEADER_RESERVED = "Rezervisana/kupljena karta"


def ticket2str(ticket):
    return '|'.join([ticket['username'], ticket['screening_term_code'], ticket['seat'],
                     ticket['date'], ticket['reserved']])


def str2ticket(line):
    if line[-1] == '\n':
        line = line[:-1]
        username, screening_term_code, seat, date, reserved = line.split('|')
        ticket = {
            'username': username,
            'screening_term_code': screening_term_code,
            'seat': seat,
            'date': date,
            'reserved': reserved
        }
        return ticket


def check_file():
    if not exists('data/tickets.txt'):
        open('data/tickets.txt', 'w').close()


def load_tickets():
    check_file()
    tickets_file = open("data/tickets.txt", 'r')

    for line in tickets_file.readlines():
        if len(line) > 1:
            ticket = str2ticket(line)
            tickets.append(ticket)
    tickets_file.close()


def save_tickets():
    tickets_file = open("data/tickets.txt", 'w')
    for ticket in tickets:
        line = ticket2str(ticket)
        tickets_file.write(line)
        tickets_file.write('\n')

    tickets_file.close()


def format_header():
    header = "{0}|{1}|{2}|{3}|{4}\n".format(HEADER_USER.ljust(MAX_USER_LENGTH),
                                            HEADER_SCREENING_TERM_CODE.ljust(MAX_SCREENING_TERM_CODE_LENGTH),
                                            HEADER_SEAT.ljust(MAX_SEAT_LENGTH),
                                            HEADER_DATE.ljust(MAX_DATE_LENGTH),
                                            HEADER_RESERVED.ljust(MAX_RESERVED_LENGTH))
    lines = "{0}+{1}+{2}+{3}+{4}".format('_' * MAX_USER_LENGTH,
                                         '_' * MAX_SCREENING_TERM_CODE_LENGTH,
                                         '_' * MAX_SEAT_LENGTH,
                                         '_' * MAX_DATE_LENGTH,
                                         '_' * MAX_RESERVED_LENGTH)

    return "{}{}".format(header, lines)


def format_ticket(ticket):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:>{}}}").format(MAX_USER_LENGTH,
                                MAX_SCREENING_TERM_CODE_LENGTH,
                                MAX_SEAT_LENGTH,
                                MAX_DATE_LENGTH,
                                MAX_RESERVED_LENGTH).format(ticket["username"],
                                                           ticket["screening_term_code"],
                                                           ticket["seat"],
                                                           ticket["date"],
                                                           ticket["reserved"])


def format_tickets(tickets_list):
    result = ""
    for ticket in tickets_list:
        result += format_ticket(ticket) + '\n'
    return result


def format_all_users():
    return format_tickets(tickets)


def reserve_ticket(screening_term_code, seat, username):
    ticket = {
        'username': username,
        'seat': seat,
        'screening_term_code': screening_term_code,
        'date': datetime.date.today().strftime('%d.%m.%Y'),
        'reserved': 'reserved'
    }

    if not tickets.__contains__(ticket):
        tickets.append(ticket)
        save_tickets()


def get_reserved_tickets_by_username(username):
    reserved_tickets = []
    for ticket in tickets:
        if ticket['username'] == username and ticket['reserved'] == 'reserved':
            reserved_tickets.append(ticket)
    return reserved_tickets


def cancel_reservation(screening_term_code, seat, username):
    reservation_to_be_cancelled = {}
    for ticket in tickets:
        if (ticket['reserved'] == 'reserved'
                and ticket['username'] == username
                and ticket['screening_term_code'] == screening_term_code
                and ticket['seat'] == seat):
            reservation_to_be_cancelled = ticket
            break
    if reservation_to_be_cancelled != {}:
        tickets.remove(reservation_to_be_cancelled)
        return True
    else:
        return False


def cancel_ticket(screening_term_code, seat):
    ticket_to_cancel = {}
    for ticket in tickets:
        if (ticket['screening_term_code'] == screening_term_code and
                ticket['seat'] == seat):
            ticket_to_cancel = ticket
            break
    if ticket_to_cancel != {}:
        tickets.remove(ticket_to_cancel)
        save_tickets()
        return True
    else:
        return False


def get_ticket_by_screening_term_code(screening_term_code):
    return [ticket for ticket in tickets if ticket['screening_term_code'] == screening_term_code]


def is_seat_occupied(seat, screening_term_code):
    movie_tickets = get_ticket_by_screening_term_code(screening_term_code)

    if len(movie_tickets) == 0:
        return False

    for ticket in movie_tickets:
        if ticket['seat'] == seat:
            return True
    return False


def get_all_reserved_tickets():
    return [ticket for ticket in tickets if ticket['reserved'] == 'reserved']


def get_all_tickets():
    return [ticket for ticket in tickets]


def get_name_from_ticket(ticket):
    user = users.get_user_by_username(ticket['username'])
    if user is None:
        name = ticket['username'].split(' ')[0]
    else:
        name = user['name']
    return name


def get_surname_from_ticket(ticket):
    user = users.get_user_by_username(ticket['username'])
    if user is None:
        surname = ticket['username'].split(' ')[1]
    else:
        surname = user['surname']
    return surname


def set_name_and_surname_of_ticket(ticket, username, new_name, new_surname):
    user = users.get_user_by_username(username)
    if user is None:
        ticket['username'] = f"{new_name} {new_surname}"
    else:
        ticket['username'] = username
        user['name'] = new_name
        user['surname'] = new_surname
        users.save_users()


def get_tickets_by_criteria(criteria, search_term):
    results = []
    if criteria == 'screening_term_code':
        for ticket in tickets:
            if ticket['screening_term_code'].upper() == search_term.upper():
                results.append(ticket)
    elif criteria == 'name':
        for ticket in tickets:
            name = get_name_from_ticket(ticket)
            if name.upper() == search_term.upper():
                results.append(ticket)
    elif criteria == 'surname':
        for ticket in tickets:
            surname = get_surname_from_ticket(ticket)
            if surname.upper() == search_term.upper():
                results.append(ticket)
    elif criteria == 'date':
        for ticket in tickets:
            if ticket['date'] == search_term:
                results.append(ticket)
    elif criteria == 'start_time':
        for ticket in tickets:
            screening_term_code = ticket['screening_term_code']
            screening = screening_module.get_screening_by_code(screening_term_code[:4])
            if screening['start_time'] == search_term:
                results.append(ticket)
    elif criteria == 'end_time':
        for ticket in tickets:
            screening_term_code = ticket['screening_term_code']
            screening = screening_module.get_screening_by_code(screening_term_code[:4])
            if screening['end_time'] == search_term:
                results.append(ticket)
    elif criteria == 'reserved':
        for ticket in tickets:
            if ticket['reserved'] == search_term:
                results.append(ticket)
    return results


def sell_ticket(screening_term_code, seat, username):
    ticket = {
        'username': username,
        'seat': seat,
        'screening_term_code': screening_term_code,
        'date': datetime.date.today().strftime('%d.%m.%Y'),
        'reserved': 'sold'
    }

    if not tickets.__contains__(ticket):
        tickets.append(ticket)
        save_tickets()


def sell_reserved_ticket(screening_term_code, seat):
    for ticket in tickets:
        if (ticket['screening_term_code'].upper() == screening_term_code.upper()
                and ticket['seat'].upper() == seat.upper()
                and ticket['reserved'] == 'reserved'):
            ticket['reserved'] = 'sold'
            break


def find_ticket_by(screening_term_code, name, surname, seat):
    for ticket in tickets:
        user_name = get_name_from_ticket(ticket)
        user_surname = get_surname_from_ticket(ticket)
        if (ticket['screening_term_code'] == screening_term_code
                and ticket['seat'] == seat
                and user_name == name
                and user_surname == surname):
            return ticket
    return {}


def remove_ticket(ticket_to_modify):
    tickets.remove(ticket_to_modify)


def modify_ticket(reserved, date, username, new_code, new_name, new_surname, new_seat):
    modified_ticket = {
        'reserved': reserved,
        'date': date,
        'screening_term_code': new_code,
        'seat': new_seat
    }
    set_name_and_surname_of_ticket(modified_ticket, username, new_name, new_surname)
    tickets.append(modified_ticket)
    save_tickets()


def get_sold_tickets_by_sale_date(sale_date):
    return [ticket for ticket in tickets
            if ticket['date'] == sale_date
            and ticket['reserved'] == 'sold']


def get_sold_tickets_by_screening_term_date(screening_term_date):
    results = []
    for ticket in tickets:
        if ticket['reserved'] == 'sold':
            screening_term_code = ticket['screening_term_code']
            term = screening_term_module.get_screening_term_by_code(screening_term_code)
            if term['date'] == screening_term_date:
                results.append(ticket)
    return results


def add_tickets(new_tickets):
    tickets.extend(new_tickets)
    save_tickets()


tickets = []
load_tickets()
print(format_header())
print(format_all_users())