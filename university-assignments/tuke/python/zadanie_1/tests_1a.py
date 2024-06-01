import pickle

from assignment1 import *


def test_load_parking_records():
    print("Testing load_parking_records()...")
    with open("test_files/parking_records.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    format_points = 0.25
    passed = 0
    for i, corr_res in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = load_parking_records(
                "samples/parking_logs_{:02d}.csv".format(i))

            if not isinstance(st_res, list):
                print("\tIncorrect return type. Expected list, got", type(st_res))
                format_points = 0.0
                gets_point = False
                continue
            elif len(st_res) != len(corr_res):
                print("\tIncorrect return value. Expected list of {} values, got {}".format(len(corr_res), len(st_res)))
                format_points = 0.0
                gets_point = False
                continue
            else:
                for record in st_res:
                    if not isinstance(record, tuple):
                        print("\tIncorrect return type. Expected list of tuples, got list of", type(record))
                        format_points = 0.0
                        gets_point = False
                        continue
                    if len(record) != 5:
                        print("\tIncorrect return value. Expected tuples of 5 values, found", len(record))
                        format_points = 0.0
                        gets_point = False
                        continue
                    plate, start_h, start_m, end_h, end_m = record
                    if not isinstance(plate, str):
                        print("\tIncorrect return value. License plate should be string, found", type(plate))
                        format_points = 0.0
                        gets_point = False
                        continue
                    if not isinstance(start_h, int):
                        print("\tIncorrect return value. Start hour should be integer, found", type(start_h))
                        format_points = 0.0
                        gets_point = False
                        continue
                    if not isinstance(start_m, int):
                        print("\tIncorrect return value. Start minute should be integer, found", type(start_m))
                        format_points = 0.0
                        gets_point = False
                        continue
                    if not isinstance(end_h, int):
                        print("\tIncorrect return value. End hour should be integer, found", type(end_h))
                        format_points = 0.0
                        gets_point = False
                        continue
                    if not isinstance(end_m, int):
                        print("\tIncorrect return value. End minute should be integer, found", type(end_m))
                        format_points = 0.0
                        gets_point = False
                        continue

                    if record not in corr_res:
                        print("\tIncorrect return value. Could not find {} in source document".format(record))
                        gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = format_points + (passed / len(correct)) * 0.5
    print("Testing load_parking_records() finished: {:.2f}/0.75 points".format(points))
    return points


def test_load_prices():
    print("Testing load_prices()...")
    with open("test_files/parking_prices.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    format_points = 0.25
    passed = 0
    for i, corr_res in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = load_prices(
                "samples/prices_{:02d}.txt".format(i))

            if not isinstance(st_res, dict):
                print("\tIncorrect return type. Expected dict, got", type(st_res))
                format_points = 0.0
                gets_point = False
                continue
            elif len(st_res) != len(corr_res):
                print("\tIncorrect return value. Expected dict of {} values, got {}".format(len(corr_res), len(st_res)))
                format_points = 0.0
                gets_point = False
                continue
            else:
                for key, val in st_res.items():
                    if not isinstance(key, str):
                        print("\tIncorrect return type. Expected string key, found", type(key))
                        format_points = 0.0
                        gets_point = False
                        continue
                    if not isinstance(val, float):
                        print("\tIncorrect return type. Expected float value, found", type(val))
                        format_points = 0.0
                        gets_point = False
                        continue

                    if key not in corr_res:
                        print("\tIncorrect return value. Could not find {} in correct keys".format(key))
                        gets_point = False
                    elif abs(corr_res[key] - val) > 1e-6:
                        print("\tInocrrect return value. Expected {} under key {}, found {}".format(corr_res[key], key, val))
                        gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = format_points + (passed / len(correct)) * 0.5
    print("Testing load_prices() finished: {:.2f}/0.75 points".format(points))
    return points


def test_calculate_parking_time():
    print("Testing calculate_parking_time()...")
    with open("test_files/parking_times.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for start_h, start_m, end_h, end_m, corr_res in correct:
        try:
            gets_point = True
            st_res = calculate_parking_time(start_h, start_m, end_h, end_m)
            st_results.append(st_res)

            if not isinstance(st_res, int):
                print("\tIncorrect return type. Expected int, got", type(st_res))
                gets_point = False
            elif st_res != corr_res:
                print("\tIncorrect return value for {}:{:02d}-{}:{:02d}. Expected {}, got {}".format(
                    start_h, start_m, end_h, end_m, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 0.5
    if len(set(st_results)) == 1:
        points = 0
    print("Testing calculate_parking_time() finished: {:.2f}/0.5 points".format(points))
    return points


def test_get_parking_fee():
    print("Testing get_parking_fee()...")
    with open("test_files/parking_fees.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for time, prices, corr_res in correct:
        try:
            gets_point = True
            st_res = get_parking_fee(time, prices)
            st_results.append(st_res)

            if not isinstance(st_res, float):
                print("\tIncorrect return type. Expected float, got", type(st_res))
                gets_point = False
            elif abs(st_res - corr_res) > 1e-6:
                print("\tIncorrect return value for {} (prices: {}). Expected {}, got {}".format(
                    time, prices, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 1.0
    if len(set(st_results)) == 1:
        points = 0
    print("Testing get_parking_fee() finished: {:.2f}/1.0 point".format(points))
    return points


def test_calculate_average_parking_fee():
    print("Testing calculate_average_parking_fee()...")
    with open("test_files/average_parking_fees.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, prices, corr_res) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = calculate_average_parking_fee(records, prices)
            st_results.append(st_res)

            if not isinstance(st_res, float):
                print("\tIncorrect return type. Expected float, got", type(st_res))
                gets_point = False
            elif abs(st_res - corr_res) > 1e-6:
                print("\tIncorrect return value for test {}. Expected {:.5f}, got {:.5f}".format(
                    i, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 0.5
    if len(set(st_results)) == 1:
        points = 0
    print("Testing calculate_average_parking_fee() finished: {:.2f}/0.5 points".format(points))
    return points


def test_calculate_average_parking_time():
    print("Testing calculate_average_parking_time()...")
    with open("test_files/average_parking_times.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, corr_res) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = calculate_average_parking_time(records)
            st_results.append(st_res)

            if not isinstance(st_res, float):
                print("\tIncorrect return type. Expected float, got", type(st_res))
                gets_point = False
            elif abs(st_res - corr_res) > 1e-6:
                print("\tIncorrect return value for test {}. Expected {:.5f}, got {:.5f}".format(
                    i, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 0.5
    if len(set(st_results)) == 1:
        points = 0
    print("Testing calculate_average_parking_time() finished: {:.2f}/0.5 points".format(points))
    return points


def test_calculate_average_parking_stays():
    print("Testing calculate_average_stays()...")
    with open("test_files/average_parking_stays.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, corr_res) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = calculate_average_stays(records)
            st_results.append(st_res)

            if not isinstance(st_res, float):
                print("\tIncorrect return type. Expected float, got", type(st_res))
                gets_point = False
            elif abs(st_res - corr_res) > 1e-6:
                print("\tIncorrect return value for test {}. Expected {:.2f}, got {:.2f}".format(
                    i, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 0.5
    if len(set(st_results)) == 1:
        points = 0
    print("Testing calculate_average_stays finished: {:.2f}/0.5 points".format(points))
    return points


def test_get_most_common_region():
    print("Testing get_most_common_region()...")
    with open("test_files/most_common_regions.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, corr_res) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = get_most_common_region(records)
            st_results.append(st_res)

            if not isinstance(st_res, str):
                print("\tIncorrect return type. Expected str, got", type(st_res))
                gets_point = False
            elif st_res != corr_res:
                print("\tIncorrect return value for test {}. Expected {}, got {}".format(
                    i, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 1.0
    if len(set(st_results)) == 1:
        points = 0
    print("Testing get_most_common_region finished: {:.2f}/1.0 point".format(points))
    return points


def test_get_busiest_hour():
    print("Testing get_busiest_hour()...")
    with open("test_files/busiest_hours.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, corr_res) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = get_busiest_hour(records)
            st_results.append(st_res)

            if not isinstance(st_res, int):
                print("\tIncorrect return type. Expected int, got", type(st_res))
                gets_point = False
            elif st_res != corr_res:
                print("\tIncorrect return value for test {}. Expected {}, got {}".format(
                    i, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 0.5
    if len(set(st_results)) == 1:
        points = 0
    print("Testing get_busiest_hour finished: {:.2f}/0.5 points".format(points))
    return points


def test_get_max_number_of_cars():
    print("Testing get_max_number_of_cars()...")
    with open("test_files/max_numbers.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, corr_res, corr_lst) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = get_max_number_of_cars(records)
            st_results.append(st_res[0])

            if not isinstance(st_res, tuple):
                print("\tIncorrect return type. Expected multiple values, got", st_res)
                gets_point = False
            elif len(st_res) != 2:
                print("\tIncorrect return type. Expected two values, got", len(st_res))
                gets_point = False
            elif not isinstance(st_res[0], int):
                print("\tIncorrect return type. First value should be int, got", type(st_res[0]))
                gets_point = False
            elif not isinstance(st_res[1], list):
                print("\tIncorrect return type. Second value should be list, got", type(st_res[1]))
                gets_point = False
            else:
                st_max, st_lst = st_res
                if st_max != corr_res:
                    print("\tIncorrect return value for test {}. Expected {}, got {}".format(
                        i, corr_res, st_max))
                    gets_point = False
                if len(st_lst) != len(corr_lst):
                    print("\tIncorrect return value for test {}. Expected list of {} values, got {}".format(
                        i, len(corr_lst), len(st_lst)))
                    gets_point = False
                else:
                    for check_idx in range(len(corr_lst)):
                        if st_lst[check_idx] != corr_lst[check_idx]:
                            print("Incorrectly calculated car numbers at timestep {} (test {}). Expected {}, got {}".format(
                                check_idx, i, corr_lst[check_idx], st_lst[check_idx]))
                            gets_point = False
                if max(st_lst) != st_max:
                    print("\tIncorrect return value for test {}. Does not return maximum value from list".format(i))
                    gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 2.0
    if len(set(st_results)) == 1:
        points = 0
    print("Testing get_max_number_of_cars finished: {:.2f}/2.0 points".format(points))
    return points


def test_optimize_hourly_fee():
    print("Testing optimize_hourly_fee()...")
    with open("test_files/optimal_fees.pkl", 'rb') as infile:
        correct = pickle.load(infile)

    passed = 0
    st_results = list()
    for i, (records, prices, corr_res) in enumerate(correct, start=1):
        try:
            gets_point = True
            st_res = optimize_hourly_fee(records, prices.copy())
            st_results.append(st_res)

            if not isinstance(st_res, float):
                print("\tIncorrect return type. Expected float, got", type(st_res))
                gets_point = False
            elif abs(st_res - corr_res) > 1e-6:
                print("\tIncorrect return value for test {}. Expected {:.2f}, got {:.2f}".format(
                    i, corr_res, st_res))
                gets_point = False
        except Exception:
            gets_point = False

        passed += gets_point

    points = (passed / len(correct)) * 2
    if len(set(st_results)) == 1:
        points = 0
    print("Testing optimize_hourly_fee() finished: {:.2f}/2.0 points".format(points))
    return points


def main():
    points = list()
    points.append(test_load_parking_records())
    print()

    points.append(test_load_prices())
    print()

    points.append(test_calculate_parking_time())
    print()

    points.append(test_get_parking_fee())
    print()

    points.append(test_calculate_average_parking_fee())
    print()

    points.append(test_calculate_average_parking_time())
    print()

    points.append(test_calculate_average_parking_stays())
    print()

    points.append(test_get_most_common_region())
    print()

    points.append(test_get_busiest_hour())
    print()

    points.append(test_get_max_number_of_cars())
    print()

    points.append(test_optimize_hourly_fee())
    print()

    print("TOTAL: {:.2f}/10 points".format(sum(points)))
    print()


if __name__ == '__main__':
    main()
