import pytest

@pytest.mark.usefixtures("setup") # Runs for each and every test execution
# But the same when declaring in conftest we give scope=class
# it will run once during start of class and end of class
class TestFixture:
    def test_firstProg(self):
        print("FIRST PROGRAM of CLASS1")
    def test_secondProg(self):
        print("2nd PROGRAM of CLASS1")
    def test_thirdProg(self):
        print("3rd PROGRAM of CLASS1")
    def test_fourthProg(self):
        print("4th PROGRAM of CLASS1")
    def test_fifthProg(self):
        print("5th PROGRAM of CLASS1")