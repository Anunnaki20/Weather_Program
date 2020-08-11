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
    sorted_data_dict = {'Act': [], '24 hr temps': [], '48 hr temps': []}
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
            sorted_data_dict['24 hr temps'].extend(hour_24)   # Adds the values from the hour_24 to the '24 hr' value
            sorted_data_dict['48 hr temps'].extend(hour_48)   # Adds the values form the hour_48 to the '48 hr' value
            sorted_dict[time_stamp] = sorted_data_dict  # Assigns the time with the sorted_data_dict
            time_stamp += 1  # Ups the time counter by 1
            # Resets all the lists and sorted_data_dict
            accurate_list = list()
            hour_24 = list()
            hour_48 = list()
            sorted_data_dict = {'Act': [], '24 hr temps': [], '48 hr temps': []}
    return sorted_dict


# all_data = RC.read_weather()  # All of the data that is read from the read_weather function in readcsv file
# all_time_data = RC.read_time(all_data[2])  # Gets the time data and puts it in 24 hour format
# sorted_dict = sorted_data(all_data[0], all_time_data)
# print(len(sorted_dict[16]['48 hr']))


def volatility(sorted_dict, period):
    """
    To find the average, min, max of the data using either 24 or 48 hours.
    :param sorted_dict: A sorted dictionary with the 24hr list and the 48hr list
    :param period: The period of time you want to use for the min,max,avg. Either 24 or 48
    :return: None
    """
    for time in sorted_dict:
        # Creates the volatility lists with as many 0 as we have period. As we do not have the data for any time before
        # the period.
        multi = 1
        if period == 48:
            multi = 2
        avg_list = [0] * multi
        max_list = [0] * multi
        min_list = [0] * multi
        temporarily_list = []
        # Checks on which data to access from the sorted_dict
        if period == 24:
            data = sorted_dict[time]['24 hr temps']  # Gets the all data from the 24 hours
            copy = sorted_dict[time]['24 hr temps'].copy()  # Copy's the 24 data
        if period == 48:
            data = sorted_dict[time]['48 hr temps']  # Gets the all data from the 48 hours
            copy = sorted_dict[time]['48 hr temps'].copy()  # Copy's the 48 data
        while len(data) != 0:
            if len(data) <= 24:  # Checks to make sure it can pop 24 values into the temporarily list
                temporarily_list = data  # If it can't pop 24 values then it assigns the values to temporarily list
                break   # Breaks the while loop so it can find the min, max, avg from the remaining values
            else:
                for i in range(0, 24):  # pops in 24 values from the data list
                    value = data.pop(0)
                    temporarily_list.append(value)  # Adds the value to the temporarily list
            min_list.append(min(temporarily_list))  # Finds the min value and adds it to the min list
            max_list.append(max(temporarily_list))  # Finds the max value and adds it to the max list
            # Finds the avg value and adds it to the avg list
            avg_list.append((sum(temporarily_list) / len(temporarily_list)))
            temporarily_list = []   # Resets the temporarily list
            sorted_dict[time]['Avg'] = avg_list  # Adds the avg list to a key value pair in the sorted dict
            sorted_dict[time]['Min'] = min_list  # Adds the min list to a key value pair in the sorted dict
            sorted_dict[time]['Max'] = max_list  # Adds the max list to a key value pair in the sorted dict
        if period == 24:
            sorted_dict[time]['24 hr temps'] = copy  # Places the 24 hour list back
        if period == 48:
            sorted_dict[time]['48 hr temps'] = copy  # Places the 48 hour list back


def data_frame(period):
    """
    The purpose is to put the data into a single panda data frame
    :param: period: The period of time that we will take avg,min,max data
    :return: The data frame with all the data organized
    """
    all_data = RC.read_weather()  # All of the data that is read from the read_weather function in readcsv file
    all_time_data = RC.read_time(all_data[2])  # Gets the time data and puts it in 24 hour format
    sorted_dict = sorted_data(all_data[0], all_time_data)
    volatility(sorted_dict, period)
    # The dictionary that will be used to make the data frame
    dataframe_dict = {'Time': [], 'Actual Temp': [], 'Avg': [], 'Min': [], 'Max': []}
    axis_index = list()  # Will become the lines in the left column
    for line in all_time_data:  # Loops through every line from the file
        axis_index.append(line)  # Puts the number of lines in a list. in ascending order
        time = all_time_data[line][0]   # Finds the first time values from each line
        volatility_data = sorted_dict[time]
        dataframe_dict['Time'].append(time)  # Adds the first time in each line into a list
        dataframe_dict['Actual Temp'].append(volatility_data['Act'].pop(0))
        dataframe_dict['Avg'].append(volatility_data['Avg'].pop(0))
        dataframe_dict['Min'].append(volatility_data['Min'].pop(0))
        dataframe_dict['Max'].append(volatility_data['Max'].pop(0))
    dataframe = pd.DataFrame(dataframe_dict, axis_index)
    return dataframe


x = data_frame(48)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(x)
