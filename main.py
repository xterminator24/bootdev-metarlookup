from airport import Airport

def prompt_for_icao():
    airport_icao = input("ICAO: ")
    return airport_icao.upper()

def main():
    airport_icao = prompt_for_icao()
    airport = Airport(airport_icao)

    if not airport:
        print(f"failed to find airport {airport_icao}")

    print_airport_to_console(airport)

def print_airport_to_console(airport):
    print()
    print()
    print('=========================================================')    
    print(f"  {airport.name} ({airport.icao}) | {airport.country}")
    print('=========================================================')
    print(f"wind: {airport.metar.wind_direction} at {airport.metar.wind_speed}")
    print(f"temperature: {airport.metar.temperature} | dewpoint: {airport.metar.dewpoint}")
    print(f"altimeter: {airport.metar.altimeter}")
    print()
    print()
        

if __name__ == "__main__":
    main()