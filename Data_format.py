import readcsv as RC


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
    for i in time_dict:
        time_stamp = 0
        while time_stamp < 24:  # loops through all times in a day
            time_list = time_dict[i]
            temp_list = temp_dict[i]
            index = [g for g, h in enumerate(time_list) if h == time_stamp]
            if len(index) == 0:
                time_stamp += 1
            else:
                for y in index:
                    alist.append(temp_list[y])
                try:
                    compared_temps[time_stamp].extend(alist)
                except KeyError:
                    compared_temps[time_stamp] = alist
                time_stamp += 1
            alist = list()
    return compared_temps













