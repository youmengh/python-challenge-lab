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


city,state, unit = inputs()





city = "columbia"
state = "maryland"
unit = "metric"





# validate user inputs
# user should not enter a number


response = None
data = None

# validate api call
try:
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&limit=1&appid=51feb6438334e6502cf871203e59a9af&units={unit}")
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("An error occurred: ", e)
    exit(0)
except ValueError:
    print("Invalid JSON")
    exit(0)

