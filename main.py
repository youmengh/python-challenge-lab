import config
import requests

def input_valid(user):
    if (not user.isalpha() or not len(user) > 0):
        return False
    else:
        return True

def inputs():
    #enter inputs
    city = input('Enter the city (no abbreviations): ')
    while (not input_valid(city)):
        city = input("Invalid input, Try again: ")

    state = input('Enter the State (no abbreviations): ')
    while (not input_valid(state) ):
        state = input("Invalid input, Try again: ")

    unit = input('Enter C, F, or K to specify the unit: ')
    while unit.upper() not in ('C', 'F', 'K'):
        unit = input('Please select one of the three Availible options (C, F, or K): ')
    
    if (unit == "C"):
        unit = "metric"
    elif(unit == "F"):
        unit = "imperial"
    else:
        unit = ""

    return city, state, unit


#city,state, unit = inputs()
userInput = {k:v for (k,v) in zip(("city", "state", "unit"), inputs())}
print(userInput)



city = "columbia"
state = "maryland"
unit = "metric"





# validate user inputs
# user should not enter a number




# validate api call
def request_data(userInput):
    response = None
    try:
        response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={userInput.city},{userInput.state}&limit=1&appid={config.api_key}&units={userInput.unit}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred: ", e)
        exit(0)
    except ValueError:
        print("Invalid JSON")
        exit(0)
    finally:
        return None
def display_weather(userInput, data):
    units = None 
    temp = data['main']['temp']
    weather = data['weather']['main']
    if (userInput.unit== "metric"):
        units = "Fahrenheit"
    elif(userInput.unit== "imperial"):
        units = "Celsius"
    else:
        units = "Kelvin"
    Weather_message = (f"The weather in {userInput.city}, {userInput.state} is {weather} with temperature at: {temp} {units}")
    print(Weather_message)
