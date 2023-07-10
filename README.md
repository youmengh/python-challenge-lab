Part 1.1 - API
Use the following endpoint
http://api.openweathermap.org/data/2.5/weather?q=London&appid=51feb6438334e6502cf871203e59a9af

Store result in a variable called "response"

response.json() returns the JSON format

temp = response.json()['main']['temp']

Part 1.2 - BDD/ATDD
Validate User Input:
Given the task of getting the city name from user input,
when user inputs the city, state, unit, they should be validated before passing to api call,
then user input can be passed on to the api call after validation.

Validate API Call:
Given the task of making an API call,
when we get the response, it should be code 200,
then we can extract the result and return it to user.

Part 1.3 - Modules
import request


Contributors
Youmeng Hin
William Boafo
Willsmaith Pochette
Jacob Lettick
Dhir Patel
Brandon Chu
Ayodele Odeseye
Adam Alti
Stephen McNally
