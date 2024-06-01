from copy import deepcopy

from Zadanie2.structure_tests import *


M1 = Movie("A", 120, "action", 16, "2023/01/31")
M2 = Movie("B", 90, "animated", 6, "2023/02/25")
M3 = Movie("C", 150, "historical", 18, "2023/03/16")
M4 = Movie("D", 120, "action", 16, "2023/04/10")

A1 = Auditorium(100)
A2 = Auditorium(200)
A3 = Auditorium(50)

CINEMA = Cinema([A1, A2, A3])

S11 = Screening(M2, A1, (17, 0))
S11.tickets_sold = 45
S12 = Screening(M1, A1, (19, 0))
S12.tickets_sold = 62
S13 = Screening(M1, A1, (21, 10))
S13.tickets_sold = 24

S21 = Screening(M3, A2, (18, 0))
S21.tickets_sold = 74
S22 = Screening(M1, A2, (21, 0))
S22.tickets_sold = 127

S31 = Screening(M1, A3, (17, 0))
S31.tickets_sold = 14
S32 = Screening(M3, A3, (19, 30))
S32.tickets_sold = 22
S33 = Screening(M1, A3, (21, 30))
S33.tickets_sold = 21

A1.screenings = [S11, S12, S13]
A2.screenings = [S21, S22]
A3.screenings = [S31, S32, S33]

CINEMA.screenings = [S11, S12, S13, S21, S22, S31, S32, S33]

FG1 = FriendGroup(
    [Person(["action", "adventure"], 21, 23, 0.5),
     Person(["adventure", "fantasy"], 23, 23, 0.4),
     Person(["horror", "noir"], 20, 22, 0.7),
     Person(["action", "historical"], 24, 23, 0.8),
     Person(["drama", "historical"], 21, 23, 0.7),
     Person(["action"], 22, 22, 0.9),
     Person(["action", "drama"], 21, 23, 0.9),
     Person(["animated", "comedy"], 23, 22, 0.8),
     Person(["action", "thriller"], 24, 23, 0.6),
     Person(["action", "comedy"], 20, 23, 0.8)]
)
FG2 = FriendGroup(
    [Person(["adventure"], 19, 22, 0.4),
     Person(["fantasy"], 21, 23, 0.8),
     Person(["historical"], 22, 22, 0.6),
     Person(["historical"], 18, 23, 0.7),
     Person(["historical"], 19, 23, 0.7),
     Person(["action"], 17, 21, 0.4),
     Person(["drama"], 24, 22, 0.6),
     Person(["adventure"], 22, 22, 0.9),
     Person(["historical"], 26, 23, 0.8),
     Person(["action"], 21, 23, 0.7)]
)
FG3 = FriendGroup(
    [Person(["animated", "comedy"], 14, 20, 0.9),
     Person(["fantasy"], 16, 21, 0.9),
     Person(["horror"], 17, 21, 0.8),
     Person(["action", "historical"], 24, 22, 0.7),
     Person(["historical", "animated"], 21, 22, 0.6),
     Person(["animated"], 17, 21, 0.9),
     Person(["action", "animated"], 15, 20, 0.9),
     Person(["animated", "comedy"], 15, 20, 0.8),
     Person(["animated", "comedy"], 16, 21, 0.9),
     Person(["action", "comedy"], 17, 21, 0.8)]
)


def test_order_movies():
    print("Checking FriendGroup.order_movies()")
    has_error = False

    test_cases = [
        (FG1, [(M1, 6), (M3, 2), (M2, 1)]),
        (FG2, [(M1, 2), (M2, 0)]),
        (FG3, [(M2, 6)])
    ]

    for group, corr in test_cases:
        try:
            test_group = deepcopy(group)
            st_res = test_group.order_movies(CINEMA)
        except Exception as e:
            print("\tCalling FriendGroup.order_movies() caused an unexpected error")
            print("\t", e)
            print()
            has_error = True
        else:
            if not isinstance(st_res, list):
                print("\tFriendGroup.order_movies() returned value of wrong type")
                print("\tExpected list, got", type(st_res))
                print()
                has_error = True
            else:
                for elem in st_res:
                    if not isinstance(elem, tuple):
                        print("\tFriendGroup.order_movies() should contain only tuples")
                        print("\t{} found: {}".format(type(elem), st_res))
                        print()
                        has_error = True
                    elif len(elem) != 2:
                        print("\tFriendGroup.order_movies() should contain only tuples with two values")
                        print("\t{} found: {}".format(elem, st_res))
                        print()
                        has_error = True
                else:
                    if st_res != corr:
                        print("\tFriendGroup.order_movies() returned wrong value")
                        print("\tExpected {}, got {}".format(corr, st_res))
                        print()
                        has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking FriendGroup.order_movies() finished: {}".format(res))


