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
    compared_values = dict()
    alist = list()
    for i in time_dict:  # loops through the values in the dictionary
        time_stamp = 0
        while time_stamp < 24:  # loops through all times in a day
            time_list = time_dict[i]
            temp_list = weather_data_dict[i]
            index = [g for g, h in enumerate(time_list) if h == time_stamp]  # gets the index of the time values
            if len(index) == 0:  # If the current time is not found it ups the time by 1
                time_stamp += 1
            else:
                for y in index:  # Uses the indexes of the time values to add the temps to the dictionary
                    alist.append(temp_list[y])
                try:
                    compared_values[time_stamp].extend(alist)
                except KeyError:
                    compared_values[time_stamp] = alist
                time_stamp += 1
            alist = list()
    return compared_values


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
    actual_value_dict = dict()
    time_temp_list = list()
    for i in time_dict:
        if i == 428:
            s = 687897
        time_list = time_dict[i]  # Gets the time list from the dictionary
        temp_list = weather_data_dict[i]  # Gets the weather data from the dictionary
        time_temp_list.append(time_list[0])  # adds the time to a list
        time_temp_list.append(temp_list[0])  # Adds the most accurate temp to the list
        actual_value_dict[i] = time_temp_list  # Adds the list of time and weather data to the dictionary
        time_temp_list = list()  # Resets the list
    return actual_value_dict


def day_temps(compared_values, hour, period):
    """
    To organize the data for each hour into avg,min,max for what period you select hour data
    :param compared_values: The dictionary of compared temps from the time and temp function
    :param hour: The time of day ranging from 0-23
    :param period: The time period of temp values you want.
    :return: A dictionary with each day being the key and a another dictionary with avg, min, and max values
    """
    assert hour < 24, "The time must be from 0-23"
    assert period == 48 or period == 24, "The time period must be less than 48"
    assert type(hour) is type(int()), "The time of day must be an integer"
    assert type(period) is type(int()), "The period must be an integer"
    volatility = dict()
    volatility_hour = dict()
    temps_24_hour = list()
    days = 1
    temp_list = compared_values[hour]
    time_frame = 48
    temp_list = temp_list[1:]  # Gets the list of temperatures for the hour excludes the most accurate temp
    while len(temp_list) > 0:
        if period == 24:
            temps_24_hour.append(temp_list.pop(0))
            # pops the first item in the list to correct for the duel 24 hr temps
            temps_24_hour.extend(temp_list[:time_frame - 1:2])  # Adds all 24 hour values from a single day in a list
            max_temp = max(temps_24_hour)
            min_temp = min(temps_24_hour)
            average_temp = sum(temps_24_hour) / len(temps_24_hour)
        elif period == 48:
            temp_list.pop(0)  # Removes the first value in the list to correct for the duel 24 hr
            temps_48_hour = temp_list[1:time_frame - 1:2]  # Gets all 48 hr values from a single day
            max_temp = max(temps_48_hour)
            min_temp = min(temps_48_hour)
            average_temp = sum(temps_48_hour) / len(temps_48_hour)
        volatility["max"] = max_temp
        volatility["min"] = min_temp
        volatility["avg"] = average_temp
        volatility_hour[days] = volatility  # puts the dictionary max,min,avg dictionary in another dictionary
        temps_24_hour = list()
        volatility = dict()
        temp_list = temp_list[time_frame - 1:]
        # moves the temp_list by 48 values. Does not include the most accurate temp
        days += 1
    return volatility_hour


def temp_dataframe(period):
    """
    The purpose is to put the data into a single panda data frame
    :param: period: The period of time that we will take avg,min,max data
    :return: The data frame with all the data organized
    """
    dataframe_dict = {}  # The dictionary that will be used to make the data frame
    day_cache = dict()  # Caches what day we are getting the avg,min,max data
    volatility_hour_cache = dict()  # Cache of the dictionary calculated from the day temp function
    axis_index = list()  # Will become the lines in the left column
    actual_value_list = list()  # A list of the most accurate value
    average_list = [0] * period  # A list of the average values over the period of time selected
    min_list = [0] * period  # A list of the min values over the period of time selected
    max_list = [0] * period  # A list of the max values over the period of time selected
    time_of_data = list()  # The time at which the value is for. In 24 hour format
    all_data = RC.read_weather()  # All of the data that is read from the read_weather function in readcsv file
    all_time_data = RC.read_time(all_data[2])  # Gets the time data and puts it in 24 hour format
    compared_values = time_and_temp(all_data[0], all_time_data)
    act_dict = actual_temp(all_data[0], all_time_data)
    for i in act_dict:  # puts the data into the actual temp list
        axis_index.append(i)
        act_value_time_list = act_dict[i]
        actual_value_list.append(act_value_time_list[1])
        time_of_data.append(act_value_time_list[0])
        day_cache[act_value_time_list[0]] = 0  # initiates the caches
        volatility_hour_cache[act_value_time_list[0]] = 0
    count_hour = 16
    for i in act_dict:  # Loop for putting the avg,min,max data into lists to then by put in the data frame dictionary
        if i > period:  # Prevents having a list of different sizes
            act_value_time_list = act_dict[i]
            time = act_value_time_list[0]
            if count_hour > 23:
                count_hour = 0
            if count_hour < time:
                day_cache[count_hour] += 1
                count_hour = time
            day_cache[count_hour] += 1
            if volatility_hour_cache[time] == 0:  # Check to make sure that day_temp() has not been called for that hour
                volatility_dict = day_temps(compared_values, time, period)  # Calls day_temp()
                volatility_hour_cache[time] = volatility_dict  # Adds the return values to the cache.
            day = day_cache[time]  # Gets the day from the day_cache for use in getting the avg,min,max
            volatility_dict = volatility_hour_cache[time]
            if day <= len(volatility_dict):
                volatility_value_dict = volatility_dict[day]
                average_list.append(volatility_value_dict['avg'])
                min_list.append(volatility_value_dict['min'])
                max_list.append(volatility_value_dict['max'])
            if i == 30:  # Debugging only remove when complete
                pass
            count_hour += 1
    dataframe_dict['Time'] = time_of_data
    dataframe_dict['Act Temp'] = actual_value_list
    dataframe_dict['Avg'] = average_list
    dataframe_dict['Min'] = min_list
    dataframe_dict['Max'] = max_list
    dataframe = pd.DataFrame(dataframe_dict, axis_index)
    return dataframe


x = temp_dataframe(48)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(x)
# print(x.iloc[:,4])
