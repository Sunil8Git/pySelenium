import pytest


@pytest.mark.usefixtures("dataLoad")
#since the fixture name is being returned we are able to see that we have to use dataLoad which is the returned value in test definition
class TestClassDataLoad:

    def test_class_dataLoad(self, dataLoad):
        print("Inside Class Data Load", dataLoad)

def test_multiBrowserCase(multiBrowser):
    print("Inside MultiBrowser Case", multiBrowser[0])
