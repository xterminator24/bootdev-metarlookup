class FieldMap:
    def __init__(self):
        self.map = {
            "metar_id": "id",
            "icaoId": "icao",
            "name": "airport_name",
            "receiptTime": "receipt_time",
            "reportTime": "report_time",
            "temp": "temperature",
            "dewp": "dewpoint",
            "wdir": "wind_direction",
            "wspd": "wind_speed",
            "visib": "visibility",
            "altim": "altimeter",
            "precip": "precipitation",
            "snow": "snow",
            "vertVis": "vertical_visibility",
            "rawOb": "raw",
            "clouds": "clouds"
        }

class Metar:
    def __init__(self):
        self.id = None
        self.icao = None
        self.airport_name = None
        self.receipt_time = None
        self.report_time = None
        self.temperature = None
        self.dewpoint = None
        self.wind_direction = None
        self.wind_speed = None
        self.visibility = None
        self.altimeter = None
        self.precipitation = None
        self.snow = None
        self.vertical_visibility = None
        self.raw = None
        self.clouds = None

    def load_from_json(self, json):
        print("loading...")
        cleaned_json = self.remove_nulls_from_json(json)
        field_map = FieldMap()
        for k, v in cleaned_json.items():
            field = field_map.map.get(k, "None")
            if field:
                setattr(self, field, v)

    def remove_nulls_from_json(self, json):
        if isinstance(json, dict):
            result = {}
            for k, v in json.items():
                if v is not None:
                    cleaned_value = self.remove_nulls_from_json(v)
                    result[k] = cleaned_value
            return result
        elif isinstance(json, list):
            result = []
            for item in json:
                if item is not None:
                    cleaned_item = self.remove_nulls_from_json(item)
                    result.append(cleaned_item)
            return result
        else:
            return json
        
    def __repr__(self):
        properties = ""
        for key, value in self.__dict__.items():
            properties += f"{key}: {value}\n"
        return properties
        
