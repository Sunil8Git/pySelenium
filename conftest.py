import pytest


@pytest.fixture(scope="class")
def setup():
    print("\nSetting up the test suite")
    yield
    print("\nFinalizing the test suite")

@pytest.fixture()
def dataLoad():
    print("Inside Loading Data")
    return ("sunil", "Kumar","In USA")

# This fixture will make sure it uses all the params in one by one and run the test case
# Any Data Type can be passed as part of the params which can be used in the def
@pytest.fixture(params=["Chrome", "Firefox", ("Sunil","Kumar"),("Soma","sundara","5G","Verizon Target")])
def multiBrowser(request):
# Request is a inbuilt operation which is tied up to fixture which is an object of fixture
# it will pick one by one of all the params in fixutre.
    print("Inside MultiBrowser")
    return request.param



