from Zadanie2.structure_tests import *

MOVIE = Movie("ABC", 95, "action", 18, "2023/01/31")
AUDITORIUM = Auditorium(20)
SCREENING = Screening(MOVIE, AUDITORIUM, (21, 0))


def test_sell_tickets():
    print("Checking Screening.sell_tickets()")
    has_error = False

    # testing selling possible
    test_counts = [5, 10, 3]
    for idx, count in enumerate(test_counts, start=1):
        try:
            st_res = SCREENING.sell_tickets(count)
        except Exception as e:
            print("\tCalling Screening.sell_tickets() caused an unexpected error")
            print("\t", e)
            has_error = True
        else:
            if st_res is not True:
                print("\tScreening.sell_tickets() returned wrong value")
                print("\tExpected True, got", st_res)
                has_error = True
            elif SCREENING.tickets_sold != sum(test_counts[:idx]):
                print("\tScreening.sell_tickets() did not update Screening.tickets_sold value")
                print("\tExpected {}, got {}".format(sum(test_counts[:idx]), SCREENING.tickets_sold))
                has_error = True

    # testing selling impossible
    test_counts = [5, 10, 3]
    for idx, count in enumerate(test_counts, start=1):
        try:
            st_res = SCREENING.sell_tickets(count)
        except Exception as e:
            print("\tCalling Screening.sell_tickets() caused an unexpected error")
            print("\t", e)
            has_error = True
        else:
            if st_res is not False:
                print("\tScreening.sell_tickets() returned wrong value")
                print("\tExpected True, got", st_res)
                has_error = True
            elif SCREENING.tickets_sold != 18:
                print("\tScreening.sell_tickets() should not update Screening.tickets_sold value")
                print("\tExpected 18, got {}".format(SCREENING.tickets_sold))
                has_error = True

    # testing extreme case
    try:
        st_res = SCREENING.sell_tickets(2)
    except Exception as e:
        print("\tCalling Screening.sell_tickets() caused an unexpected error")
        print("\t", e)
        has_error = True
    else:
        if st_res is not True:
            print("\tScreening.sell_tickets() returned wrong value")
            print("\tExpected True, got", st_res)
            has_error = True
        elif SCREENING.tickets_sold != 20:
            print("\tScreening.sell_tickets() did not update Screening.tickets_sold value")
            print("\tExpected 20, got {}".format(SCREENING.tickets_sold))
            has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Screening.sell_tickets() finished: {}".format(res))


def test_get_occupancy():
    print("Checking Screening.get_occupancy()")
    has_error = False

    # testing selling possible
    test_vals = [(5, 0.25), (15, 0.75), (18, 0.9), (20, 1.0)]
    for tickets, corr in test_vals:
        try:
            SCREENING.tickets_sold = tickets
            st_res = SCREENING.get_occupancy()
        except Exception as e:
            print("\tCalling Screening.get_occupancy() caused an unexpected error")
            print("\t", e)
            has_error = True
        else:
            if not isinstance(st_res, float):
                print("\tScreening.get_occupancy() returned wrong value type")
                print("\tExpected float, got", type(st_res))
                has_error = True
            elif abs(st_res - corr) > 1e-3:
                print("\tScreening.get_occupancy() returned wrong value")
                print("\tExpected {:.3f}, got {:.3f}".format(corr, st_res))
                has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Screening.get_occupancy() finished: {}".format(res))


def test_get_end_time():
    print("Checking Screening.get_end_time()")
    has_error = False

    test_vals = [
        ((17, 0), (18, 35)),
        ((17, 5), (18, 40)),
        ((18, 15), (19, 50)),
        ((21, 3), (22, 38)),
    ]
    for start, end in test_vals:
        try:
            SCREENING.time = start
            st_res = SCREENING.get_end_time()
        except Exception as e:
            print("\tCalling Screening.get_end_time() caused an unexpected error")
            print("\t", e)
            has_error = True
        else:
            if not isinstance(st_res, tuple):
                print("\tScreening.get_end_time() returned wrong value type")
                print("\tExpected float, got", type(st_res))
                has_error = True
            elif len(st_res) != 2:
                print("\tScreening.get_end_time() returned tuple with wrong length")
                print("\tExpected two values, got", len(st_res))
                has_error = True
            elif not all([isinstance(elem, int) for elem in st_res]):
                print("\tScreening.get_end_time() did not return tuple of integers")
                print("\tExpected only integers, got", [isinstance(elem, int) for elem in st_res])
                has_error = True
            elif st_res != end:
                print("\tScreening.get_end_time() returned wrong value")
                print("\tExpected {}, got {}".format(end, st_res))
                has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Screening.get_end_time() finished: {}".format(res))


def test_screening():
    try:
        test_movie_structure()
        test_auditorium_structure()
        test_screening_structure()
    except RuntimeError:
        print("Cannot test Auditorium class")
        return

    test_sell_tickets()
    print()

    test_get_occupancy()
    print()

    test_get_end_time()
    print()


if __name__ == '__main__':
    test_screening()
