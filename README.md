# bootdev-metarlookup
Look up aviation weather information using ICAO codes

## Installation
### Create a virtual environment
```
python3 -m venv venv
```
### Activate the virtual environment
```
source venv/bin/activate
```
### Install the project required packages
```
pip install requests
```
### Verify the required packages are installed
```
pip list
```

## TODO
- [ ] Convert altimeter to inHg when country is CA, US, or JP
- [ ] Come up with a useful way to display the data. Initially on the console.
- [ ] Refactor the Weather Class to work more like the airport class (pass the ICAO on init)
- [ ] Implement better error handling when entering an invalid ICAO
- [ ] Imlement a method of determining best runway to use based on wind direction
- [ ] Implement a flight mode where you can select a Departure, Arrival, and Alternate airport and provide a weather briefing
- [ ] Implement a text to speech option to read the metar of an airport
