from auditorium_tests import test_auditorium
from cinema_tests import test_cinema
from group_tests import test_friendgroup
from Zadanie2.movie_tests import test_movie
from person_tests import test_person
from screening_tests import test_screening


def main():
    print("MOVIE TESTING:")
    test_movie()
    print()

    print("AUDITORIUM TESTING:")
    test_auditorium()
    print()

    print("CINEMA TESTING:")
    test_cinema()
    print()

    print("SCREENING TESTING:")
    test_screening()
    print()

    print("PERSON TESTING:")
    test_person()
    print()

    print("FRIENDGROUP TESTING:")
    test_friendgroup()
    print()


if __name__ == '__main__':
    main()
