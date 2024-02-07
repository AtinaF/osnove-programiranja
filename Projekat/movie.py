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


def filter_movies(criterion, search_term):
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


# movie1 = {
#     "title": "Title1",
#     "genre": "Genre1",
#     "duration": "Duration1",
#     "director": "Director1",
#     "main_roles": "Main1, Main2, Main3",
#     "country": "Country1",
#     "year": "2001",
#     "description": "Description1"
# }
#
# movie2 = {
#     "title": "Title2",
#     "genre": "Genre2",
#     "duration": "Duration2",
#     "director": "Director2",
#     "main_roles": "Main4, Main5, Main6",
#     "country": "Country2",
#     "year": "2002",
#     "description": "Description2"
# }
#
# movies = [movie1, movie2]
movies=[]
load_movies()
# save_movies()
formated_movies = format_all_movies()
print(format_header())
print(formated_movies)