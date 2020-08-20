import matplotlib.pyplot as plt
import Data_Format_New as DF
import readcsv as RC
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plotting(dataframe, data_type,period):
    """
    To plot the temperature data
    :param: dataframe: The dataframe produced by the data_from function in Data_Format_New
    :param: data_type: A string unit of the type of data we want to graph. Can be 'Temperature', 'Pressure', 'Humidity'
    :return: None
    """
    pd.options.plotting.backend = "matplotlib"
    df = dataframe[0]
    unit = {'Temperature': " (°C)", "Pressure": " (hPa)", "Humidity": ""}
    # First Sub plot
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))
    df['Actual'].plot(ax=axes[0])
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


def interactive_plots(dataframe, data_type,period):
    """
    To plot the temperature data with plotly
    :param: dataframe: The dataframe produced by the data_from function in Data_Format_New
    :param: data_type: A string unit of the type of data we want to graph. Can be 'Temperature', 'Pressure', 'Humidity'
    :return: None
    """
    df = dataframe[0]
    index = dataframe[1]
    unit = {'Temperature': " (°C)", "Pressure": " (hPa)", "Humidity": ""}
    pd.options.plotting.backend = "plotly"
    # Makes the subplots
    fig = make_subplots(rows=4, cols=1, subplot_titles=(data_type, "Min and Max " + data_type, "% Error"))
    # Graphs all plots in the proper location
    fig.add_trace(go.Scatter(x=index, y=df['Actual'], name="Actual " + data_type), row=1, col=1)
    fig.add_trace(go.Scatter(x=index[period:], y=df['Avg'][period:], name='Average'), row=1, col=1)
    fig.add_trace(go.Scatter(x=index[period:], y=df['Min'][period:], name="Min " + data_type), row=2, col=1)
    fig.add_trace(go.Scatter(x=index[period:], y=df['Max'][period:], name='Max ' + data_type), row=2, col=1)
    fig.add_trace(go.Scatter(x=index[period:],
                             y=((abs(df['Avg'][period:] - df['Actual'][period:])/df['Actual'][period:]) * 100),
                             name='% Error'),
                  row=3, col=1)
    # Updates the axis labels and sets the size of the graphs
    fig.update_xaxes(title_text="Readings", row=1, col=1)
    fig.update_xaxes(title_text="Readings", row=2, col=1)
    fig.update_xaxes(title_text="Readings", row=3, col=1)
    fig.update_yaxes(title_text=data_type + unit[data_type], row=1, col=1)
    fig.update_yaxes(title_text=data_type + unit[data_type], row=2, col=1)
    fig.update_yaxes(title_text='%Error', row=3, col=1)
    fig.update_layout(height=900, title_text=data_type + " over a whole month using " + str(period) + " data")
    fig.show()


def main():
    period = int(input("Enter the period will use to Predict future temperatures. Can choose between 24 or 48: "))
    while period != 24 and period != 48:
        period = int(input("The period must be either 24 or 48: "))
    # Plots temperature
    temp_data = DF.data_frame(period, weather, 'Temperature')
    plotting(temp_data, 'Temperature', period)
    # Plots Pressure
    pressure_data = DF.data_frame(period, weather, 'Pressure')
    plotting(pressure_data, 'Pressure', period)
    # Plots Humidity
    humidity_data = DF.data_frame(period, weather, 'Humidity')
    plotting(humidity_data, 'Humidity', period)
    # Plots the Interactive charts
    temp_data = DF.data_frame(period, weather, 'Temperature')
    interactive_plots(temp_data, 'Temperature', period)
    pressure_data = DF.data_frame(period, weather, 'Pressure')
    interactive_plots(pressure_data, 'Pressure', period)
    humidity_data = DF.data_frame(period, weather, 'Humidity')
    interactive_plots(humidity_data, 'Humidity', period)


if __name__ == '__main__':
    exit_input = 'Y'
    weather = RC.read_weather()
    while exit_input != 'N':
        main()
        exit_input = str(input("Do you want to graph again? (Yes: Y, No: N): "))
