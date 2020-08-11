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
    # Create all the necessary dictionaries and lists
    sorted_dict = dict()
    sorted_data_dict = {'Act': [], '24 hr': [], '48 hr': []}
    accurate_list = list()
    hour_24 = list()
    hour_48 = list()
    for key in time_dict:   # loops through all lines in the file
        time_stamp = 0
        time_list = time_dict[key]  # Gets the weather data for that line
        weather_list = weather_data_dict[key]   # Gets the time data for that line
        while time_stamp < 24:  # Goes through 0-23 hours for each line
            index = [g for g, h in enumerate(time_list) if h == time_stamp]
            # Gets the index in the time_list for the given time.
            if len(index) == 0:  # Checks to make sure that the list is of indexes is not empty. Prevents errors
                time_stamp += 1
            if index[0] == 0:   # If the first index is 0 then it puts it in the appropriate lists
                accurate_list.append(weather_list[index[0]])
                hour_24.append(weather_list[index[1]])
            else:   # If the first index is not 0 then it puts it in the hour_24 and hour_48 list
                hour_24.append(weather_list[index[0]])
                hour_48.append(weather_list[index[1]])
            try:    # Checks to see if a key value has been created in the dictionary
                sorted_data_dict = sorted_dict[time_stamp]  # Grabs the nested dictionary for the time
            except KeyError:    # If not it sets the time to to the current sorted_data_dict
                sorted_dict[time_stamp] = sorted_data_dict
            sorted_data_dict['Act'].extend(accurate_list)   # Adds the values from the accurate list to the 'Act' value
            sorted_data_dict['24 hr'].extend(hour_24)   # Adds the values from the hour_24 to the '24 hr' value
            sorted_data_dict['48 hr'].extend(hour_48)   # Adds the values form the hour_48 to the '48 hr' value
            sorted_dict[time_stamp] = sorted_data_dict  # Assigns the time with the sorted_data_dict
            time_stamp += 1  # Ups the time counter by 1
            # Resets all the lists and sorted_data_dict
            accurate_list = list()
            hour_24 = list()
            hour_48 = list()
            sorted_data_dict = {'Act': [], '24 hr': [], '48 hr': []}
    return sorted_dict


# all_data = RC.read_weather()  # All of the data that is read from the read_weather function in readcsv file
# all_time_data = RC.read_time(all_data[2])  # Gets the time data and puts it in 24 hour format
# compared_values = sorted_data(all_data[0], all_time_data)
# print(len(compared_values[16]['48 hr']))

def volatility(sorted_dict, period):
    """
    To find the average, min, max of the data using either 24 or 48 hours.
    :param sorted_dict: A sorted dictionary with the 24hr list and the 48hr list
    :param period: The period of time you want to use for the min,max,avg. Either 24 or 48
    :return: The sorted_dict with a new key value pairs of 'Avg','Min','Max' for each hour
    """

