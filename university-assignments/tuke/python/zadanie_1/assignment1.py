# Zadanie 1 - Parkujeme

# Meno: Dmytro Varich
# Spolupráca: 
# Použité zdroje: 
# Čas potrebný na vypracovanie: niekoľko dní

def load_parking_records(file_path):  # 0.75b
    """
    Loads and returns parking records.
     - file_path: path to csv file with parking records
    Returns: list of tuples with number late, parking start hour and minute
             and parking end hour and minute.
    """
    # print("Test...\n")
    with open(file_path, 'r') as my_file:
        lines = my_file.readlines()

    tple = tuple(lines)
    # print(tple)
    my_tuple = tuple(item.rstrip() for item in tple)
    # print(my_tuple)

    subtuples = [tuple(substring.split(',')) for substring in my_tuple]
    # print(subtuples)

    # new_t = tuple(tuple(int(x) if x.isdigit() else x for x in sub) for sub in subtuples)
    # print(list(new_t))

    return list(tuple(tuple(int(x) if x.isdigit() else x for x in sub) for sub in subtuples))


def load_prices(file_path):  # 0.75b
    """
    Loads and returns parking pricing.
     - file_path: path to txt file with prices
    Returns: dictionary with prices for 30m, 1h, 3h, 6h, 1d, h+
    """
    with open(file_path, 'r', encoding='utf-8') as my_file:
        line = my_file.readlines()
    # print(line)

    # remove space in list /n
    my_list = list(elem.rstrip() for elem in line)
    # print(my_list)

    # separate time and price as two separate lists
    time = list(elem[elem.find(''): elem.find(':')] for elem in my_list)
    # print(time)
    price = list(elem[elem.find(': ') + 2:] for elem in my_list)

    # turn the price into a float data type
    price = [float(elem) for elem in price]
    # print(price)

    # make a dictionary out of them
    # time_and_time = zip(time, price)
    # print(dict(time_and_time))

    return dict(zip(time, price))


def calculate_parking_time(start_h, start_m, end_h, end_m):  # 0.5b
    """
    Calculates and returns the duration of parking in minutes
    based on start and end time.
    """

    # convert hours to minutes and add to the minutes that we have
    end_h = end_h * 60
    # print(end_h)

    start_h = start_h * 60
    # print(start_h)

    # subtract end_h - start_h
    if end_m > start_h:
        difference_min = end_m - start_m
    else:
        difference_min = start_m - end_m

    result = abs(end_h - start_h) - difference_min
    # print(result)

    return result


def get_parking_fee(time_in_minutes, prices):  # 1b
    """
    Calculates and returns the price of parking for a given amount
    of time based on pricing.
    """

    # if parking up to 15 minutes, then free of charge
    if time_in_minutes < 15:
        return 0.0
    elif time_in_minutes < 30:
        return prices.get('30m')
    elif time_in_minutes <= 60:
        return prices.get('1h')
    elif time_in_minutes == 180:
        return prices.get('3h')
    elif time_in_minutes == 360:
        return prices.get('6h')
    elif time_in_minutes == 1440:
        return prices.get('1d')

    dict_time = {
        "60": prices.get('1h'),
        "180": prices.get('3h'),
        "360": prices.get('6h'),
        "1440": prices.get('1d'),
        "h1": prices.get('h+')
    }
    range_time = [60, 180, 360, 1440]

    # Find range
    a = 0
    b = 0
    for i in range(0, len(range_time) - 1):
        # print(i, "-", i+1, "  ", range_time[i], "-", range_time[i+1])

        if range_time[i] < time_in_minutes < range_time[i + 1]:
            a = range_time[i]
            b = range_time[i + 1]
            break
        else:
            continue
    # print(a)
    # print(time_in_minutes)
    # print(b)

    # Calculate price
    time_in_minutes -= a
    # print(time_in_minutes)
    result = 0.0
    i = 0
    if time_in_minutes < 60:
        result = dict_time.get(str(a)) + prices.get('h+')
    else:
        while True:
            # print(i)
            if time_in_minutes < 60:
                result = dict_time.get(str(a)) + (i + 1) * prices.get('h+')
                break
            else:
                time_in_minutes -= 60
                i += 1

    # print(i)
    # print(result)
    # Comparison
    if result > dict_time.get(str(b)):
        # print(dict_time.get(str(b)))
        return dict_time.get(str(b))
    else:
        # print(result)
        return result


def calculate_average_parking_fee(records, prices):  # 0.5b
    """
    Calculates the average amount paid for parking during the day.
    """
    # print(records)
    # print(prices)

    counter = len(records)
    # print(counter)

    result = 0.0
    for value in records:
        result += get_parking_fee(calculate_parking_time(value[1], value[2], value[3], value[4]), prices)

    # print(result/counter)
    return result / counter


def calculate_average_parking_time(records):  # 0.5b
    """
    Calculates the average length of parking for the day.
    """
    counter = len(records)
    # print(counter)

    result = 0.0
    for value in records:
        result += calculate_parking_time(value[1], value[2], value[3], value[4])

    return result / counter


def calculate_average_stays(records):  # 0.5b
    """
    Calculates the average number a car was parked during the day.
    """
    # print(records)

    visits = {}
    total_visits = 0
    total_cars = 0
    for record in records:
        car, _, _, _, _ = record
        visits[car] = visits.get(car, 0) + 1
    # print(visits)
    for car in visits:
        total_visits += visits[car]
        total_cars += 1
        # print(total_visits, "-", total_cars, "->", car, ":", visits[car])
    # print(len(records))
    # print(total_visits, "-", total_cars)
    return total_visits / total_cars


