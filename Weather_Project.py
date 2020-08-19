import matplotlib.pyplot as plt
import Data_Format_New as DF
import readcsv as RC


def plotting(dataframe, data_type):
    """
    To plot the temperature data
    :return: None
    """

    df = dataframe
    value = {'Temperature': " (°C)", "Pressure": " (hPa)", "Humidity": ""}
    # First Sub plot
    fig, axes = plt.subplots(nrows = 3, ncols = 1, figsize=(15,10))
    df.plot(y="Actual", ax=axes[0])
    df['Avg'][period:].plot(ax=axes[0])
    axes[0].set_title(data_type + " readings over a whole month")
    axes[0].set_xlabel("Readings")
    axes[0].set_ylabel(data_type + value[data_type])
    axes[0].legend(["Actual " + data_type, "Predicted" + data_type + " Using " + str(period) + " Hours"])

    # Second Sub plot
    df['Min'][period:].plot(ax=axes[1])
    df['Max'][period:].plot(ax=axes[1])
    axes[1].legend(["Minimum " + data_type, "Maximum " + data_type])
    axes[1].set_title("Max And Min " + data_type + " over a whole month")
    axes[1].set_xlabel("Readings")
    axes[1].set_ylabel(data_type + value[data_type])

    # Third Sub plot
    plt.plot((abs(df['Avg'][period:] - df['Actual'][period:])/df['Actual'][period:]) * 100)
    axes[2].legend(['% Error of the Predicted ' + data_type])
    axes[2].set_title(data_type + " readings over a whole month")
    axes[2].set_xlabel("Readings")
    axes[2].set_ylabel("% Error")
    plt.show()


if __name__ == '__main__':
    weather = RC.read_weather()
    period = int(input("Enter the period will use to Predict future temperatures: "))
    temp_data = DF.data_frame(period, weather, 'Temperature')
    plotting(temp_data, 'Temperature')
    pressure_data = DF.data_frame(period, weather, 'Pressure')
    plotting(pressure_data, 'Pressure')
    humidity_data = DF.data_frame(period, weather, 'Humidity')
    plotting(humidity_data, 'Humidity')
