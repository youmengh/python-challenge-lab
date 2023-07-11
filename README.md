## Group 2: Python Challenge Lab
### Objective: This lab leverages your knowledge of Python and TDD to create a Python application to use a public
API as its back end.
### Part 1.1 - API
- Use the following endpoint
- http://api.openweathermap.org/data/2.5/weather?q=London&appid=51feb6438334e6502cf871203e59a9af

- Store result in a variable called "response"

- response.json() returns the JSON format

- temp = response.json()['main']['temp']

### Part 1.2 - BDD/ATDD
- Validate User Input: Given the task of getting the city name from user input, when user inputs the city, state, unit, they should be validated before passing to api call, then user input can be passed on to the api call after validation.

- Validate API Call: Given the task of making an API call, when we get the response, it should be code 200, then we can extract the result and return it to user.

### Part 1.3 - Modules
- import request
Part 1.4 Testing
- Testing api request
- Testing output message
- to run Test: pytest -s


### Contributors
- Youmeng Hin
- William Boafo
- Willsmaith Pochette
- Jacob Lettick
- Dhir Patel
- Brandon Chu
- Ayodele Odeseye
- Adam Alti
- Stephen McNally

### Some improvements that could be worked on:
- Utilized external api to validate User City and state input
- graphical user interface as opposed to command line to prompt user input and display the current weather.

