import requests

def check_input():
    if (not x.isAlpha()):
        print("Invalid input (enter only alphabets)")

print('Enter the city (no abbreviations)')
x = input()

print('Enter the State (no abbreviations)')
y = input()
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
