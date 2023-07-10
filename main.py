import requests

def input_valid(user):
    if (not user.isalpha() and len(user) > 0):
        print("Invalid input (enter only alphabets)")
        return False
    else:
        return True

# def inputs():
#     #enter inputs
#     x = input('Enter the city (no abbreviations)')
#     while (not input_valid(x)):
#         x = input("Invalid input, Try again")

#     y = input('Enter the State (no abbreviations)')
#     while (not input_valid(y) ):
#         y = input('Enter the State (no abbreviations)')
#     return x,y

# def inputs():
#     x = input('Enter valid City')
#     y = input('Enter valid State/country')
#     if (not input_valid(x) or not input_valid(y)):
#         x=""
#         y=""
#         return x,y
#     else:
#         return x,y

# x,y = inputs()

# if (x == ""):
#     print('Invalid input try again')
#     inputs()


# user = ""
# while (input_valid(user) == False):
#     user.input('Enter the city (no abbreviations)')
# x = user
# user = ""
# while (input_valid(user) == False):
#     user.input('Enter the state (no abbreviations)')
# y = user


""" x = input('Enter the city (no abbreviations)')
y = input('Enter the state (no abbreviations)')

print('Enter C, F or K for me')
z = input()
unit = ""
if (z == "C"):
    unit = "metric"
elif(z == "F"):
    unit = "imperial"
else:
    unit = ""
 """
# validate user inputs
# user should not enter a number




# validate api call
def request_data(userInput):
    response = None
    try:
        response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={userInput.city},{userInput.state}&limit=1&appid=51feb6438334e6502cf871203e59a9af&units={userInput.unit}")
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
