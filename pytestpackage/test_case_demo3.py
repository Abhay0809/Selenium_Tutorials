"""
file name should start with test
test method name should start with test

py.test test_mod.py # run tests in module
py.test somepath # run all tests below somepath
py.test test_mod.py::test_method # only run test_method in test_mod

-s to print statements
-v verbose
"""

import pytest


@pytest.fixture()
def setUp():
    print("Running demo3 setUp")
    yield
    print("Running demo3 tearDown")


def test_demo3_methodA(setUp):
    print("Running demo3 method A")


def test_demo3_methodB(setUp):
    print("Running demo3 method B")


'''
py.test -s -v test_case_demo3.py
py.test -s -v
py.test -s -v .\test_case_demo3.py::test_demo3_methodB
'''


