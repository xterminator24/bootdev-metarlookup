import os
import platform
from airport import Airport

def prompt_for_icao():
    airport_icao = input("Enter ICAO or \"exit\" to exit: ")
    return airport_icao.upper()

def main():
    clear_console()
    while True:
        airport_icao = prompt_for_icao()

        if airport_icao == "EXIT":
            break

        airport = Airport(airport_icao)

        if not airport.is_valid:
            print(f"failed to find airport {airport_icao}")
        else:
            print_airport_to_console(airport)


def print_airport_to_console(airport):
    print()
    print()
    print('=========================================================')    
    print(f"  {airport.name} ({airport.icao}) | {airport.country}")
    print('=========================================================')
    print(f"wind: {airport.metar.wind_direction} at {airport.metar.wind_speed}")
    print(f"temperature: {airport.metar.temperature} | dewpoint: {airport.metar.dewpoint}")
    print(f"altimeter: {round(airport.metar.altimeter_hpa)} ({round(airport.metar.altimeter_inhg, 2)})")
    if airport.metar.precipitation is not None:
        print(f"precipitation: {airport.metar.precipitation}")
    if airport.metar.snow is not None:
        print(f"snow: {airport.metar.snow}")
    print()
    print(f"raw: {airport.metar.raw}")
    print()
    print()

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        

if __name__ == "__main__":
    main()