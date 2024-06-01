from movie import Movie
from structure_tests import test_movie_structure


def check_movie_constructor_types():
    has_error = False
    # checking with wrong type of title
    try:
        movie = Movie(1237, 120, "action", 18, "2023/01/31")
    except TypeError as t_err:
        if str(t_err) != "Movie title must be string":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect title type")
        print("\t\tUnexpected error when calling Movie constructor:")
        print(e)
        has_error = True
    else:
        print("\tTesting with incorrect title type")
        print("\t\tDid not generate error for wrong title type")
        has_error = True

    # checking with wrong type of length
    try:
        movie = Movie("ABC", "120", "action", 18, "2023/01/31")
    except TypeError as t_err:
        if str(t_err) != "Movie length must be integer":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect length type")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect length type")
        print("\t\tDid not generate error for wrong length type")
        has_error = True

    # checking with wrong type of age_limit
    try:
        movie = Movie("ABC", 120, "action", "18", "2023/01/31")
    except TypeError as t_err:
        if str(t_err) != "Age limit must be integer":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect age_limit type")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect age_limit type")
        print("\t\tDid not generate error for wrong age_limit type")
        has_error = True

    # checking with wrong type of release_date
    try:
        movie = Movie("ABC", 120, "action", 18, 2023)
    except TypeError as t_err:
        if str(t_err) != "Release date must be string":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect release_date type")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect release_date type")
        print("\t\tDid not generate error for wrong release_date type")
        has_error = True

    return has_error


def check_movie_constructor_values():
    has_error = False
    # checking with wrong length value
    try:
        movie = Movie("ABC", 0, "action", 18, "2023/01/31")
    except ValueError as v_err:
        if str(v_err) != "Movie length must be at least 1":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect length value - zero")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect length value - zero")
        print("\t\tDid not generate error for wrong length value")
        has_error = True

    try:
        movie = Movie("ABC", -12, "action", 18, "2023/01/31")
    except ValueError as v_err:
        if str(v_err) != "Movie length must be at least 1":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect length value - negative value")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect length value - negative value")
        print("\t\tDid not generate error for wrong length value")
        has_error = True

    # checking with wrong genre value
    try:
        movie = Movie("ABC", 120, 123, 18, "2023/01/31")
    except ValueError as v_err:
        if str(v_err) != "Unknown genre \"123\"":
            print("\t\tMovie.__init__() generated incorrect error message")
            print(v_err)
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect genre value - wrong type")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect genre value - wrong type")
        print("\t\tDid not generate error for wrong genre value")
        has_error = True

    try:
        movie = Movie("ABC", 120, "dramedy", 18, "2023/01/31")
    except ValueError as v_err:
        if str(v_err) != "Unknown genre \"dramedy\"":
            print("\t\tMovie.__init__() generated incorrect error message")
            print(v_err)
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect genre value - wrong value")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect genre value - wrong value")
        print("\t\tDid not generate error for wrong genre value")
        has_error = True

    # checking with wrong age limit value
    try:
        movie = Movie("ABC", 120, "action", 0, "2023/01/31")
    except ValueError as v_err:
        if str(v_err) != "Age limit must be at least 1":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect age_limit value - zero")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect age_limit value - zero")
        print("\t\tDid not generate error for wrong age_limit value")
        has_error = True

    try:
        movie = Movie("ABC", 120, "action", -18, "2023/01/31")
    except ValueError as v_err:
        if str(v_err) != "Age limit must be at least 1":
            print("\t\tMovie.__init__() generated incorrect error message")
            has_error = True
    except Exception as e:
        print("\tTesting with incorrect age limit value - negative value")
        print("\t\tUnexpected error when calling Movie constructor:")
        print("\t\t", e)
        has_error = True
    else:
        print("\tTesting with incorrect age limit value - negative value")
        print("\t\tDid not generate error for wrong age_limit value")
        has_error = True

    return has_error


