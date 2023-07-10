import main 
import pytest 

@pytest.fixture
def userInput():
    userInput  = {
        'city':"hartford",
        'state':"Connecticut",
        'unit' : "Celsius"
    }
    return userInput

def test_request_data():
    pass
def test_display_weather(userInput,):
    data = ['']
    
