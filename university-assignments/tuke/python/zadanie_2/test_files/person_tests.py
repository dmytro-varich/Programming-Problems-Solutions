from auditorium import Auditorium
from movie import Movie
from person import Person
from screening import Screening
from Zadanie2.structure_tests import *


def test_is_interested():
    print("Checking Person.is_interested()")
    has_error = False

    test_person = Person(
        ['adventure', 'drama', 'fantasy', 'noir', 'sci-fi'],
        18, 23, 0.5)
    tests = [
        ('animated', False),
        ('drama', True),
        ('fantasy', True),
        ('horror', False),
        ('noir', True),
        ('thriller', False)
    ]

    for category, corr in tests:
        movie = Movie("ABC", 90, category, 12, "2021/01/31")
        try:
            st_res = test_person.is_interested(movie)
        except Exception as e:
            print("\tCalling Person.is_interested() caused an unexpected error")
            print("\t", e)
            pritn()
            has_error = True
        else:
            if not isinstance(st_res, bool):
                print("\tPerson.is_interested() return wrong value type")
                print("\tExpected bool, got", type(st_res))
                print()
                has_error = True
            elif st_res is not corr:
                print("\tPerson.is_interested() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tInterests {}, genre {}".format(test_person.interests, category))
                print()
                has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Person.is_interested() finished: {}".format(res))


def test_is_allowed():
    print("Checking Person.is_allowed()")
    has_error = False

    test_person = Person(
        ['adventure', 'drama', 'fantasy', 'noir', 'sci-fi'],
        16, 23, 0.5)
    tests = [
        (12, True),
        (16, True),
        (18, False),
        (20, False),
        (6, True),
        (10, True)
    ]

    for age, corr in tests:
        movie = Movie("ABC", 90, "action", age, "2021/01/31")
        try:
            st_res = test_person.is_allowed(movie)
        except Exception as e:
            print("\tCalling Person.is_allowed() caused an unexpected error")
            print("\t", e)
            pritn()
            has_error = True
        else:
            if not isinstance(st_res, bool):
                print("\tPerson.is_allowed() return wrong value type")
                print("\tExpected bool, got", type(st_res))
                print()
                has_error = True
            elif st_res is not corr:
                print("\tPerson.is_allowed() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tAge limit {}, person age {}".format(age, test_person.age))
                print()
                has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Person.is_allowed() finished: {}".format(res))


def test_can_attend():
    print("Checking Person.can_attend()")
    has_error = False

    test_person = Person(['adventure'], 16, 22, 0.5)

    test_screenings = [
        (Screening(Movie("ABC", 120, "adventure", 12, "2023/01/31"), Auditorium(100), (17, 0)), True),
        (Screening(Movie("ABC", 120, "adventure", 12, "2023/01/31"), Auditorium(100), (19, 45)), True),
        (Screening(Movie("ABC", 120, "adventure", 12, "2023/01/31"), Auditorium(100), (20, 0)), False),
        (Screening(Movie("ABC", 120, "adventure", 16, "2023/01/31"), Auditorium(100), (17, 0)), True),
        (Screening(Movie("ABC", 120, "adventure", 16, "2023/01/31"), Auditorium(100), (19, 45)), True),
        (Screening(Movie("ABC", 120, "adventure", 16, "2023/01/31"), Auditorium(100), (20, 0)), False),
        (Screening(Movie("ABC", 120, "adventure", 18, "2023/01/31"), Auditorium(100), (17, 0)), False),
        (Screening(Movie("ABC", 120, "adventure", 18, "2023/01/31"), Auditorium(100), (19, 45)), False),
        (Screening(Movie("ABC", 120, "adventure", 18, "2023/01/31"), Auditorium(100), (20, 0)), False)
    ]

    for screening, corr in test_screenings:
        try:
            st_res = test_person.can_attend(screening)
        except Exception as e:
            print("\tCalling Person.can_attend() caused an unexpected error")
            print("\t", e)
            print()
            has_error = True
        else:
            if not isinstance(st_res, bool):
                print("\tPerson.can_attend() return wrong value type")
                print("\tExpected bool, got", type(st_res))
                print()
                has_error = True
            elif st_res is not corr:
                print("\tPerson.can_attend() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tAge limit {}, person age {}".format(screening.movie.age_limit, test_person.age))
                print("\tBedtime {}, finish {}".format(22, screening.get_end_time()))
                print()
                has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Person.can_attend() finished: {}".format(res))


def test_will_attend():
    print("Checking Person.will_attend()")
    has_error = False

    test_person1 = Person(["adventure"], 16, 22, 0.75)
    test_person2 = Person(["adventure"], 16, 22, 0.5)
    test_screening = Screening(
        Movie("ABC", 120, "adventure", 12, "2023/01/31"),
        Auditorium(100),
        (17, 0)
    )

    test_cases = [
        (0, True, True),
        (20, True, True),
        (40, True, True),
        (49, True, True),
        (50, True, False),
        (60, True, False),
        (74, True, False),
        (75, False, False),
        (80, False, False),
        (90, False, False),
        (100, False, False)
    ]

    for test_person in [test_person1, test_person2]:
        for sold, corr1, corr2 in test_cases:
            try:
                test_screening.tickets_sold = sold
                st_res = test_person.will_attend(test_screening)
            except Exception as e:
                print("\tCalling Person.will_attend() caused an unexpected error")
                print("\t", e)
                pritn()
                has_error = True
            else:
                corr = corr1 if test_person == test_person1 else corr2
                if not isinstance(st_res, bool):
                    print("\tPerson.will_attend() return wrong value type")
                    print("\tExpected bool, got", type(st_res))
                    print()
                    has_error = True
                elif st_res is not corr:
                    print("\tPerson.will_attend() returned wrong value")
                    print("\tExpected {}, got {}".format(corr, st_res))
                    print("\tTolerance {}, occupancy {}".format(test_person.tolerance, sold / 100))
                    print()
                    has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Person.will_attend() finished: {}".format(res))


def test_person():
    try:
        test_movie_structure()
        test_auditorium_structure()
        test_screening_structure()
        test_person_structure()
    except RuntimeError:
        print("Cannot test Auditorium class")
        return

    test_is_interested()
    print()

    test_is_allowed()
    print()

    test_can_attend()
    print()

    test_will_attend()
    print()


if __name__ == '__main__':
    test_person()
