from auditorium import Auditorium
from movie import Movie
from screening import Screening
from Zadanie2.structure_tests import *


def test_is_available():
    print("Checking Auditorium.is_available()")
    has_error = False

    auditorium = Auditorium(100)
    auditorium.screenings = [
        Screening(Movie("ABC", 120, "action", 18, "2023/01/31"), auditorium, (15, 30)),
        Screening(Movie("DEF", 90, "action", 18, "2023/01/31"), auditorium, (18, 00)),
        Screening(Movie("ABC", 120, "action", 18, "2023/01/31"), auditorium, (21, 00)),
    ]

    # testing possible screenings
    test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), auditorium, (19, 35))
    st_res = auditorium.is_available(test_screening)
    if st_res is not True:
        print("\tAuditorium.is_available() returned wrong value, expected True, got {}".format(st_res))
        print("\tPrevious screening finishes at 19:30, new one starts at 19:35")
        print("\tNext screening starts at 21:00, new one finishes at 20:55")
        print()
        has_error = True

    test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), auditorium, (23, 5))
    st_res = auditorium.is_available(test_screening)
    if st_res is not True:
        print("\tAuditorium.is_available() returned wrong value, expected True, got {}".format(st_res))
        print("\tPrevious screening finishes at 23:00, new one starts at 23:05")
        print("\tNo next screening defined")
        print()
        has_error = True

    test_screening = Screening(Movie("JKL", 20, "comedy", 12, "2023/03/31"), auditorium, (17, 35))
    st_res = auditorium.is_available(test_screening)
    if st_res is not True:
        print("\tAuditorium.is_available() returned wrong value, expected True, got {}".format(st_res))
        print("\tPrevious screening finishes at 17:30, new one starts at 17:35")
        print("\tNext screening starts at 18:00, new one finishes at 17:55")
        print()
        has_error = True

    # testing impossible screenings
    test_screening = Screening(Movie("GHI", 120, "comedy", 16, "2023/03/31"), auditorium, (19, 35))
    st_res = auditorium.is_available(test_screening)
    if st_res is not False:
        print("\tAuditorium.is_available() returned wrong value, expected False, got {}".format(st_res))
        print("\tPrevious screening finishes at 19:30, new one starts at 19:35")
        print("\tNext screening starts at 21:00, new one finishes at 21:35")
        print()
        has_error = True

    test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), auditorium, (22, 30))
    st_res = auditorium.is_available(test_screening)
    if st_res is not False:
        print("\tAuditorium.is_available() returned wrong value, expected False, got {}".format(st_res))
        print("\tPrevious screening finishes at 23:00, new one starts at 22:30")
        print()
        has_error = True

    test_screening = Screening(Movie("JKL", 70, "comedy", 12, "2023/03/31"), auditorium, (17, 20))
    st_res = auditorium.is_available(test_screening)
    if st_res is not False:
        print("\tAuditorium.is_available() returned wrong value, expected False, got {}".format(st_res))
        print("\tPrevious screening finishes at 17:30, new one starts at 17:20")
        print("\tNext screening starts at 18:00, new one finishes at 18:30")
        print()
        has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Auditorium.is_available() finished: {}".format(res))


