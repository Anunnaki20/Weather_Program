import json

def read_weather():
    temp1 = {}
    temp2 = {}

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
            linenum += 1
            temp2[datadict['responseTime']] = datadict['temperature']
    return 

# so now we have a dictonary in the format
# { 1: [23, 21, ... 24], 2: [20, 19, ... 17], ... 800: [26, 27, ... 25]}
# Where 1: is a label for the hour
# and [] is a list of 48 temperatures
# print(temp1[1])   # for hour 1
# print(temp1[800]) # for hour 800
#
# print(temp2)

