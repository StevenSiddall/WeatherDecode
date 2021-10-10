from datetime import datetime
import sys

def decodeType(typeIn: str):
    if typeIn == "METAR:" or typeIn == "SPECI:":
        return typeIn[:-1]
    return -1

def decodeStationID(stationIn: str):
    # TODO: Do lookup in dict mapping station codes to full names
    return stationIn

def decodeDateTime(dateTimeIn: str):
    # Format: YYGGggZ e.g. 090253Z
    # YY = Day of month
    # GGggZ = Time in UTC (Zulu time) e.g. 1830Z
    if len(dateTimeIn) != 7 or dateTimeIn[6] != 'Z':
        return -1

    now = datetime.utcnow()
    parsedDateTime = datetime.strptime(dateTimeIn, '%d%H%MZ')
    parsedDateTime = parsedDateTime.replace(year=now.year, month=now.month)
    return parsedDateTime.strftime('%H%MZ %b %d %Y')

def decodeModifier(modifierIn: str):
    if modifierIn == 'AUTO':
        return 'AUTO -- Report was automatically generated'
    elif modifierIn == 'COR':
        return 'COR -- Report was corrected'
    return -1

if __name__ == '__main__':
    # TODO: Get live data
    input = sys.argv[1]
    print("Input:", input)

    inputSplit = input.split()
    print(inputSplit)

    # TODO: Check basic input requirements

    type = decodeType(inputSplit[0])
    stationID = decodeStationID(inputSplit[1])
    dateTime = decodeDateTime(inputSplit[2])
    print("Type:", type)
    print("Station ID:", stationID)
    print("Date and Time:", dateTime)