def test_add_screening():
    print("Checking Auditorium.add_screening()")
    has_error = False

    auditorium = Auditorium(100)
    auditorium.screenings = [
        Screening(Movie("ABC", 120, "action", 18, "2023/01/31"), auditorium, (15, 30)),
        Screening(Movie("DEF", 90, "action", 18, "2023/01/31"), auditorium, (18, 00)),
        Screening(Movie("ABC", 120, "action", 18, "2023/01/31"), auditorium, (21, 00)),
    ]

    # testing possible screenings
    test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), auditorium, (19, 35))
    st_res = auditorium.add_screening(test_screening)
    if st_res is not True:
        print("\tAuditorium.add_screening() returned wrong value, expected True, got {}".format(st_res))
        print("\tPrevious screening finishes at 19:30, new one starts at 19:35")
        print("\tNext screening starts at 21:00, new one finishes at 20:55")
        print()
        has_error = True
    if test_screening not in auditorium.screenings:
        print("\tAuditorum.add_screening() should add new screening to list of screenings")
        print("\tPrevious screening finishes at 19:30, new one starts at 19:35")
        print("\tNext screening starts at 21:00, new one finishes at 20:55")
        print()
        has_error = True

    test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), auditorium, (23, 5))
    st_res = auditorium.add_screening(test_screening)
    if st_res is not True:
        print("\tAuditorium.add_screening() returned wrong value, expected True, got {}".format(st_res))
        print("\tPrevious screening finishes at 23:00, new one starts at 23:05")
        print("\tNo next screening defined")
        print()
        has_error = True
    if test_screening not in auditorium.screenings:
        print("\tAuditorum.add_screening() should add new screening to list of screenings")
        print("\tPrevious screening finishes at 23:00, new one starts at 23:05")
        print("\tNo next screening defined")
        print()
        has_error = True

    test_screening = Screening(Movie("JKL", 20, "comedy", 12, "2023/03/31"), auditorium, (17, 35))
    st_res = auditorium.add_screening(test_screening)
    if st_res is not True:
        print("\tAuditorium.add_screening() returned wrong value, expected True, got {}".format(st_res))
        print("\tPrevious screening finishes at 17:30, new one starts at 17:35")
        print("\tNext screening starts at 18:00, new one finishes at 17:55")
        print()
        has_error = True
    if test_screening not in auditorium.screenings:
        print("\tAuditorum.add_screening() should add new screening to list of screenings")
        print("\tPrevious screening finishes at 17:30, new one starts at 17:35")
        print("\tNext screening starts at 18:00, new one finishes at 17:55")
        print()
        has_error = True

    # testing impossible screenings
    test_screening = Screening(Movie("GHI", 120, "comedy", 16, "2023/03/31"), auditorium, (19, 35))
    st_res = auditorium.add_screening(test_screening)
    if st_res is not False:
        print("\tAuditorium.add_screening() returned wrong value, expected False, got {}".format(st_res))
        print("\tPrevious screening finishes at 19:30, new one starts at 19:35")
        print("\tNext screening starts at 21:00, new one finishes at 21:35")
        print()
        has_error = True
    if test_screening in auditorium.screenings:
        print("\tAuditorum.add_screening() shouldn't add new screening to list of screenings")
        print("\tPrevious screening finishes at 19:30, new one starts at 19:35")
        print("\tNext screening starts at 21:00, new one finishes at 21:35")
        print()
        has_error = True

    test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), auditorium, (22, 30))
    st_res = auditorium.add_screening(test_screening)
    if st_res is not False:
        print("\tAuditorium.add_screening() returned wrong value, expected False, got {}".format(st_res))
        print("\tPrevious screening finishes at 23:00, new one starts at 22:30")
        print()
        has_error = True
    if test_screening in auditorium.screenings:
        print("\tAuditorum.add_screening() shouldn't add new screening to list of screenings")
        print("\tPrevious screening finishes at 23:00, new one starts at 22:30")
        print()
        has_error = True

    test_screening = Screening(Movie("JKL", 70, "comedy", 12, "2023/03/31"), auditorium, (17, 20))
    st_res = auditorium.add_screening(test_screening)
    if st_res is not False:
        print("\tAuditorium.add_screening() returned wrong value, expected False, got {}".format(st_res))
        print("\tPrevious screening finishes at 17:30, new one starts at 17:20")
        print("\tNext screening starts at 18:00, new one finishes at 18:30")
        print()
        has_error = True
    if test_screening in auditorium.screenings:
        print("\tAuditorum.add_screening() shouldn't add new screening to list of screenings")
        print("\tPrevious screening finishes at 17:30, new one starts at 17:20")
        print("\tNext screening starts at 18:00, new one finishes at 18:30")
        print()
        has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Auditorium.add_screening() finished: {}".format(res))


def test_auditorium():
    try:
        test_auditorium_structure()
        test_movie_structure()
        test_screening_structure()
    except RuntimeError:
        print("Cannot test Auditorium class")
        return

    test_is_available()
    print()

    test_add_screening()
    print()


if __name__ == '__main__':
    test_auditorium()
