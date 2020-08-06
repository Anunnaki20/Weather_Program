import pandas as pd
import readcsv as RC


def time_and_temp(weather_data_dict, time_dict):
    """
    The purpose is to combine all temps that correspond with their time.
    :param weather_data_dict: A dictionary of temperatures
    :param time_dict: A dictionary of times in which each temp in the temp_dict correspond to
    :return: A dictionary with the hour being the keys and a list of temps that go with that hour being the values
    """
    assert len(weather_data_dict) == len(time_dict), "The dictionary's must be the same size"
    compared_temps = dict()
    alist = list()
    for i in time_dict:  # loops through the values in the dictionary
        time_stamp = 0
        while time_stamp < 24:  # loops through all times in a day
            time_list = time_dict[i]
            temp_list = weather_data_dict[i]
            index = [g for g, h in enumerate(time_list) if h == time_stamp]  # gets the index of the time values
            if len(index) == 0:
                time_stamp += 1
            else:
                for y in index:  # Uses the indexes of the time values to add the temps to the dictionary
                    alist.append(temp_list[y])
                try:
                    compared_temps[time_stamp].extend(alist)
                except KeyError:
                    compared_temps[time_stamp] = alist
                time_stamp += 1
            alist = list()
    return compared_temps


def actual_temp(weather_data_dict, time_dict):
    """
    The purpose is to get the actual weather data for all 808 readings.
    e.g. temp_dict = {1:[23, 25, 28, 22]} time_dict = {1:[14,15,16,17]}
    It would return {1:[14, 23]} as at 14:00 hours 23 is the most accurate temperature
    the 1 being the line form the file it was read from
    :param weather_data_dict: A dictionary of a list of temperatures
    :param time_dict: A dictionary of a list of times
    :return: A dictionary with the time and most accurate temp
    """
    assert len(weather_data_dict) == len(time_dict), "The dictionary's must be the same size"
    actual_temp_dict = dict()
    time_temp_list = list()
    for i in time_dict:
        time_list = time_dict[i]
        temp_list = weather_data_dict[i]
        time_temp_list.append(time_list[0])
        time_temp_list.append(temp_list[0])
        actual_temp_dict[i] = time_temp_list
        time_temp_list = list()
    return actual_temp_dict


def day_temps(compared_temps, time_of_day, period):
    """
    To organize the data for each hour into avg,min,max for what period you select hour data
    :param compared_temps: The dictionary of compared temps from the time and temp function
    :param time_of_day: The time of day ranging from 0-23
    :param period: The time period of temp values you want.
    :return: A dictionary with each day being the key and a another dictionary with avg, min, and max values
    """
    assert time_of_day < 24, "The time must be from 0-23"
    assert period > 0, "The time period must be greater than 0"
    assert type(time_of_day) is type(int()), "The time of day must be an integer"
    assert type(period) is type(int()), "The period must be an integer"
    volatility = dict()
    volatility_hour = dict()
    start_day = 0
    end_day = period
    days = 1
    temp_list = compared_temps[time_of_day]
    amount_temps = len(temp_list)
    while amount_temps != 0:
        one_day = temp_list[start_day:end_day]
        max_temp = max(one_day)
        min_temp = min(one_day)
        average_temp = sum(one_day) / len(one_day)
        volatility["max"] = max_temp
        volatility["min"] = min_temp
        volatility["avg"] = average_temp
        volatility_hour[days] = volatility
        volatility = dict()
        start_day += period
        end_day += period
        amount_temps -= len(one_day)
        days += 1
    return volatility_hour


def temp_dataframe():
    """
    The purpose is to put the data into a single panda data frame
    :return: The data frame with all the data organized
    """
    dataframe_dict = {}     # The dictionary that will be used to make the data frame
    day_cache = dict()  # Caches what day we are getting the avg,min,max data
    day_temps_cache = dict()        # Cache of the dictionary calculated from the day temp function
    axis_index = list()     # Will become the lines in the left column
    actual_temp_list = list()
    average_list = list()
    min_list = list()
    max_list = list()
    time_of_data = list()
    all_data = RC.read_weather()    # All of the data that is read from the read_weather function in readcsv file
    all_time_data = RC.read_time(all_data[2])
    compared_temps = time_and_temp(all_data[0], all_time_data)
    act_dict = actual_temp(all_data[0], all_time_data)
    period = 24     # The amount of time that we will take for the avg,min,max values for the day_temps function
    count = 1
    while count < period:      # Used add 0 to the beginning when no avg,min,max data can be calculated
        average_list.append(0)
        min_list.append(0)
        max_list.append(0)
        count += 1
    for i in act_dict:  # puts the data into the actual temp list
        axis_index.append(i)
        act_temp_time_list = act_dict[i]
        actual_temp_list.append(act_temp_time_list[1])
        time_of_data.append(act_temp_time_list[0])
        day_cache[act_temp_time_list[0]] = 0
        day_temps_cache[act_temp_time_list[0]] = 0
    for i in act_dict:
        act_temp_time_list = act_dict[i]
        time = act_temp_time_list[0]
        day_cache[time] += 1
        if day_temps_cache[time] == 0:
            day_temps_dict = day_temps(compared_temps, time, period)
            day_temps_cache[time] = day_temps_dict
        day = day_cache[time]
        day_temps_dict = day_temps_cache[time]
        day_dict = day_temps_dict[day]
        average_list.append(day_dict['avg'])
        min_list.append(day_dict['min'])
        max_list.append(day_dict['max'])
    dataframe_dict['Time'] = time_of_data
    dataframe_dict['Act Temp'] = actual_temp_list
    dataframe_dict['Avg'] = average_list[:808]
    dataframe_dict['Min'] = min_list[:808]
    dataframe_dict['Max'] = max_list[:808]
    dataframe = pd.DataFrame(dataframe_dict, axis_index)
    return dataframe


x = temp_dataframe()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(x)
# print(x.head(100))
# atest = {0:[1,2,5,5,8,23,3,3,37,23,24,26,7,6,23,6,57,5,2,34,12,9999,23,21,23,22,1,24,34,1,23,35,46,1,23,15,4,21,3,35,34,23,524,61,34,25,1,2,7,3,2,5,9,6,34,2,2,6,8,94,4]}
# print(day_temps(atest,0,24))
# 9999 is the 24th hour

