import pytest


@pytest.fixture()
def setUp():
    print("Once before every method")


def test_methodA(setUp):
    print("Running Method A")


def test_methodB():
    print("Running Method B")