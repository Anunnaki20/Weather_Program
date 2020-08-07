import readcsv as RC
import matplotlib.pyplot as plt
import Data_format as DF


def plotting_temp():
    """
    To plot the temperature data
    :return: None
    """
    period = int(input("Enter the period will use to Predict future temperatures: "))
    df = DF.dataframe(period)
    avg_frame = df[df['Avg'] > 0]   # Gets only the data frame if it is greater than 0
    avg = avg_frame.iloc[:, 2]      # Gets only the average data of the data frame that is greater than 0
    df.plot(y = 'Act Temp')
    plt.plot(avg)
    plt.legend(["Actual Temperature", "Predicted Temperature Using "+str(period)+" Hours"])
    plt.title("Temperature readings over a whole month")
    plt.xlabel("Readings")
    plt.ylabel("Temperature (°C)")
    plt.show()


if __name__ == '__main__':
    plotting_temp()