def test_movie_constructor():
    print("Checking Movie.__init__()")
    type_tests = check_movie_constructor_types()

    value_tests = check_movie_constructor_values()

    has_error = type_tests or value_tests
    res = "passed all tests" if not has_error else "did not pass all tests"
    print("Checking Movie.__init__() finished: {}".format(res))


def run_validate_test(movie, date, corr_err, corr_msg):
    try:
        movie.validate_date(date)
    except corr_err as e:
        if str(e) != corr_msg:
            print("\t\tMovie.validate_date() generated incorrect error message")
            print("\t\tExpected {}, got {}".format(corr_msg, e))
            return True
    except Exception as e:
        print("\t\tUnexpected error when calling Movie.validate_date():")
        print("\t\t", e)
        return True
    else:
        print("\t\tMovie.validate_date() did not generate error when expected")
        return True

    return False


def test_validate_date():
    print("Checking Movie.validate_date()")
    has_error = False

    movie = Movie("ABC", 120, "action", 18, "2023/01/31")

    # testing with wrong type
    with_err = run_validate_test(
        movie, 2023, TypeError, "Release date must be string")
    has_error = has_error or with_err

    # testing with incorrect number of /
    with_err = run_validate_test(
        movie, "2023/01/31/", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "/2023/01/31", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023//01/31", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "20230131", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "20230131", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err

    # testing with incorrect / position
    with_err = run_validate_test(
        movie, "20230/1/31", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "202/301/31", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/013/1", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/0131/", ValueError, "Release date must meet format YYYY/MM/DD")
    has_error = has_error or with_err

    # testing with incorrect year/month/day value
    with_err = run_validate_test(
        movie, "2o23/01/31", ValueError, "Could not load date from string: \"2o23/01/31\"")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/o1/31", ValueError, "Could not load date from string: \"2023/o1/31\"")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/01/3i", ValueError, "Could not load date from string: \"2023/01/3i\"")
    has_error = has_error or with_err

    # testing with invalid month
    with_err = run_validate_test(
        movie, "2023/-1/23", ValueError, "Invalid month -1")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/13/28", ValueError, "Invalid month 13")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/00/25", ValueError, "Invalid month 0")
    has_error = has_error or with_err

    # testing with invalid day
    with_err = run_validate_test(
        movie, "2023/01/33", ValueError, "Invalid day for January: 33")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/02/30", ValueError, "Invalid day for February: 30")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/03/-1", ValueError, "Invalid day for March: -1")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/04/31", ValueError, "Invalid day for April: 31")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/05/00", ValueError, "Invalid day for May: 0")
    has_error = has_error or with_err
    with_err = run_validate_test(
        movie, "2023/06/31", ValueError, "Invalid day for June: 31")
    has_error = has_error or with_err

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Movie.validate_date() finished: {}".format(res))


def check_get_time_passed_result(movie, date, corr):
    try:
        st_res = movie.get_time_passed(date)
        if st_res != corr:
            print(
                "\tIncorrect result for release date {} and date {}".format(
                    movie.release_date, date))
            print("\tExpected {}, got {}".format(corr, st_res))
            return True
    except Exception as e:
        print("\tCalling Movie.get_time_passed() caused an error")
        print("\t", e)
        return True
    else:
        return False


def test_get_time_passed():
    print("Checking Movie.get_time_passed()")
    has_error = False

    movie = Movie("ABC", 120, "action", 18, "2021/01/01")

    check_for = [
        ("2021/01/01", 0),
        ("2021/01/15", 14),
        ("2021/02/24", 54),
        ("2021/03/05", 63),
        ("2021/12/31", 364),
        ("2022/01/01", 365),
        ("2023/03/31", 819)
    ]

    for test_date, corr in check_for:
        wrong = check_get_time_passed_result(movie, test_date, corr)
        has_error = has_error or wrong

    res = "did not pass all tests" if has_error else "passed all tests"
    print("Checking Movie.get_time_passed() finished: {}".format(res))


def test_movie():
    try:
        test_movie_structure()
    except RuntimeError:
        print("Cannot test Movie class")
        return

    test_movie_constructor()
    print()

    test_validate_date()
    print()

    test_get_time_passed()
    print()


if __name__ == '__main__':
    test_movie()
