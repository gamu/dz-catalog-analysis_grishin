import math

### Data
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
###

## Задача 1
def average_rating(movies):
    if not movies:
        return 0.0
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    average_age = math.ceil(sum(ages) / len(ages))
    return (max(ages), min(ages), average_age)

def duration_in_hours(minutes):
    hours = minutes // 60
    rest_minutes = minutes % 60
    return f"{hours}ч {rest_minutes}м"

## Задача 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

## Задача 3
def print_non_comedies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print("Первый шедевр:", movie["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

## Задача 4
def normalize_title(title):
    words = title.split()
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:])
    return " ".join(new_words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {duration}, жанры: {genres}'


## Задача 5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

## Задача 6
def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            titles = filmography.get(actor, [])
            titles.append(movie["title"])
            filmography[actor] = titles
    return filmography

def movies_above_average(movies):
    average = average_rating(movies)
    return {movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average}

## Задача 7
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)

## Задача 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration_high_rated(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


## Финальная задача
def build_report(movies):
    _, _, average_age = catalog_age_stats(movies)
    movies_by_title = {movie["title"]: movie for movie in movies}
    genre_counts = sorted(count_by_genre(movies).items(), key=lambda item: (-item[1], item[0]))
    genres_line = ", ".join(sorted(all_genres(movies)))

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print()
    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies, 3):
        print(f"  {format_report_line(movies_by_title[title])}")
    print()
    print("Фильмов по жанрам:")
    for genre, count in genre_counts:
        print(f"  {genre} — {count}")
    print()
    print(f"Все жанры каталога: {genres_line}")


if __name__ == "__main__":
    build_report(movies)

    print()
    print("Фильмы не из жанра comedy:")
    print_non_comedies(movies)

    print()
    find_first_masterpiece(movies)
    find_first_masterpiece([movie for movie in movies if movie["rating"] <= 9.0])

    print()
    print("Фильмы с рейтингом от 8.0:")
    print_high_rated(movies)
    print(f"Суммарная длительность фильмов с рейтингом выше 7: {total_duration_high_rated(movies)} мин")

