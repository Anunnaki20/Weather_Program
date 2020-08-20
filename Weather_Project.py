import matplotlib.pyplot as plt
import Data_Format_New as DF
import readcsv as RC
import pandas as pd
import plotly as pl

def plotting(dataframe, data_type):
    """
    To plot the temperature data
    :param: dataframe: The dataframe produced by the data_from function in Data_Format_New
    :param: data_type: A string unit of the type of data we want to graph. Can be 'Temperature', 'Pressure', 'Humidity'
    :return: None
    """
    df = dataframe
    unit = {'Temperature': " (°C)", "Pressure": " (hPa)", "Humidity": ""}
    # First Sub plot
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))
    df.plot(y="Actual", ax=axes[0])
    df['Avg'][period:].plot(ax=axes[0])
    axes[0].legend(["Actual " + data_type, "Predicted" + data_type + " Using " + str(period) + " Hours"])
    axes[0].set_title(data_type + " readings over a whole month")
    axes[0].set_xlabel("Readings")
    axes[0].set_ylabel(data_type + unit[data_type])

    # Second Sub plot
    df['Min'][period:].plot(ax=axes[1])
    df['Max'][period:].plot(ax=axes[1])
    axes[1].legend(["Minimum " + data_type, "Maximum " + data_type])
    axes[1].set_title("Max And Min " + data_type + " over a whole month")
    axes[1].set_xlabel("Readings")
    axes[1].set_ylabel(data_type + unit[data_type])

    # Third Sub plot
    plt.plot((abs(df['Avg'][period:] - df['Actual'][period:])/df['Actual'][period:]) * 100)
    axes[2].legend(['% Error of the Predicted ' + data_type])
    axes[2].set_title(data_type + " readings over a whole month")
    axes[2].set_xlabel("Readings")
    axes[2].set_ylabel("% Error")
    plt.show()


if __name__ == '__main__':
    weather = RC.read_weather()
    period = int(input("Enter the period will use to Predict future temperatures. Can choose between 24 or 48: "))
    # Plots temperature
    # temp_data = DF.data_frame(period, weather, 'Temperature')
    # plotting(temp_data, 'Temperature')
    # Plots Pressure
    # pressure_data = DF.data_frame(period, weather, 'Pressure')
    # plotting(pressure_data, 'Pressure')
    # Plots Humidity
    humidity_data = DF.data_frame(period, weather, 'Humidity')
    plotting(humidity_data, 'Humidity')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(humidity_data)
