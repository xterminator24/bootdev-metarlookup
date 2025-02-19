from weather import Weather

def prompt_for_icao():
    airport_icao = input("ICAO: ")
    return airport_icao.upper()

def main():
    airport_icao = prompt_for_icao()
    weather = Weather()
    json = weather.get(airport_icao)
    print(json)

if __name__ == "__main__":
    main()