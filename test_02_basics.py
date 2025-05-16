import pytest

#@pytest.mark.smoke
def test_assertFalse():
    a = 5
    b = 6
    assert a == b

def test_assertTrue():
    a = 5
    b = 6
    assert a == b -1

def test_carName():
    print("Honda CRV")

def test_carColor():
    print("BLAAACK")

@pytest.mark.xfail
def test_carType():
    print("SUVVVVV")

#@pytest.mark.skip
def test_carPrice():
    print("25000$$")



def test_fixtureDemo(setup):
    print("Demonstrate a test fixture")

