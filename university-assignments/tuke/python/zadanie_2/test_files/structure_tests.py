from auditorium import Auditorium
from cinema import Cinema
from group import FriendGroup
from movie import Movie
from person import Person
from screening import Screening


def test_structure(list_of_attributes, must_have):
    for attribute in must_have:
        if attribute not in list_of_attributes:
            return attribute


def test_movie_structure():
    try:
        movie = Movie("ABC", 100, "action", 18, "2022/12/20")
    except Exception as e:
        print("Cannot check Movie structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "title",
        "length",
        "genre",
        "age_limit",
        "release_date",
        "validate_date",
        "get_time_passed"
    ]

    missing = test_structure(dir(movie), all_attributes)
    if missing:
        raise RuntimeError(
            "Movie structure incorrect, attribute {} missing".format(missing))


def test_auditorium_structure():
    try:
        auditorium = Auditorium(250)
    except Exception as e:
        print("Cannot check Auditorium structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "capacity",
        "screenings",
        "is_available",
        "add_screening"
    ]

    missing = test_structure(dir(auditorium), all_attributes)
    if missing:
        raise RuntimeError(
            "Auditorium structure incorrect, attribute {} missing".format(missing))


def test_cinema_structure():
    try:
        cinema = Cinema([Auditorium(250), Auditorium(100), Auditorium(70)])
    except Exception as e:
        print("Cannot check Cinema structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "auditoriums",
        "screenings",
        "add_movie",
        "get_movies_shown",
        "get_screenings_for_movie"
    ]

    missing = test_structure(dir(cinema), all_attributes)
    if missing:
        raise RuntimeError(
            "Cinema structure incorrect, attribute {} missing".format(missing))


def test_screening_structure():
    try:
        screening = Screening(
            Movie("ABC", 120, "action", 18, "2023/01/31"),
            Auditorium(100),
            (20, 30)
        )
    except Exception as e:
        print("Cannot check Screening structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "movie",
        "auditorium",
        "time",
        "tickets_sold",
        "sell_tickets",
        "get_occupancy",
        "get_end_time"
    ]

    missing = test_structure(dir(screening), all_attributes)
    if missing:
        raise RuntimeError(
            "Screening structure incorrect, attribute {} missing".format(missing))


def test_person_structure():
    try:
        person = Person(["action", "horror", "sci-fi"], 20, 23, 0.8)
    except Exception as e:
        print("Cannot check Person structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "interests",
        "age",
        "bedtime",
        "tolerance",
        "is_interested",
        "is_allowed",
        "can_attend",
        "will_attend"
    ]

    missing = test_structure(dir(person), all_attributes)
    if missing:
        raise RuntimeError(
            "Person structure incorrect, attribute {} missing".format(missing))


def test_friendgroup_structure():
    try:
        p1 = Person(["action", "horror", "sci-fi"], 20, 23, 0.8)
        p2 = Person(["adventure", "fantasy", "western"], 19, 22, 0.9)
        p3 = Person(["comedy", "romance"], 21, 23, 0.5)
        group = FriendGroup([p1, p2, p3])
    except Exception as e:
        print("Cannot check FriendGroup structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "members",
        "order_movies",
        "choose_screening",
        "buy_tickets"
    ]

    missing = test_structure(dir(group), all_attributes)
    if missing:
        raise RuntimeError(
            "FriendGroup structure incorrect, attribute {} missing".format(missing))


if __name__ == '__main__':
    test_movie_structure()

    test_auditorium_structure()

    test_cinema_structure()

    test_screening_structure()

    test_person_structure()

    test_friendgroup_structure()
