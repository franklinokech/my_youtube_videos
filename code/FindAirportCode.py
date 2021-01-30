# import the dictfile module
from dictfile import readDictionary


def FindAirportCode():
    airportDictionary = readDictionary('airports.txt')

    while True:
        code = input('Enter the Airport Code')
        if code == "": break
        if code in airportDictionary:
            print(airportDictionary[code])
        else:
            print('their is no airport with code '+ code)


# start code
if __name__ == '__main__':
    FindAirportCode()