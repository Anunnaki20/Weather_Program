import json
import datetime as DT
import pytz
eastern = pytz.timezone('US/Eastern')


def read_weather():
    temp1 = {}
    temp2 = {}
    time = {}

    with open('forecast.txt', 'r') as f:
        linenum = 1
        fl = f.readlines()
        #print(fl[0])

        for line in fl:
            # parse out the number and the comma
            data = line.split('{')
            jsondata = "{" + data[1].strip()
            #print(jsondata)

            # convert to dictionary for this hours data
            datadict = json.loads(jsondata)
            #print(datadict['temperature'])

            # store the temperature data for this hour, all 48 values, in a new dict
            temp1[linenum] = datadict['temperature']
            time[linenum] = datadict['validTimeUtc']
            linenum += 1
            temp2[datadict['responseTime']] = datadict['temperature']

    return temp1, temp2, time

# so now we have a dictonary in the format
# { 1: [23, 21, ... 24], 2: [20, 19, ... 17], ... 800: [26, 27, ... 25]}
# Where 1: is a label for the hour
# and [] is a list of 48 temperatures
# print(temp1[1])   # for hour 1
# print(temp1[800]) # for hour 800
#
# print(temp2)

# x = read_weather()
# print(x[0])     # Prints temp1
# print(x[2])
# y= DT.datetime.utcfromtimestamp(1593633600)
# time = int(f"{y:%H}")
# print(time)

def read_time(adict):
    """
    returns a list of times from a POSIX time code. The times are in EST time zone
    :param adict: a dictionary of POSIX time codes
    :return: A dict of times in EST time zone that correspond to the readings from the temp
    """
    linenum = 1
    temp_time = dict()
    for i in adict:
        hour = list()
        for j in range(len(adict[i])):
            utctime = DT.datetime.fromtimestamp(adict[i][j],eastern)
            # Gets date and time from POSIX sets time zone to eastern
            temp_time[linenum] = hour
            hour.append(int(f"{utctime:%H}"))  # Grabs just the hour in 24 hour format
        linenum += 1
    return temp_time

x = read_weather()
print(len(x[2][1]))
y = read_time(x[2])
print(y[1])
