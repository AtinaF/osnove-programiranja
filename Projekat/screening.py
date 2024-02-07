from os.path import exists


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




screening1 = {
    'code': "1123",
    'hall': "hall12",
    'start_time': "01.01.2023",
    'end_time': "02.02.2023",
    'days': ["ponedeljak", "utorak", "sreda", "nedelja"],
    # days=[ponedeljak, utorak, sreda, cetvrtak, petak, subota, nedelja]
    'movie': "movie aaa",
    'price': "424"
}
screening2 = {
    'code': "1553",
    'hall': "hall1fd2",
    'start_time': "11.11.2023",
    'end_time': "22.12.2023",
    'days': ["ponedeljak", "utorak", "sreda", "nedelja"],
    # days=[ponedeljak, utorak, sreda, cetvrtak, petak, subota, nedelja]
    'movie': "movie adfaa",
    'price': "23.00"
}

# screenings = [screening1, screening2]
# save_screenings()
screenings=[]
load_screenings()
save_screenings()
print(format_header())
print(format_all_screenings())
