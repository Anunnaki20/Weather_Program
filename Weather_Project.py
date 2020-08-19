import matplotlib.pyplot as plt
import Data_Format_New as DF


def plotting_temp():
    """
    To plot the temperature data
    :return: None
    """
    period = int(input("Enter the period will use to Predict future temperatures: "))
    df = DF.data_frame(period)

    # First Sub plot
    fig, axes = plt.subplots(nrows = 3, ncols = 1, figsize=(15,10))
    df.plot(y="Actual Temp",ax=axes[0])
    df['Avg'][period:].plot(ax=axes[0])
    axes[0].set_title("Temperature readings over a whole month")
    axes[0].set_xlabel("Readings")
    axes[0].set_ylabel("Temperature (°C)")
    axes[0].legend(["Actual Temperature", "Predicted Temperature Using " + str(period) + " Hours"])

    # Second Sub plot
    df['Min'][period:].plot(ax=axes[1])
    df['Max'][period:].plot(ax=axes[1])
    axes[1].legend(["Minimum Temperature", "Maximum Temperature Using"])
    axes[1].set_title("Max And Min temperatures over a whole month")
    axes[1].set_xlabel("Readings")
    axes[1].set_ylabel("Temperature (°C)")

    # Third Sub plot
    plt.plot((df['Actual Temp'][period:] - df['Avg'][period:]))
    axes[2].legend(['Accuracy of the Predicted temperature'])
    axes[2].set_title("Temperature readings over a whole month")
    axes[2].set_xlabel("Readings")
    axes[2].set_ylabel("Temperature (°C)")
    plt.show()


if __name__ == '__main__':
    plotting_temp()
