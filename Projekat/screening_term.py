from os.path import exists
from Projekat import screening

#ogranicenja
MIN_CODE_LENGTH = 1
MAX_CODE_LENGTH = 30
MIN_DATE_LENGTH = 7
MAX_DATE_LENGTH = 27


#ispis u zaglavlju tabele
HEADER_CODE = "Sifra bioskopske projekcije"
HEADER_DATE = "Datum odrzavanja"

def screening_term2str(screening_term):
    return '|'.join([screening_term['code'], screening_term['date']])

def str2screening_term(line):
    if line[-1] == '\n':
        line = line[:-1]
        code, date = line.split('|')
        screening_term = {
            'code': code,
            'date': date,
        }
        return screening_term


def check_file():
    if not exists('data/screening_terms.txt'):
        open('data/screening_terms.txt', 'w').close()


def load_screening_terms():
    check_file()
    screening_terms_file = open('data/screening_terms.txt', 'r')
    for line in screening_terms_file.readlines():
        if len(line) > 1:
            screening_term = str2screening_term(line)
            screening_terms.append(screening_term)
    screening_terms_file.close()


def save_screening_terms():
    screening_terms_file = open("data/screening_terms.txt", 'w')
    for screening_term in screening_terms:
        line = screening_term2str(screening_term)
        screening_terms_file.write(line)
        screening_terms_file.write('\n')

    screening_terms_file.close()


def format_header():
    header = "{0}|{1}\n".format(HEADER_CODE.ljust(MAX_CODE_LENGTH),
                                      HEADER_DATE.ljust(MAX_DATE_LENGTH))
    lines = "{0}+{1}".format('_' * MAX_CODE_LENGTH,
                                    '_' * MAX_DATE_LENGTH)

    return "{}{}".format(header, lines)


def format_screening_term(screening_term):
    return ("{{0:{}}}|"
            "{{1:{}}}").format(MAX_CODE_LENGTH,
                                      MAX_DATE_LENGTH).format(screening_term["code"],
                                                                     screening_term["date"])


def format_screening_terms(screening_terms_list):
    result = ""
    for screening_term in screening_terms_list:
        result += format_screening_term(screening_term) + '\n'
    return result


def format_all_screening_terms():
    return format_screening_terms(screening_terms)


def get_screening_terms_by_criteria(criteria, search_term):
    filtered_terms = []
    if criteria == 'movie':
        for screening_term in screening_terms:
            code = screening_term['code'][:4]
            screenings = screening.get_screenings_by_movie_title_and_code(search_term, code)
            if len(screenings) > 0:
                filtered_terms.append(screening_term)
    elif criteria == 'code':
        for screening_term in screening_terms:
            if screening_term['code'][:4] == search_term:
                filtered_terms.append(screening_term)
    elif criteria == 'hall':
        for screening_term in screening_terms:
            code = screening_term['code'][:4]
            screenings = screening.get_screenings_by_hall_name_and_code(search_term, code)
            if len(screenings) > 0:
                filtered_terms.append(screening_term)
    elif criteria == 'date':
        for screening_term in screening_terms:
            if search_term == screening_term['date']:
                filtered_terms.append(screening_term)
    elif criteria == 'start_time':
        for screening_term in screening_terms:
            code = screening_term['code'][:4]
            screenings = screening.get_screenings_by_start_time_and_code(search_term, code)
            if len(screenings) > 0:
                filtered_terms.append(screening_term)
    elif criteria == 'end_time':
        for screening_term in screening_terms:
            code = screening_term['code'][:4]
            screenings = screening.get_screenings_by_end_time_and_code(search_term, code)
            if len(screenings) > 0:
                filtered_terms.append(screening_term)

    return filtered_terms


def generate_screening_terms(terms):
    for term in terms:
        if not screening_terms.__contains__(term):
            screening_terms.append(term)
    save_screening_terms()


def code_exists_in_screening_terms(code):
    for screening_term in screening_terms:
        if screening_term['code'].upper() == code.upper():
            return True
    return False


def get_screening_term_by_code(screening_term_code):
    for term in screening_terms:
        if term['code'] == screening_term_code:
            return term
    return {}


screening_terms = []
load_screening_terms()
print(format_header())
print(format_all_screening_terms())