import datetime as DT
import readcsv as RC
from Data_format import time_and_temp


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


