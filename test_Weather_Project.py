
import Weather_Project as WP
import readcsv as RC
import datetime as DT

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