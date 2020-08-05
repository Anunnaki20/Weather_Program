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
    for i in time_dict:
        time_stamp = 0
        alist = list()
        while time_stamp < 24:  # loops through ever hour in the day.
            time_list = time_dict[i]
            temp_list = temp_dict[i]
            index = [g for g, h in enumerate(time_list) if h == time_stamp]
            for y in index:
                alist.append(temp_list[y])
            compared_temps[time_stamp] = alist
    return compared_temps


temp_dict = {1: [23, 21, 26]}
time_dict = {1: [0, 3, 0]}
print(time_and_temp(temp_dict, time_dict))












