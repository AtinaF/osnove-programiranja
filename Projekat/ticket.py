#ogranicenja
from os.path import exists

MIN_USER_LENGTH = 1
MAX_USER_LENGTH = 20
MIN_SCREENING_TERM_LENGTH = 1
MAX_SCREENING_TERM_LENGTH = 40
MIN_SEAT_LENGTH = 1
MAX_SEAT_LENGTH = 15
MIN_SALE_DATE_LENGTH = 1
MAX_SALE_DATE_LENGTH = 15
MIN_RESERVED_LENGTH = 1
MAX_RESERVED_LENGTH = 30


#ispis u zaglavlju tabele
HEADER_USER = "Korisnicko ime"
HEADER_SCREENING_TERM = "Termin bioskopske projekcije"
HEADER_SEAT = "Oznaka sedista"
HEADER_SALE_DATE = "Datum prodaje"
HEADER_RESERVED = "Rezervisana/kupljena karta"


def ticket2str(ticket):
    return '|'.join([ticket['username'], ticket['screening_term'], ticket['seat'],
                     ticket['sale_date'], ticket['reserved']])


def str2ticket(line):
    if line[-1] == '\n':
        line = line[:-1]
        username, screening_term, seat, sale_date, reserved = line.split('|')
        ticket = {
            'username': username,
            'screening_term': screening_term,
            'seat': seat,
            'sale_date': sale_date,
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
                                            HEADER_SCREENING_TERM.ljust(MAX_SCREENING_TERM_LENGTH),
                                            HEADER_SEAT.ljust(MAX_SEAT_LENGTH),
                                            HEADER_SALE_DATE.ljust(MAX_SALE_DATE_LENGTH),
                                            HEADER_RESERVED.ljust(MAX_RESERVED_LENGTH))
    lines = "{0}+{1}+{2}+{3}+{4}".format('_' * MAX_USER_LENGTH,
                                         '_' * MAX_SCREENING_TERM_LENGTH,
                                         '_' * MAX_SEAT_LENGTH,
                                         '_' * MAX_SALE_DATE_LENGTH,
                                         '_' * MAX_RESERVED_LENGTH)

    return "{}{}".format(header, lines)


def format_ticket(ticket):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:>{}}}").format(MAX_USER_LENGTH,
                                MAX_SCREENING_TERM_LENGTH,
                                MAX_SEAT_LENGTH,
                                MAX_SALE_DATE_LENGTH,
                                MAX_RESERVED_LENGTH).format(ticket["username"],
                                                           ticket["screening_term"],
                                                           ticket["seat"],
                                                           ticket["sale_date"],
                                                           ticket["reserved"])


def format_tickets(tickets_list):
    result = ""
    for ticket in tickets_list:
        result += format_ticket(ticket) + '\n'
    return result


def format_all_users():
    return format_tickets(tickets)




# ticket1 = {
#             'username': "username",
#             'screening_term': "screening_term",
#             'seat': "seat",
#             'sale_date': "sale_date",
#             'reserved': "reserved"
#         }
# ticket2 = {
#             'username': "username",
#             'screening_term': "screening_term",
#             'seat': "seat",
#             'sale_date': "sale_date",
#             'reserved': "reserved"
#         }
# tickets = [ticket1, ticket2]
tickets = []
load_tickets()
# save_tickets()
print(format_header())
print(format_all_users())