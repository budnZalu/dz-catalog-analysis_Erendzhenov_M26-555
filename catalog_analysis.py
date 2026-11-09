import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1. Переменные, числа и math.
def average_rating(movies):
    """Вернуть средний рейтинг непустого каталога с одним знаком после запятой."""
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Вернуть максимальный, минимальный и средний возраст непустого каталога."""
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    """Представить длительность в минутах в виде часов и оставшихся минут."""
    return f"{minutes // 60}ч {minutes % 60}м"


# Этап 2. Условия и match.
def rating_tier(rating):
    """Определить категорию фильма по рейтингу."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Определить группу фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы.
def print_non_comedy_movies(movies):
    """Вывести названия фильмов, не относящихся к комедиям."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies):
    """Найти первый фильм с рейтингом выше 9.0 или сообщить об отсутствии."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Посчитать фильмы, длительность которых строго больше порога."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4. Строки.
def normalize_title(title):
    """Сделать первую букву каждого слова заглавной и убрать лишние пробелы."""
    words = title.split()
    return " ".join(word[0].upper() + word[1:] for word in words)


def make_slug(title):
    """Преобразовать название в строку со строчными буквами и дефисами."""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Собрать описание фильма с нормализованным названием и списком жанров."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]:.1f}/10, '
        f"{duration}, жанры: {genres}"
    )


# Этап 5. Списки.
def titles_sorted_by_rating(movies):
    """Вернуть названия по убыванию рейтинга, не изменяя исходный каталог."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Вернуть до n пар (название, рейтинг) лучших фильмов."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# Этап 6. Словари.
def count_by_genre(movies):
    """Посчитать фильмы каждого жанра; один фильм может иметь несколько жанров."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Собрать названия фильмов для каждого актера в порядке каталога."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(movie["title"])
    return filmography


def ratings_above_average(movies):
    """Вернуть названия и рейтинги фильмов выше округленного среднего."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


# Этап 7. Множества.
def all_genres(movies):
    """Объединить жанры всех фильмов в одно множество."""
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    """Найти актеров, участвовавших в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Вернуть жанры первого каталога, отсутствующие во втором."""
    return all_genres(movies_a) - all_genres(movies_b)


# Этап 8. Итераторы и генераторы.
def iter_high_rated(movies, min_rating=8.0):
    """Лениво выдавать фильмы с рейтингом не ниже заданного порога."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated_movies(movies):
    """Продемонстрировать обход генератора с форматированием каждого фильма."""
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration_above_seven(movies):
    """Сложить минуты фильмов с рейтингом строго выше 7 без промежуточного списка."""
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


# Этап 9. Итоговый отчет.
def build_report(movies):
    """Напечатать отчет по каталогу и демонстрации циклов и генератора."""
    print("ОТЧЕТ ПО КАТАЛОГУ")
    if not movies:
        print("Каталог пуст.")
        return

    oldest, newest, average_age = catalog_age_stats(movies)
    print(f"Всего фильмов: {len(movies)}")
    print(f"Средний рейтинг: {average_rating(movies):.1f}")
    print(f"Возраст самого старого фильма (лет): {oldest}")
    print(f"Возраст самого нового фильма (лет): {newest}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")
    print(
        "Суммарная длительность фильмов с рейтингом выше 7: "
        f"{total_duration_above_seven(movies)} мин"
    )

    print("\nТоп-3 фильма:")
    movies_by_title = {movie["title"]: movie for movie in movies}
    for title, _rating in top_n_by_rating(movies):
        print(f"  {format_report_line(movies_by_title[title])}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(
        genre_counts.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")
    print("\nВсе жанры каталога: " + ", ".join(sorted(all_genres(movies))))

    print("\nКатегории фильмов по убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        movie = movies_by_title[title]
        print(
            f"  {normalize_title(title)} — {rating_tier(movie['rating'])}, "
            f"{decade_label(movie['year'])}, слаг: {make_slug(title)}"
        )

    print("\nФильмы с рейтингом выше среднего:")
    for title, rating in ratings_above_average(movies).items():
        print(f"  {normalize_title(title)} — {rating:.1f}/10")

    print("\nФильмография актеров:")
    for actor, titles in sorted(actor_filmography(movies).items()):
        film_titles = ", ".join(normalize_title(title) for title in titles)
        print(f"  {actor}: {film_titles}")

    print("\nФильмы без жанра comedy:")
    print_non_comedy_movies(movies)
    print("\nПервый фильм с рейтингом выше 9.0:")
    print_first_masterpiece(movies)
    print("\nФильмы с рейтингом не ниже 8.0:")
    print_high_rated_movies(movies)


if __name__ == "__main__":
    build_report(movies)
