from airport import Airport

def prompt_for_icao():
    airport_icao = input("ICAO: ")
    return airport_icao.upper()

def main():
    airport_icao = prompt_for_icao()
    airport = Airport(airport_icao)

    if not airport:
        print(f"failed to find airport {airport_icao}")
        
    print(airport)
        

if __name__ == "__main__":
    main()