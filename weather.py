import requests

class Weather:

    def __init__(self):
        self.api_base_url = "https://aviationweather.gov/api/data/metar?"

    def get(self, icao):
        url = self.api_base_url + f"ids={icao}" + "&format=json"
        print("retrieving...")
        response = requests.get(url)

        if response.status_code != 200:
            return None
        
        json_data = response.json()
        return json_data[0]
