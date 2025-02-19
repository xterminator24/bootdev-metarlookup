from weather import Weather
from metar import Metar

def prompt_for_icao():
    airport_icao = input("ICAO: ")
    return airport_icao.upper()

def main():
    airport_icao = prompt_for_icao()
    weather = Weather()
    metar = Metar()
    json = weather.get(airport_icao)

    if json:
        metar.load_from_json(json)
        print(metar)
    else:
        print("weather lookup failed")

if __name__ == "__main__":
    main()