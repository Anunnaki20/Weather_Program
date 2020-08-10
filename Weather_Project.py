import matplotlib.pyplot as plt
import Data_format as DF


def plotting_temp():
    """
    To plot the temperature data
    :return: None
    """
    period = int(input("Enter the period will use to Predict future temperatures: "))
    df = DF.temp_dataframe(period)
    avg_frame = df[df['Avg'] > 0]   # Gets only the data frame if it is greater than 0
    avg = avg_frame.iloc[:, 2]
    df.plot(y='Act Temp')
    plt.plot(avg)
    plt.legend(["Actual Temperature", "Predicted Temperature Using "+str(period)+" Hours"])
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()

    min_temp = avg_frame.iloc[:, 3]
    max_temp = avg_frame.iloc[:, 4]
    # df.plot(y='Act Temp')
    plt.plot(min_temp)
    plt.plot(max_temp)
    plt.legend(["Actual Temperature " + str(period) + " Hours", "Minimum Temperature", "Maximum Temperature Using"])
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()

    actual = df[df['Act Temp'] > 0]
    actual_temps = avg_frame.iloc[:, 1]
    plt.plot((actual_temps- avg))
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()


if __name__ == '__main__':
    plotting_temp()
