from main import request_data, weather_message
import pytest 

@pytest.fixture
def userInput():
    userInput  = {
        'city':"hartford",
        'state':"Connecticut",
        'unit' : "metric"
    }
    return userInput
@pytest.fixture
def requestData():
    data = { 'main':{
        'temp': 86
    },
    'weather': [{
        'main':"cloudy"
    }]
    }
    return data
@pytest.fixture
def response_code():
    return 200
def test_request_data(userInput, response_code):
    data = request_data(userInput)
    assert(int(data['cod']) == response_code)
    
def test_weather_message(userInput,requestData):
    units = "Celsius"
    message = (f"The weather in {userInput['city']}, {userInput['state']} is {requestData['weather'][0]['main']} with temperature at: {requestData['main']['temp']} degrees {units.lower()}.")
    assert(message == weather_message(userInput,requestData))
