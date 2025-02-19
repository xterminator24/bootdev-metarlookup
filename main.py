def prompt_for_icao():
    airport_icao = input("ICAO: ")
    return airport_icao.upper()

def main():
    airport_icao = prompt_for_icao()
    print(f"airport: {airport_icao}")

if __name__ == "__main__":
    main()