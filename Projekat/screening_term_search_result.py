import datetime
from os.path import exists


#ogranicenja
MIN_CODE_LENGTH = 1
MAX_CODE_LENGTH = 28
MIN_HALL_LENGTH = 7
MAX_HALL_LENGTH = 20
MIN_START_TIME_LENGTH = 1
MAX_START_TIME_LENGTH = 27
MIN_END_TIME_LENGTH = 1
MAX_END_TIME_LENGTH = 27
MIN_MOVIE_LENGTH = 1
MAX_MOVIE_LENGTH = 17
MIN_DATE_LENGTH = 1
MAX_DATE_LENGTH = 30


#ispis u zaglavlju tabele
HEADER_CODE = "Sifra termina projekcije"
HEADER_HALL = "Sifra sale"
HEADER_START_TIME = "Vreme pocetka projekcije"
HEADER_END_TIME = "Vreme zavrsetka projekcije"
HEADER_MOVIE = "Naziv filma"
HEADER_DATE = "Datum odrzavanja projekcije"

def screening_term_search_result2str(result):
    return '|'.join([result['code'], result['movie'], result['hall'], result['date'], result['start_time'],
                     result['end_time']])


def str2screening_term_search_result(line):
    if line[-1] == '\n':
        line = line[:-1]
        screening_term_code, movie, hall, date, start_time, end_time = line.split('|')
        screening_term_search_result = {
            'code': screening_term_code,
            'movie': movie,
            'hall': hall,
            'date': date,
            'start_time': start_time,
            'end_time': end_time,
        }
        return screening_term_search_result


def check_file():
    if not exists('data/screening_term_search_result.txt'):
        open('data/screening_term_search_result.txt', 'w').close()


def load_screening_term_search_results():
    check_file()
    file = open("data/screening_term_search_result.txt", 'r')
    for line in file.readlines():
        if len(line) > 1:
            screening_term_search_result = str2screening_term_search_result(line)
            screening_term_search_results.append(screening_term_search_result)
    file.close()


def save_screening_term_search_results():
    file = open("data/screening_term_search_result.txt", 'w')
    for screening_term_search_result in screening_term_search_results:
        line = screening_term_search_result2str(screening_term_search_result)
        file.write(line)
        file.write('\n')
    file.close()


def format_header():
    header = "{0}|{1}|{2}|{3}|{4}|{5}\n".format(HEADER_CODE.ljust(MAX_CODE_LENGTH),
                                            HEADER_MOVIE.ljust(MAX_MOVIE_LENGTH),
                                            HEADER_HALL.ljust(MAX_HALL_LENGTH),
                                            HEADER_DATE.ljust(MAX_DATE_LENGTH),
                                            HEADER_START_TIME.ljust(MAX_START_TIME_LENGTH),
                                            HEADER_END_TIME.ljust(MAX_END_TIME_LENGTH))
    lines = "{0}+{1}+{2}+{3}+{4}+{5}".format('_' * MAX_CODE_LENGTH,
                                         '_' * MAX_MOVIE_LENGTH,
                                         '_' * MAX_HALL_LENGTH,
                                         '_' * MAX_DATE_LENGTH,
                                         '_' * MAX_START_TIME_LENGTH,
                                         '_' * MAX_END_TIME_LENGTH)

    return "{}{}".format(header, lines)


def format_screening_term_search_result(screening_term_search_result):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:{}}}|"
            "{{5:{}}}").format(MAX_CODE_LENGTH,
                                MAX_MOVIE_LENGTH,
                                MAX_HALL_LENGTH,
                                MAX_DATE_LENGTH,
                                MAX_START_TIME_LENGTH,
                                MAX_END_TIME_LENGTH).format(screening_term_search_result["code"],
                                                         screening_term_search_result["movie"],
                                                         screening_term_search_result["hall"],
                                                         screening_term_search_result["date"],
                                                         screening_term_search_result["start_time"],
                                                         screening_term_search_result["end_time"])


def format_screening_term_search_results(screening_term_search_result_list):
    result = ""
    for screening_term_search_result in screening_term_search_result_list:
        result += format_screening_term_search_result(screening_term_search_result) + '\n'
    return result


def format_all_screening_term_search_results():
    return format_screening_term_search_results(screening_term_search_results)


def add_screening_term_search_results(results):
    screening_term_search_results.clear()
    for result in results:
        screening_term_search_results.append(result)
    # save_screening_term_search_results()


screening_term_search_results = []
# load_screening_term_search_results()