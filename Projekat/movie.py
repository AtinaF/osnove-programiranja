from os.path import exists


#ogranicenja
MIN_TITLE_LENGTH = 1
MAX_TITLE_LENGTH = 20
MIN_GENRE_LENGTH = 1
MAX_GENRE_LENGTH = 25
MIN_DURATION_LENGTH = 1
MAX_DURATION_LENGTH = 15
MIN_DIRECTOR_LENGTH = 1
MAX_DIRECTOR_LENGTH = 15
MIN_MAIN_ROLES_LENGTH = 1
MAX_MAIN_ROLES_LENGTH = 50
MIN_COUNTRY_LENGTH = 1
MAX_COUNTRY_LENGTH = 15
MIN_YEAR_LENGTH = 1
MAX_YEAR_LENGTH = 6
MIN_DESCRIPTION_LENGTH = 1
MAX_DESCRIPTION_LENGTH = 50

#ispis u zaglavlju tabele
HEADER_TITLE = "Naslov"
HEADER_GENRE = "Zanr"
HEADER_DURATION = "Trajanje"
HEADER_DIRECTOR = "Reziser"
HEADER_MAIN_ROLES = "Uloge"
HEADER_COUNTRY = "Zemlja"
HEADER_YEAR = "Godina"
HEADER_DESCRIPTION = "Opis"

def movie2str(movie):
    return "|".join([movie["title"], movie["genre"], movie["duration"],movie["director"], movie["main_roles"], movie["country"], movie["year"], movie["description"]])


def str2movie(line):
    title, genre, duration, director, main_roles, country, year, description = line.split('|')
    movie = {
        "title":title,
        "genre":genre,
        "duration":duration,
        "director":director,
        "main_roles":main_roles,
        "country":country,
        "year":year,
        "description":description
    }
    return movie


def check_file():
    if not exists('data/movies.txt'):
        open('data/movies.txt', 'w').close()


def load_movies():
    check_file()
    movies_file = open("data/movies.txt", 'r')
    for line in movies_file.readlines():
        if len(line) > 1:
            movie = str2movie(line)
            movies.append(movie)
    movies_file.close()


def save_movies():
    users_file = open("data/movies.txt", 'w')
    for movie in movies:
        line = movie2str(movie)
        users_file.write(line)
        users_file.write('\n')

    users_file.close()


def format_header():
    header = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}\n".format(HEADER_TITLE.ljust(MAX_TITLE_LENGTH),
                                            HEADER_GENRE.ljust(MAX_GENRE_LENGTH),
                                            HEADER_DURATION.ljust(MAX_DURATION_LENGTH),
                                            HEADER_DIRECTOR.ljust(MAX_DIRECTOR_LENGTH),
                                            HEADER_MAIN_ROLES.ljust(MAX_MAIN_ROLES_LENGTH),
                                            HEADER_COUNTRY.ljust(MAX_COUNTRY_LENGTH),
                                            HEADER_YEAR.ljust(MAX_YEAR_LENGTH),
                                            HEADER_DESCRIPTION.ljust(MAX_DESCRIPTION_LENGTH))

    lines = "{0}+{1}+{2}+{3}+{4}+{5}+{6}+{7}".format('_' * MAX_TITLE_LENGTH,
                                         '_' * MAX_GENRE_LENGTH,
                                         '_' * MAX_DURATION_LENGTH,
                                         '_' * MAX_DIRECTOR_LENGTH,
                                         '_' * MAX_MAIN_ROLES_LENGTH,
                                         '_' * MAX_COUNTRY_LENGTH,
                                         '_' * MAX_YEAR_LENGTH,
                                         '_' * MAX_DESCRIPTION_LENGTH)

    return "{}{}".format(header, lines)


def format_movie(movie):
    return ("{{0:{}}}|"
            "{{1:{}}}|"
            "{{2:{}}}|"
            "{{3:{}}}|"
            "{{4:>{}}}|"
            "{{5:>{}}}|"
            "{{6:>{}}}|"
            "{{7:>{}}}").format(MAX_TITLE_LENGTH,
                                MAX_GENRE_LENGTH,
                                MAX_DURATION_LENGTH,
                                MAX_DIRECTOR_LENGTH,
                                MAX_MAIN_ROLES_LENGTH,
                                MAX_COUNTRY_LENGTH,
                                MAX_YEAR_LENGTH,
                                MAX_DESCRIPTION_LENGTH).format(movie["title"],
                                                               movie["genre"],
                                                               movie["duration"],
                                                               movie["director"],
                                                               movie["main_roles"],
                                                               movie["country"],
                                                               movie["year"],
                                                               movie["description"])


def format_movies(movie_list):
    result = ""
    for movie in movie_list:
        result += format_movie(movie)
    return result


def format_all_movies():
    return format_movies(movies)


def filter_movies_by_criterion(criterion, search_term):
    filtered_movies = []
    for movie in movies:
        criterion_lower = criterion.lower()

        if criterion_lower == 'duration':
            # 15-80 minuta
            min_duration, max_duration = map(int, search_term.split('-'))
            movie_duration = int(movie.get(criterion_lower, 0))

            if min_duration <= movie_duration <= max_duration:
                filtered_movies.append(movie)
        else:
            if search_term.lower() in movie.get(criterion_lower, '').lower():
                filtered_movies.append(movie)

    return filtered_movies


def filter_movies_by_criteria(criteria, search_terms):
    filtered_movies = []

    for movie in movies:
        number_of_criteria_satisfied = 0
        for i in range(len(criteria)):
            if criteria[i].lower() == 'duration':
                min_duration, max_duration = map(int, search_terms[i].split('-'))
                movie_duration = int(movie.get(criteria[i].lower(), 0))

                if min_duration <= movie_duration <= max_duration:
                    number_of_criteria_satisfied += 1

            if search_terms[i].lower() in movie.get(criteria[i].lower(), '').lower():
                number_of_criteria_satisfied += 1

        if number_of_criteria_satisfied == len(criteria):
            filtered_movies.append(movie)

    return filtered_movies


def add_movie(movie):
    if get_movie_by_title(movie['title']) == {}:
        movies.append(movie)
        save_movies()


def get_movie_by_title(title):
    for movie in movies:
        if movie['title'].upper() == title.upper():
            return movie
    return {}


def modify_movie(movie_to_modify, modified_movie):
    if movies.__contains__(movie_to_modify):
        movies.remove(movie_to_modify)
        movies.append(modified_movie)
        save_movies()


def delete_movie(movie):
    if movies.__contains__(movie):
        movies.remove(movie)
        save_movies()


movies=[]
load_movies()
formated_movies = format_all_movies()
print(format_header())
print(formated_movies)