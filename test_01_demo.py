#ANY PYTEST file should start with test_ keyword
#Test Method Names also should have test_ or end with _test
# pytest test_02_basics.py -v -s
# Example there are many cases with similar names like
# carName, carColor, carType, carPrice, to run all car cases we can give below command
# pytest -k car -v -s
# OR
# pytest test_02_basics.py -k car -v -s
# -k FOR METHOD NAME EXECUTION
# -s FOR PRINTING OUTPUT
# -v FOR MORE INFORMATION verbose

# TO RUN SMOKE TEST CASES
# tag/mark the test cases with @pytest.mark.smoke--> smoke is user defined
# pytest -m smoke -v -s

# SKIP a Test Case from the suite
# @pytest.mark.skip
# pytest -v -s
#================================= 1 failed, 7 passed, 1 skipped, 3 warnings in 0.14s ==================================
#SUNIL KUMAR S
# WORKING IN USA FOR ATT

# @pytest.mark.xfail
# test_02_basics.py::test_carType SUVVVVV
# XPASS
# to make to run the test case for any pre req for other test case required, but no need to worry about execution details

# FIXTURES
import pytest


# C:\Users\admin\PycharmProjects\PythonProject\pyTest>py.test
# ================================================= test session starts =================================================
# platform win32 -- Python 3.8.6, pytest-8.3.5, pluggy-1.5.0
# rootdir: C:\Users\admin\PycharmProjects\PythonProject\pyTest
# collected 1 item
#
# test_01_demo.py .                                                                                                [100%]
#
# ================================================== 1 passed in 0.06s ==================================================
#
# C:\Users\admin\PycharmProjects\PythonProject\pyTest>py.test -s
# ================================================= test session starts =================================================
# platform win32 -- Python 3.8.6, pytest-8.3.5, pluggy-1.5.0
# rootdir: C:\Users\admin\PycharmProjects\PythonProject\pyTest
# collected 1 item
#
# test_01_demo.py HELLO PYTEST
# .
#
# ================================================== 1 passed in 0.01s ==================================================
# @pytest.fixture when give the test becomes like init and in the same function if a yeild command is given, post commands give after yeild will be executed as tear down
# test_02_basics.py::test_fixtureDemo
# Setting up the test suite
# Demonstrate a test fixture
# PASSED
# Finalizing the test suite
# Instead of having multiple fixtures in a suite, we can create a CONFTEST.py
# which tell what configs has to be done

def test_firstProg():
    print("HELLO PYTEST")
def test_secondProg():
    print("HELLO GOOD MORNING")
#IF SAME test name is given then the latest one will replace the above one.

#@pytest.mark.smoke
def test_assertErr():
    tempStr = "Sunil Kumar S"
    assert tempStr == "Sunil Kumar S"
