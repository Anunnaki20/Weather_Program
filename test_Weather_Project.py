
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
    reason = "The funciton is not converting the time correctly, check the math"
    adict = {1:[1593633600]}
    result = RC.read_time(adict)
    time = DT.datetime.utcfromtimestamp(1593633600)
    expected = int(f"{time:%H}") - 4
    assert result[1] == expected, str_form(objective,result,expected,reason)

