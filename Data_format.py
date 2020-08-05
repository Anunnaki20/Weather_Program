

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
    It would return {14:23} as at 14:00 hours 23 is the most accurate temperature
    :param temp_dict: A dictionary of a list of temperatures
    :param time_dict: A dictionary of a list of times
    :return: A dictionary with the time and the closest temperature for that time
    """
    assert len(temp_dict) == len(time_dict), "The dictionary's must be the same size"
    actual_temp_dict = dict()
    for i in time_dict:
        time_list = time_dict[i]
        temp_list = temp_dict[i]
        actual_temp_dict[time_list[0]] = temp_list[0]
    return actual_temp_dict












