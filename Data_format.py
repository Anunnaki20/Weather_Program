import math as m


def time_and_temp(temp_dict, time_dict):
    """
    The purpose is to combine all temps that correspond with their time.
    :param temp_dict: A dictionary of temperatures
    :param time_dict: A dictionary of times in which each temp in the temp_dict correspond to
    :return: A dictionary with the hour being the keys and a list of temps that go with that hour being the values
    """
    assert len(temp_dict) == len(time_dict), "The dictionary's must be the same size"
    compared_temps = dict()
    alist = list()
    for i in time_dict:     # loops through the values in the dictionary
        time_stamp = 0
        while time_stamp < 24:  # loops through all times in a day
            time_list = time_dict[i]
            temp_list = temp_dict[i]
            index = [g for g, h in enumerate(time_list) if h == time_stamp]  # gets the index of the time values
            if len(index) == 0:
                time_stamp += 1
            else:
                for y in index:     # Uses the indexes of the time values to add the temps to the dictionary
                    alist.append(temp_list[y])
                try:
                    compared_temps[time_stamp].extend(alist)
                except KeyError:
                    compared_temps[time_stamp] = alist
                time_stamp += 1
            alist = list()
    return compared_temps


def actual_temp(temp_dict, time_dict):
    """
    The purpose is to get the actual temp for all 808 readings.
    e.g. temp_dict = {1:[23, 25, 28, 22]} time_dict = {1:[14,15,16,17]}
    It would return {1:[14, 23]} as at 14:00 hours 23 is the most accurate temperature
    :param temp_dict: A dictionary of a list of temperatures
    :param time_dict: A dictionary of a list of times
    :return: A dictionary with the time and most accurate temp
    """
    assert len(temp_dict) == len(time_dict), "The dictionary's must be the same size"
    actual_temp_dict = dict()
    time_temp_list = list()
    for i in time_dict:
        time_list = time_dict[i]
        temp_list = temp_dict[i]
        time_temp_list.append(time_list[0])
        time_temp_list.append(temp_list[0])
        actual_temp_dict[i] = time_temp_list
        time_temp_list = list()
    return actual_temp_dict


def one_day_temps(compared_temps):
    """
    To organize the data for each hour into 24 hour data
    :param compared_temps: The dictionary of compared temps from the time and temp function
    :return: A dictionary with each day being the key and a another dictionary with avg, min, and max values
    """
    volatility = dict()
    volatility_hour = dict()
    for i in compared_temps:
        start_day = 0
        end_day = 24
        days = 0
        temp_list = compared_temps[i]
        amount_temps = len(temp_list)
        while amount_temps != 0:
            one_day = temp_list[start_day:end_day]
            print(one_day[-1])
            max_temp = max(one_day)
            min_temp = min(one_day)
            average_temp = sum(one_day)/ len(one_day)
            volatility["max"] = max_temp
            volatility["min"] = min_temp
            volatility["avg"] = average_temp
            volatility_hour[days] = volatility
            volatility = dict()
            start_day += 24
            end_day += 24
            days += 1
            amount_temps -= len(one_day)
    return volatility_hour

# atest = {0:[1,2,5,5,8,23,3,3,37,23,24,26,7,6,23,6,57,5,2,34,12,9999,23,21,23,22,1,24]}
# print(one_day_temps(atest))
# 9999 is the 24th hour












