import requests
print('Enter the city (no abbreviations)')
x = input()
print('Enter the State (no abbreviations)')
y = input()
print('Enter C, F or K for me')
z = input()
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={x},{y}&limit=1&appid=51feb6438334e6502cf871203e59a9af")
temp = response.json()['main']['temp']
print(temp)

