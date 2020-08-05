import datetime as DT
import readcsv as RC
from Data_format import time_and_temp
from Data_format import actual_temp
from Data_format import day_temps

def str_form(obj, result, expected, reason):
    """
    Purpose:
        Produce a string for information about a failed test case.
        Abbreviates test case assertions somewhat.
    Preconditions:
        :param obj:  a string describing the objective of the test (a function or method name)
        :param result: a value: the actual result of using the objective
        :param expected: a value: the intended or expected result of using the objective
        :param reason: a string describing the purpose of the test
    Return:
        :return: a string
    """
    return 'Test fault for {}.  Returned <{}>, expected <{}>.  Reason: "{}"'.format(obj, result, expected, reason)


# Testing read_time function
def test_1():
    objective = "read_time()"
    reason = "The function is not converting the time correctly, check the math"
    adict = {1:[1593633600]}
    result = RC.read_time(adict)
    time = DT.datetime.utcfromtimestamp(1593633600)
    expected = [int(f"{time:%H}") - 4]
    assert result[1] == expected, str_form(objective,result,expected,reason)


def test_2():
    objective = "read_time()"
    reason = "The function is not converting the time correctly, check the math"
    adict = {1: [1593633600,1593637200]}
    result = RC.read_time(adict)
    expected = [16,17]
    assert result[1] == expected, str_form(objective, result, expected, reason)


def test_3():
    objective = "read_time()"
    reason = "The function is not converting the time correctly, check the math"
    adict = {1: [1593633600, 1593637200, 1593640800, 1593644400, 1593648000]}
    result = RC.read_time(adict)
    expected = [16, 17, 18, 19, 20]
    assert result[1] == expected, str_form(objective, result, expected, reason)


def test_4():
    objective = "read_time()"
    reason = "The function is not converting the time correctly, check the math"
    adict = {1: [1593633600, 1593637200, 1593640800, 1593644400, 1593648000, 1593651600, 1593655200, 1593658800,
                 1593662400, 1593666000, 1593669600, 1593673200, 1593676800, 1593680400]}
    result = RC.read_time(adict)
    expected = [16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5]
    assert result[1] == expected, str_form(objective, result, expected, reason)


# Testing the time_and_temp function in teh Data_format file
def test_5():
    objective = "time_and_temp()"
    reason = "The function is not placing the values in a dictionary properly"
    time_dict = {1: [12, 13, 16]}
    temp_dict = {1: [13, 16, 20]}
    expected = {12: [13], 13: [16], 16: [20]}
    result = time_and_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_6():
    objective = "time_and_temp()"
    reason = "The function is not adding the second values to the existing dictionary"
    time_dict = {1: [0, 1, 2], 2: [0, 1, 2]}
    temp_dict = {1: [10, 13, 16], 2: [12, 15, 17]}
    expected = {0: [10, 12], 1: [13, 15], 2: [16, 17]}
    result = time_and_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_7():
    objective = "time_and_temp()"
    reason = "The function is not getting the time indexes correctly"
    time_dict = {1: [1, 1, 1], 2: [1, 1, 1]}
    temp_dict = {1: [10, 13, 16], 2: [12, 15, 17]}
    expected = {1: [10, 13, 16, 12, 15, 17]}
    result = time_and_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_8():
    objective = "time_and_temp()"
    reason = "The function is not adding the temps to the lists correctly"
    time_dict = {1: [1, 5, 1], 2: [5, 23, 1]}
    temp_dict = {1: [24, 30, 25], 2: [28, 15, 13]}
    expected = {1: [24, 25, 13], 5: [30, 28], 23: [15]}
    result = time_and_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_9():
    objective = "time_and_temp()"
    reason = "The function is not adding the temps to the lists correctly"
    time_dict = {1: [16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                     19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}
    temp_dict = {1: [27, 27, 26, 25, 24, 22, 20, 19, 19, 18, 18, 17, 17, 17, 17, 18, 21, 24, 26, 27, 28, 29, 29, 30, 30,
                     29, 28, 28, 26, 24, 23, 21, 21, 20, 20, 19, 19, 18, 19, 20, 22, 24, 25, 26, 26, 26, 27, 27]}
    expected = {0:[19,21], 1:[18,20], 2:[18,20], 3:[17,19], 4:[17,19], 5:[17,18], 6:[17,19], 7:[18,20], 8:[21,22],
               9:[24,24], 10:[26,25], 11:[27,26], 12:[28,26], 13:[29,26], 14:[29,27], 15:[30,27], 16:[27,30], 17:[27,29]
                , 18:[26,28], 19:[25,28], 20:[24,26], 21:[22,24], 22:[20,23], 23:[19, 21]}
    result = time_and_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_10():
    objective = "time_and_temp()"
    reason = "The function is not working correctly"
    x = RC.read_weather()
    time_dict = RC.read_time(x[2])
    temp_dict = x[0]
    expected = time_and_temp(temp_dict, time_dict)
    result = time_and_temp(temp_dict, time_dict)
    print(result)
    assert result == expected, str_form(objective, result, expected, reason)


# Testing the actual_temp() in the Data_format file
def test_11():
    objective = "actual_temp()"
    reason = "The function is not getting the time and temp properly"
    time_dict = {1: [9, 10, 11, 12]}
    temp_dict = {1: [12, 16, 24, 21]}
    expected = {1: [9, 12]}
    result = actual_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_12():
    objective = "actual_temp()"
    reason = "The function is not getting the time and temp properly"
    time_dict = {1: [9, 10, 11, 12], 2: [23, 0, 1]}
    temp_dict = {1: [12, 16, 24, 21], 2: [20, 21, 42]}
    expected = {1: [9, 12], 2: [23, 20]}
    result = actual_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


def test_13():
    objective = "actual_temp()"
    reason = "The function is not getting the time and temp properly"
    time_dict = {3: [9, 10, 11, 12], 1: [23, 0, 1]}
    temp_dict = {1: [12, 16, 24, 21], 3: [20, 21, 42]}
    expected = {1: [23, 12], 3: [9, 20]}
    result = actual_temp(temp_dict, time_dict)
    assert result == expected, str_form(objective, result, expected, reason)


# Testing the day_temps from Data_format file
def test_14():
    objective = "day_temp()"
    reason = "The function is not doing math correctly correctly"
    compared_temps = {0: [1,2,4,5,6,7,8,9,10,11]}
    time_of_day = 0
    period = 5
    expected = {1: {'max': 6, 'min': 1, 'avg':(sum(compared_temps[0][0:5])/5)}, 2:{'max': 11, 'min':7, 'avg':(sum(compared_temps[0][5:10])/5)}}
    result = day_temps(compared_temps,time_of_day,period)
    assert result == expected, str_form(objective, result, expected, reason)


def test_15():
    objective = "day_temp()"
    reason = "The function is not doing math correctly correctly"
    compared_temps = {0: [1,2], 1:[2,4], 2:[3,6]}
    time_of_day = 2
    period = 2
    expected = {1: {'max': 6, 'min': 3, 'avg': 4.5}}
    result = day_temps(compared_temps,time_of_day,period)
    assert result == expected, str_form(objective, result, expected, reason)

