from metar import Weather, Metar

def prompt_for_icao():
    airport_icao = input("ICAO: ")
    return airport_icao.upper()

def main():
    airport_icao = prompt_for_icao()
    weather = Weather()
    metar = Metar()
    metar = weather.get(airport_icao)

    if not metar:
        print(f"weather lookup failed for {airport_icao}")
        
    print(metar)
        

if __name__ == "__main__":
    main()