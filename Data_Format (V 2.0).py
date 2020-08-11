import pandas as pd
import readcsv as RC


def sorted_data(weather_data_dict, time_dict):
    """
    The purpose is to combine all temps that correspond with their time.
    :param weather_data_dict: A dictionary of weather data
    :param time_dict: A dictionary of times in which each temp in the temp_dict correspond to
    :return: A dictionary with the hour being the keys and a list of temps that go with that hour being the values
    """
    assert len(weather_data_dict) == len(time_dict), "The dictionary's must be the same size"
    sorted_dict = dict()
    sorted_data_dict = {'Act': [], '24 hr': [], '48 hr': []}
    accurate_list = list()
    hour_24 = list()
    hour_48 = list()
    for key in time_dict:
        time_stamp = 0
        time_list = time_dict[key]
        weather_list = weather_data_dict[key]
        while time_stamp < 24:
            index = [g for g, h in enumerate(time_list) if h == time_stamp]
            if len(index) == 0:
                time_stamp += 1
            if index[0] == 0:
                accurate_list.append(weather_list[index[0]])
                hour_24.append(weather_list[index[1]])
            else:
                hour_24.append(weather_list[index[0]])
                hour_48.append(weather_list[index[1]])
            try:
                sorted_data_dict = sorted_dict[time_stamp]
            except KeyError:
                sorted_dict[time_stamp] = sorted_data_dict
            sorted_data_dict['Act'].extend(accurate_list)
            sorted_data_dict['24 hr'].extend(hour_24)
            sorted_data_dict['48 hr'].extend(hour_48)
            sorted_dict[time_stamp] = sorted_data_dict
            time_stamp += 1
            accurate_list = list()
            hour_24 = list()
            hour_48 = list()
            sorted_data_dict = {'Act': [], '24 hr': [], '48 hr': []}
    return sorted_dict


all_data = RC.read_weather()  # All of the data that is read from the read_weather function in readcsv file
all_time_data = RC.read_time(all_data[2])  # Gets the time data and puts it in 24 hour format
compared_values = sorted_data(all_data[0], all_time_data)
print(compared_values[16]['Act'])