def test_choose_screening():
    print("Checking FriendGroup.choose_screening()")
    has_error = False

    test_cases = [
        (FG1, [(S21, 10, 10, 27), (S31, 10, 10, 71), (S32, 10, 9, 27), (S11, 10, 9, 46), (S12, 10, 7, 71), (S13, 0, 0, 71), (S22, 0, 0, 71), (S33, 0, 0, 71)]),
        (FG2, [(S31, 10, 10, 71), (S11, 10, 8, 46), (S12, 9, 6, 71), (S13, 0, 0, 71), (S22, 0, 0, 71), (S33, 0, 0, 71)]),
        (FG3, [(S11, 10, 10, 46)])
    ]

    for group, corr in test_cases:
        try:
            test_group = deepcopy(group)
            st_res = test_group.choose_screening(CINEMA)
        except Exception as e:
            print("\tCalling FriendGroup.choose_screening() caused an unexpected error")
            print("\t", e)
            print()
            has_error = True
        else:
            if not isinstance(st_res, tuple):
                print("\tFriendGroup.choose_screening() returned value of wrong type")
                print("\tExpected tuple, got", type(st_res))
                print()
                has_error = True
            elif len(st_res) != 2:
                print("\tFriendGroup.choose_screening() returned wrong value")
                print("\tExpected two values, got", len(st_res))
                print()
                has_error = True
            else:
                best, screen_list = st_res

                if not isinstance(screen_list, list):
                    print("\tFriendGroup.choose_screening() returned value of wrong type")
                    print("\tExpected list, got", type(screen_list))
                    print()
                    has_error = True
                else:
                    for elem in screen_list:
                        if not isinstance(elem, tuple):
                            print("\tFriendGroup.choose_screening() should contain only tuples")
                            print("\t{} found: {}".format(type(elem), screen_list))
                            print()
                            has_error = True
                        elif len(elem) != 4:
                            print("\tFriendGroup.choose_screening() should contain only tuples with four values")
                            print("\t{} found: {}".format(elem, screen_list))
                            print()
                            has_error = True
                    else:
                        if screen_list != corr:
                            print("\tFriendGroup.choose_screening() returned wrong value")
                            print("\tExpected {}, got {}".format(corr, screen_list))
                            print()
                            has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking FriendGroup.choose_screening() finished: {}".format(res))


def test_buy_tickets():
    print("Checking FriendGroup.buy_tickets()")
    has_error = False

    test_cases = [
        (FG1, S11, 10), (FG1, S12, 10), (FG1, S13, 0),
        (FG1, S21, 10), (FG1, S22, 0),
        (FG1, S31, 10), (FG1, S32, 10), (FG1, S33, 0),
        (FG2, S11, 10), (FG2, S12, 9), (FG2, S13, 0),
        (FG2, S21, 10), (FG2, S22, 0),
        (FG2, S31, 10), (FG2, S32, 9), (FG2, S33, 0),
        (FG3, S11, 10), (FG3, S12, 2), (FG3, S13, 0),
        (FG3, S21, 7), (FG3, S22, 0),
        (FG3, S31, 10), (FG3, S32, 2), (FG3, S33, 0)
    ]

    for group, screening, change in test_cases:
        test_group = deepcopy(group)
        test_screening = deepcopy(screening)
        orig_count = test_screening.tickets_sold
        try:
            st_res = test_group.buy_tickets(test_screening)
        except Exception as e:
            print("\tCalling FriendGroup.buy_tickets() caused an unexpected error")
            print("\t", e)
            print()
            has_error = True
        else:
            if st_res is not None:
                print("\tFriendGroup.buy_tickets() should not have a return value")
                print("\tExpected None, got", st_res)
                print()
                has_error = True
            else:
                corr = orig_count + change
                if test_screening.tickets_sold != corr:
                    print("\tIncorrect number of tickets bought in FriendGroup.buy_tickets()")
                    print("\tExpected {}, found {}".format(corr, test_screening.tickets_sold))
                    print()
                    has_error = True

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking FriendGroup.buy_tickets() finished: {}".format(res))


def test_friendgroup():
    try:
        test_movie_structure()
        test_auditorium_structure()
        test_cinema_structure()
        test_screening_structure()
        test_person_structure()
        test_friendgroup_structure()
    except RuntimeError:
        print("Cannot test Auditorium class")
        return

    test_order_movies()
    print()

    test_choose_screening()
    print()

    test_buy_tickets()
    print()


if __name__ == '__main__':
    test_friendgroup()
