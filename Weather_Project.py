import readcsv as RC
import matplotlib.pyplot as plt
import Data_format as DF


def plotting_pred_vs_act():
    """
    To plot the actual temperature value and the predicted value (avg value) on the same graph
    :param pred_dict: A dictionary with the average temp values
    :param act_dict: A dictionary with the  actual temperature values
    :return: None
    """
    all_data = RC.read_weather()
    all_time_data = RC.read_time(all_data[2])
    compared_temps = DF.time_and_temp(all_data[0],all_time_data)
    act_dict = DF.actual_temp(all_data[0], all_time_data)
    period = 24 #int(input("Enter the time period that we will use for the predicted graph: "))
    act_temp_xaxis = list()
    act_temp_yaxis = list()
    pred_temp_xaxis = []
    count = 1
    while count != (period - 1):      # Used to make the pred axis's equal dimensions
        pred_temp_xaxis.append(0)
        count += 1
    pred_temp_xaxis.append(period)
    pred_temp_yaxis = list()
    pred_cache = dict()
    for i in act_dict:  # pust the data into the actual temp axis's
        act_temp_xaxis.append(i)
        act_temp_time_list = act_dict[i]
        act_temp_yaxis.append(act_temp_time_list[1])
        if i >= period:
            pred_temp_xaxis.append(i)
    for i in act_dict:      # loop used to data into the pred temp axis's
        average = list()
        act_temp_time_list = act_dict[i]    # Uses the time value from the actual data
        time = act_temp_time_list[0]
        pred_cache[time] = 1    # stores what day we are at for that time
        pred_dict = DF.day_temps(compared_temps, time, period)  # calls the day temps to get a dict with avg values
        value = pred_cache[time]    # gets the day number from the cache
        pred_average = pred_dict[value]     # Gets the dictionary from the day key
        average.append(pred_average['avg'])     # puts the average value in a list
        pred_cache[time] += 1   # adds a day to the cache
        pred_temp_yaxis.append(average)     # adds the average to the pred y-axis
    plt.plot(act_temp_xaxis, act_temp_yaxis)    # Plotting the actual temp values
    plt.plot(pred_temp_xaxis, pred_temp_yaxis)  # Plotting the pred temp values
    plt.legend(["Actual Temperature"])
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()


plotting_pred_vs_act()


