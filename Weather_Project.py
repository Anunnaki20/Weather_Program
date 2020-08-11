import matplotlib.pyplot as plt
import Data_Format_New as DF


def plotting_temp():
    """
    To plot the temperature data
    :return: None
    """
    period = int(input("Enter the period will use to Predict future temperatures: "))
    df = DF.data_frame(period)
    avg_frame = df['Avg']   # Gets only the data frame if it is greater than 0
    avg_frame = avg_frame[period:]
    print(avg_frame)
    df.plot(y='Actual Temp')
    plt.plot(avg_frame)
    plt.legend(["Actual Temperature", "Predicted Temperature Using "+str(period)+" Hours"])
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()

    min_temp = df['Min']
    min_temp = min_temp[period:]
    max_temp = df['Max']
    max_temp = max_temp[period:]
    # df.plot(y='Act Temp')
    plt.plot(min_temp)
    plt.plot(max_temp)
    plt.legend(["Actual Temperature " + str(period) + " Hours", "Minimum Temperature", "Maximum Temperature Using"])
    plt.title("Max And Min temperatures over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()

    actual_temps = df['Actual Temp']
    actual_temps = actual_temps[period:]
    plt.plot((actual_temps - avg_frame))
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()


if __name__ == '__main__':
    plotting_temp()
