from movie import Movie
from screening import Screening
from Zadanie2.structure_tests import *


A1 = Auditorium(100)
A2 = Auditorium(200)

M1 = Movie("ABC", 120, "action", 18, "2023/01/31")
M2 = Movie("DEF", 90, "comedy", 16, "2023/03/31")
M3 = Movie("GHI", 150, "historical", 16, "2023/04/10")

CINEMA = Cinema([A1, A2])


def test_add_movie():
    print("Checking Cinema.add_movie()")
    has_error = False

    # testing with all good times
    try:
        start_times = [(18, 0), (19, 0), (21, 5), (21, 15)]
        CINEMA.add_movie(M1, start_times)
    except Exception as e:
        print("\tCalling Cinema.add_movie() caused an unexpected error")
        print("\t", e)
        has_error = True
    else:
        if len(CINEMA.screenings) != 4:
            print("\tNot all screenings were added to Cinema.screenings list")
            print("\tExpected 4 screenings, got {}".format(len(CINEMA.screenings)))
            print()
            has_error = True
        if len(A1.screenings) + len(A2.screenings) != 4:
            print("\tNot all screenings were added to Auditorium.screenings list")
            print("\tExpected 4 screenings, got {}".format(len(A1.screenings) + len(A2.screenings)))
            print()
            has_error = True
        if not all([isinstance(elem, Screening) for elem in CINEMA.screenings]):
            print("\tNot all elements if Cinema.screenings list are of type Screening")
            has_error = True
        screening_times = [sc.time for sc in CINEMA.screenings]
        for start_time in start_times:
            if start_time not in screening_times:
                print("\tCould not find screening at {} in Cinema.screenings list".format(start_time))
                print()
                has_error = True

    try:
        start_times = [(17, 0)]
        CINEMA.add_movie(M2, start_times)
    except Exception as e:
        print("\tCalling Cinema.add_movie() caused an unexpected error")
        print("\t", e)
        has_error = True
    else:
        if len(CINEMA.screenings) != 5:
            print("\tNot all screenings were added to Cinema.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(CINEMA.screenings)))
            print()
            has_error = True
        if len(A1.screenings) + len(A2.screenings) != 5:
            print("\tNot all screenings were added to Auditorium.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(A1.screenings) + len(A2.screenings)))
            print()
            has_error = True
        if not all([isinstance(elem, Screening) for elem in CINEMA.screenings]):
            print("\tNot all elements if Cinema.screenings list are of type Screening")
            has_error = True
        screening_times = [sc.time for sc in CINEMA.screenings]
        for start_time in start_times:
            if start_time not in screening_times:
                print("\tCould not find screening at {} in Cinema.screenings list".format(start_time))
                print()
                has_error = True

    # testing with incorrect times
    try:
        start_times = [(19, 30)]
        CINEMA.add_movie(M2, start_times)
    except RuntimeError as e:
        corr = "Could not add movie DEF at 19:30"
        if str(e) != corr:
            print("\tCalling Cinema.add_movie() caused RuntimeError with wrong message")
            print("\tExpected {}, got {}".format(corr, e))
            print()
            has_error = True
    except Exception as e:
        print("\tCalling Cinema.add_movie() caused an unexpected error")
        print("\t", e)
        has_error = True
    else:
        if len(CINEMA.screenings) != 5:
            print("\tNo screenings should have been added to Cinema.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(CINEMA.screenings)))
            print()
            has_error = True
        if len(A1.screenings) + len(A2.screenings) != 5:
            print("\tNo screenings should have been added to Auditorium.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(A1.screenings) + len(A2.screenings)))
            print()
            has_error = True
        if not all([isinstance(elem, Screening) for elem in CINEMA.screenings]):
            print("\tNot all elements if Cinema.screenings list are of type Screening")
            has_error = True
        screening_times = [sc.time for sc in CINEMA.screenings]
        for start_time in start_times:
            if start_time in screening_times:
                print("\tFound unexpected screening at {} in Cinema.screenings list".format(start_time))
                print()
                has_error = True

    try:
        start_times = [(19, 5)]
        CINEMA.add_movie(M3, start_times)
    except RuntimeError as e:
        corr = "Could not add movie GHI at 19:05"
        if str(e) != corr:
            print("\tCalling Cinema.add_movie() caused RuntimeError with wrong message")
            print("\tExpected {}, got {}".format(corr, e))
            print()
            has_error = True
    except Exception as e:
        print("\tCalling Cinema.add_movie() caused an unexpected error")
        print("\t", e)
        has_error = True
    else:
        if len(CINEMA.screenings) != 5:
            print("\tNo screenings should have been added to Cinema.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(CINEMA.screenings)))
            print()
            has_error = True
        if len(A1.screenings) + len(A2.screenings) != 5:
            print("\tNo screenings should have been added to Auditorium.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(A1.screenings) + len(A2.screenings)))
            print()
            has_error = True
        if not all([isinstance(elem, Screening) for elem in CINEMA.screenings]):
            print("\tNot all elements if Cinema.screenings list are of type Screening")
            has_error = True
        screening_times = [sc.time for sc in CINEMA.screenings]
        for start_time in start_times:
            if start_time in screening_times:
                print("\tFound unexpected screening at {} in Cinema.screenings list".format(start_time))
                print()
                has_error = True

    try:
        start_times = [(22, 0)]
        CINEMA.add_movie(M3, start_times)
    except RuntimeError as e:
        corr = "Could not add movie GHI at 22:00"
        if str(e) != corr:
            print("\tCalling Cinema.add_movie() caused RuntimeError with wrong message")
            print("\tExpected {}, got {}".format(corr, e))
            print()
            has_error = True
    except Exception as e:
        print("\tCalling Cinema.add_movie() caused an unexpected error")
        print("\t", e)
        has_error = True
    else:
        if len(CINEMA.screenings) != 5:
            print("\tNo screenings should have been added to Cinema.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(CINEMA.screenings)))
            print()
            has_error = True
        if len(A1.screenings) + len(A2.screenings) != 5:
            print("\tNo screenings should have been added to Auditorium.screenings list")
            print("\tExpected 5 screenings, got {}".format(len(A1.screenings) + len(A2.screenings)))
            print()
            has_error = True
        if not all([isinstance(elem, Screening) for elem in CINEMA.screenings]):
            print("\tNot all elements if Cinema.screenings list are of type Screening")
            has_error = True
        screening_times = [sc.time for sc in CINEMA.screenings]
        for start_time in start_times:
            if start_time in screening_times:
                print("\tFound unexpected screening at {} in Cinema.screenings list".format(start_time))
                print()
                has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Cinema.add_movie() finished: {}".format(res))


def test_get_movies_shown():
    print("Checking Cinema.get_movies_shown()")
    has_error = False

    try:
        st_res = CINEMA.get_movies_shown()
    except Exception as e:
        print("\tCalling Cinema.get_movies_shown() caused an unexpected error")
        print(e)
        has_error = True

    if not has_error and not isinstance(st_res, list):
        print("\tCinema.get_movies_shown() returned value of wrong type")
        print("\tExpected list, got", type(st_res))
        print()
        has_error = True
    elif not all([isinstance(elem, Movie) for elem in st_res]):
        print("\tCinema.get_movies_shown() result has other objects than Movie")
        print("\tFound", [type(elem) for elem in st_res])
        print()
        has_error = True
    elif M1 not in st_res:
        print("\tCinema.get_movies_shown() returned wrong value")
        print("\tCould not find movie ABC")
        print()
        has_error = True
    elif M2 not in st_res:
        print("\tCinema.get_movies_shown() returned wrong value")
        print("\tCould not find movie DEF")
        print()
        has_error = True
    elif M3 in st_res:
        print("\tCinema.get_movies_shown() returned wrong value")
        print("\tFound movie GHI")
        print()
        has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Cinema.get_movies_shown() finished: {}".format(res))


def test_get_screenings_for_movie():
    print("Checking Cinema.get_screenings_for_movie()")
    has_error = False

    corr = [
        (M1, [(18, 0), (19, 0), (21, 5), (21, 15)]),
        (M2, [(17, 0)]),
        (M3, [])
    ]

    for test_movie, times in corr:
        try:
            st_res = CINEMA.get_screenings_for_movie(test_movie)
        except Exception as e:
            print("\tCalling Cinema.get_screenings_for_movie() caused an unexpected error")
            print(e)
            has_error = True
        else:
            if not isinstance(st_res, list):
                print("\tCinema.get_screenings_for_movie() returned value of wrong type")
                print("\tExpected list, got", type(st_res))
                print()
                has_error = True
            elif not all([isinstance(elem, Screening) for elem in st_res]):
                print("\tCinema.get_screenings_for_movie() result has other objects than Screening")
                print("\tFound", [type(elem) for elem in st_res])
                print()
                has_error = True
            else:
                screening_times = [sc.time for sc in st_res]
                if len(screening_times) != len(times):
                    print("\tCinema.get_screenings_for_movie() returned incorrect number of screenings")
                    print("\tExpected {}, got {}".format(len(times), len(screening_times)))
                for corr_time in times:
                    if corr_time not in screening_times:
                        print("\tCould not find starting time {} in result".format(corr_time))
                        print()
                        has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Cinema.get_screenings_for_movie() finished: {}".format(res))


def test_cinema():
    try:
        test_movie_structure()
        test_auditorium_structure()
        test_screening_structure()
        test_cinema_structure()
    except RuntimeError:
        print("Cannot test Auditorium class")
        return

    test_add_movie()
    print()

    test_get_movies_shown()
    print()

    test_get_screenings_for_movie()
    print()


if __name__ == '__main__':
    test_cinema()