def get_most_common_region(records):  # 1b
    """
    Returns the code of the most common region of cars parked during the day.
    """
    # print(records)
    # records = sorted(records)
    # print(records)

    new_list = [value[0][0:2] for value in records]
    # (new_list)

    # Create a dictionary and record the number of matching elements
    dict_number_car = {}
    for value in new_list:
        dict_number_car[value] = dict_number_car.get(value, 0) + 1
    # print(dict_number_car)

    max_key = max(dict_number_car, key=dict_number_car.get)
    # print(max_key)

    return max_key


def get_busiest_hour(records):  # 0.5b
    """
    Returns the hour when the most cars were parked at the parking lot.
    It considers cars that were parked before or at the given hour
    and stayed at the parking lot until or after the given hour.
    """
    # print(records)

    my_list = [i for value in records
               for i in range(value[1], value[3] + 1)]
    # print(my_list)

    dict_time = {}
    for value in my_list:
        dict_time[value] = dict_time.get(value, 0) + 1

    # print(dict_time)

    max_key = max(dict_time, key=dict_time.get)
    # print(max_key)

    return max_key


def get_max_number_of_cars(records):  # 2b
    """
    Returns the highest number of cars parked at the parking lot in a given
    minute.
    """

    # print(records)
    # print(len(records))

    my_list = [i for value in records
               for i in range(value[1] * 60 + value[2], value[3] * 60 + value[4])
               ]
    # print(my_list)

    dict_minute = {}

    # add start time
    # print("0 elem: ", my_list[0])
    start_time_list = []
    start_work = my_list[0]
    while start_work % 60:
        start_work -= 1
        start_time_list.append(start_work)
        # print(start_work)

    start_time_list.reverse()
    # print(start_time_list)

    for key in start_time_list:
        dict_minute[key] = 0

    # print(dict_minute)

    for value in my_list:
        dict_minute[value] = dict_minute.get(value, 0) + 1

    # print(dict_minute)

    dict_no_break_time = {}

    start_key = min(dict_minute.keys())
    end_key = max(dict_minute.keys())

    for key in range(start_key, end_key + 1):
        dict_no_break_time[key] = 0

    for key, value in dict_minute.items():
        if key in dict_no_break_time:
            dict_no_break_time[key] = value
    # print(dict_no_break_time)
    # print(max(dict_minute.values()))
    # print(len(dict_no_break_time))

    # add at the end of time
    # print("Max elem: ", max(my_list))
    end_time_list = []
    end_work = max(my_list)
    while end_work % 60:
        end_work += 1
        end_time_list.append(end_work)
        # print(end_work)
    # print(end_work)
    # difference = end_work-start_work-len(dict_no_break_time)
    # print(difference)
    # print(end_time_list)

    # print(dict_minute)

    list_parking_car = []

    for minute in dict_no_break_time.keys():
        list_parking_car.append(dict_no_break_time[minute])

    # for i in range(0, difference):
    #   list_parking_car.append(0)
    # print(len(dict_minute))
    # print(list_parking_car)
    # list_parking_car.pop()
    # print(len(list_parking_car))

    return max(dict_no_break_time.values()), list_parking_car


def optimize_hourly_fee(records, prices):  # 2b
    """
    Returns the fee of additional hours that will maximize income for
    the parking lot.
    """
    # print(calculate_average_parking_fee(records, prices))
    # prices['1h'] // 0.1 * 0.1
    # print(records)
    # print(prices)

    half_hour_price = prices['30m']
    hour_price = prices['1h']

    max_revenue = 0
    optimal_extra_fee = None

    for extra_fee in range(int(half_hour_price * 100), int(hour_price * 100), 10):
        extra_fee = extra_fee / 100.0
        total_revenue = 0
        for record in records:
            car_id, entry_hour, entry_minute, exit_hour, exit_minute = record
            total_parking_time = calculate_parking_time(entry_hour, entry_minute, exit_hour, exit_minute)
            total_parking_time_hours = total_parking_time // 60
            total_parking_time_minutes = total_parking_time % 60

            hourly_fee = prices['1h']
            half_hourly_fee = prices['30m']
            max_hourly_fee = prices['h+']

            # Calculate the parking fee for the first hour
            if total_parking_time <= 60:
                parking_fee = half_hourly_fee * (total_parking_time_minutes > 0) + hourly_fee
            else:
                parking_fee = hourly_fee + (total_parking_time_hours - 1) * max_hourly_fee + \
                              max_hourly_fee * (total_parking_time_minutes > 0)

            # Add the extra fee for the first hour
            parking_fee += extra_fee

            total_revenue += parking_fee

        if total_revenue > max_revenue:
            max_revenue = total_revenue
            optimal_extra_fee = extra_fee

    optimal_extra_fee = round(optimal_extra_fee * 10) / 10
    # print(optimal_extra_fee)
    return optimal_extra_fee


if __name__ == '__main__':
    path_1 = "C:\\Users\\admin\\Desktop\\pythonProject\\ZADANIE_1_PYTHON_TUKE\\samples\\parking_logs_01.csv"
    path_2 = "C:\\Users\\admin\\Desktop\\pythonProject\\ZADANIE_1_PYTHON_TUKE\\samples\\prices_01.txt"
    load_parking_records(path_1)
    load_prices(path_2)
    calculate_parking_time(7, 11, 18, 26)
    get_parking_fee(120, load_prices(path_2))
    calculate_average_parking_fee(load_parking_records(path_1), load_prices(path_2))
    calculate_average_stays(load_parking_records(path_1))
    get_most_common_region(load_parking_records(path_1))
    get_busiest_hour(load_parking_records(path_1))
    get_max_number_of_cars(load_parking_records(path_1))
    optimize_hourly_fee(load_parking_records(path_1), load_prices(path_2))