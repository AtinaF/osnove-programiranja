from os.path import exists

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
    # sifra bioskopske porjekcijem | datum odrzavanja

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
    if not exists('data/screening_term.txt'):
        open('data/screening_term.txt', 'w').close()


def load_screening_terms():
    check_file()
    screening_terms_file = open("screening_terms.txt", 'r')
    for line in screening_terms_file.readlines():
        if len(line) > 1:
            screening_term = str2screening_term(line)
            screening_terms.append(screening_term)
    screening_terms_file.close()


def save_screening_terms():
    screening_terms_file = open("data/screening_term.txt", 'w')
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


screening_term1 = {
    'code': "1111AA",
    'date': "01.02.2023.",
}
screening_term2 = {
    'code': "1211AB",
    'date': "01.02.2023.",
}

screening_terms=[screening_term1, screening_term2]
save_screening_terms()
print(format_header())
print(format_all_screening_terms())