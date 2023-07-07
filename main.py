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


x = input('Enter the city (no abbreviations)')
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

# validate user inputs
# user should not enter a number


response = None
data = None

# validate api call
try:
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={x},{y}&limit=1&appid=51feb6438334e6502cf871203e59a9af&units={unit}")
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("An error occurred: ", e)
    exit(0)
except ValueError:
    print("Invalid JSON")
    exit(0)

temp = response.json()['main']['temp']
print(temp)
