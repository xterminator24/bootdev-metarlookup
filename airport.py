import requests
from metar import Weather

class FieldMap:
    def __init__(self):
        self.map = {
            "id": "id",
            "name": "name",
            "icaoId": "icao",
            "iataId": "iata",
            "faaId": "faa",
            "state": "state",
            "country": "country",
            "source": "source",
            "type": "type",
            "lat": "latitude",
            "lon": "longitude",
            "elev": "elevation",
            "runways": "runways",
            "rwyNum": "runway_count",
            "passengers": "passengers",
            "beacon": "beacon",
            "tower": "tower"
        }

class Airport:
    def __init__(self, icao):
        self.id = None
        self.name = None
        self.icao = icao
        self.iata = None
        self.faa = None
        self.state = None
        self.country = None
        self.source = None
        self.type = None
        self.latitude = None
        self.longitude = None
        self.elevation = None
        self.runways = None
        self.runway_count = None
        self.passengers = None
        self.beacon = None
        self.has_beacon = None
        self.tower = None
        self.has_tower = None
        self.metar = None

        # get airport info and load
        self.load()

        # retrieve the weather information
        weather = Weather()
        self.metar = weather.get(icao)

        self.has_beacon = self.beacon == "B"
        self.has_tower = self.tower == "T"

    def load(self):
        url = f"https://aviationweather.gov/api/data/airport?ids={self.icao}&format=json"
        print("retrieving airport...")
        response = requests.get(url)

        if response.status_code != 200:
            return None
        
        json_data = response.json()

        if len(json_data) == 0:
            return None
        
        self.load_from_json(json_data[0])
        
    def load_from_json(self, json):
        print("loading airport...")
        field_map = FieldMap()
        for key, value in json.items():
            field = field_map.map.get(key, None)
            if field:
                setattr(self, field, value)
        print("airport loaded...")

    def __repr__(self):
        properties = ""
        for key, value in self.__dict__.items():
            properties += f"{key}: {value}\n"
        return properties
