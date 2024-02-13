import datetime
import re
from os.path import exists
from Projekat import hall as hall_module


#ogranicenja
MIN_CODE_LENGTH = 1
MAX_CODE_LENGTH = 20
MIN_HALL_LENGTH = 7
MAX_HALL_LENGTH = 20
MIN_START_TIME_LENGTH = 1
MAX_START_TIME_LENGTH = 27
MIN_END_TIME_LENGTH = 1
MAX_END_TIME_LENGTH = 27
MIN_DAYS_LENGTH = 1
MAX_DAYS_LENGTH = 55
MIN_MOVIE_LENGTH = 1
MAX_MOVIE_LENGTH = 17
MIN_PRICE_LENGTH = 1
MAX_PRICE_LENGTH = 15

#ispis u zaglavlju tabele
HEADER_CODE = "Sifra projekcije"
HEADER_HALL = "Sifra sale"
HEADER_START_TIME = "Vreme pocetka projekcije"
HEADER_END_TIME = "Vreme zavrsetka projekcije"
HEADER_DAYS = "Dani odrzavanja projekcije"
HEADER_MOVIE = "Naziv filma"
HEADER_PRICE = "Cena"


def screening2str(screening):
    return '|'.join([screening['code'], screening['hall'], screening['start_time'], screening['end_time'], screening['days'],
                     screening['movie'], screening['price']])


def str2screening(line):
    if line[-1] == '\n':
        line = line[:-1]
        code, hall, start_time, end_time, days, movie, price = line.split('|')
        screening = {
            'code': code,
            'hall': hall,
            'start_time': start_time,
            'end_time': end_time,
            'days': days,  # days=[ponedeljak, utorak, sreda, cetvrtak, petak, subota, nedelja]
            'movie':movie,
            'price':price
        }
        return screening


def check_file():
    if not exists('data/screenings.txt'):
        open('data/screenings.txt', 'w').close()


def load_screenings():
    check_file()
    screening_file = open("data/screenings.txt", 'r')
    for line in screening_file.readlines():
        if len(line) > 1:
            screening = str2screening(line)
            screenings.append(screening)
    screening_file.close()


def save_screenings():
    screenings_file = open("data/screenings.txt", 'w')
    for screening in screenings:
        line = screening2str(screening)
        screenings_file.write(line)
        screenings_file.write('\n')
    screenings_file.close()


def format_header():
    #ispis sa kolonom lozinke
    header = "{0}|{1}|{2}|{3}|{4}|{5}|{6}\n".format(HEADER_CODE.ljust(MAX_CODE_LENGTH),
                                            HEADER_HALL.ljust(MAX_HALL_LENGTH),
                                            HEADER_START_TIME.ljust(MAX_START_TIME_LENGTH),
                                            HEADER_END_TIME.ljust(MAX_END_TIME_LENGTH),
                                            HEADER_DAYS.ljust(MAX_DAYS_LENGTH),
                                            HEADER_MOVIE.ljust(MAX_MOVIE_LENGTH),
                                            HEADER_PRICE.ljust(MAX_PRICE_LENGTH))
    lines = "{0}+{1}+{2}+{3}+{4}+{5}+{6}".format('_' * MAX_CODE_LENGTH,
                                         '_' * MAX_HALL_LENGTH,
                                         '_' * MAX_START_TIME_LENGTH,
                                         '_' * MAX_END_TIME_LENGTH,
                                         '_' * MAX_DAYS_LENGTH,
                                         '_' * MAX_MOVIE_LENGTH,
                                         '_' * MAX_PRICE_LENGTH)

    return "{}{}".format(header, lines)


def format_screening(screening):
    # days_str = ",".join(screening['days'])
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:{}}}|"
            "{{5:{}}}|"
            "{{6:{}}}").format(MAX_CODE_LENGTH,
                                MAX_HALL_LENGTH,
                                MAX_START_TIME_LENGTH,
                                MAX_END_TIME_LENGTH,
                                MAX_DAYS_LENGTH,
                                MAX_MOVIE_LENGTH,
                                MAX_PRICE_LENGTH).format(screening["code"],
                                                         screening["hall"],
                                                         screening["start_time"],
                                                         screening["end_time"],
                                                         screening["days"],
                                                         screening["movie"],
                                                         screening["price"])


def format_screenings(screenings_list):
    result = ""
    for screening in screenings_list:
        result += format_screening(screening) + '\n'
    return result


def format_all_screenings():
    return format_screenings(screenings)


def get_screenings_by_start_time_and_code(start_time, code):
    result = []
    for screening in screenings:
        if screening['start_time'] == start_time and screening['code'] == code:
            result.append(screening)
    return result


def get_screenings_by_end_time_and_code(end_time, code):
    result = []
    for screening in screenings:
        if screening['end_time'] == end_time and screening['code'] == code:
            result.append(screening)
    return result


def get_screenings_by_movie_title_and_code(search_term, code):
    result = []
    for screening in screenings:
        if search_term.upper() in screening['movie'].upper() and screening['code']==code:
            result.append(screening)
    return result

def get_screenings_by_hall_name_and_code(hall, code):
    result = []
    for screening in screenings:
        if hall.upper() in screening['hall'].upper() and screening['code']==code:
            result.append(screening)
    return result


def get_screening_by_code(code):
    for screening in screenings:
        if screening['code'] == code:
            return screening
    return {}


def generate_codes():
    codes = []
    for i in range(26):
        for j in range(26):
            code = chr(65 + i) + chr(65 + j)
            codes.append(code)
    return codes


def generate_movie_dates(num_weeks, days_of_week):
    movie_dates = []
    current_date = datetime.date.today()

    for i in range(num_weeks * 7):
        if current_date.weekday() in days_of_week:
            movie_dates.append(current_date)

        current_date += datetime.timedelta(days=1)

    return movie_dates


def get_screening_terms():
    terms = []
    codes = generate_codes()
    number_of_weeks = 2
    week_days = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

    for screening in screenings:
        days = screening['days'].split(',')
        days_in_week = []

        for day in days:
            days_in_week.append(week_days.index(day.strip()))

        movie_dates = generate_movie_dates(number_of_weeks, days_in_week)

        for i, movie_date in enumerate(movie_dates):
            screening_term = {
                'code': f"{screening['code']}{codes[i]}",
                'date': movie_date.strftime("%d.%m.%Y")
            }
            terms.append(screening_term)

    return terms


def get_hall_by_screening_code(screening_code):
    for screening in screenings:
        if screening['code'] == screening_code:
            return screening['hall']
    return ""


def is_valid_screening_code(code):
    pattern =  re.compile(r'^[0-9]+$')
    return len(code) == 4 and bool(pattern.match(code))


def are_days_valid(days):
    days = days.split(',')
    if (len(days) <= 7):
        return True
    return False


def add_screening(screening):
    if (is_valid_screening_code(screening['code'])
            and hall_module.hall_code_exists(screening['hall'])
            and are_days_valid(screening['days'])):

        if not screenings.__contains__(screening):
            screenings.append(screening)
            save_screenings()


def modify_screening(screening_to_modify, modified_screening):
    if screenings.__contains__(screening_to_modify):
        screenings.remove(screening_to_modify)
        screenings.append(modified_screening)
        save_screenings()


def get_ticket_price(ticket):
    for screening in screenings:
        if screening['movie'] == ticket['title']:
            return float(screening['price'])


screenings=[]
load_screenings()
save_screenings()
print(format_header())
print(format_all_screenings())
