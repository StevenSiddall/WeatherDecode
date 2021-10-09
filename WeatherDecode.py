from datetime import datetime

def decodeType(typeIn: str):
    if typeIn == "METAR" or typeIn == "SPECI":
        return typeIn
    else:
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
    
    # manipulate string to match pattern for datetime
    dateTimeIn = dateTimeIn[:1] + '+' + dateTimeIn[2:-1] + 'UTC'
    parsedDateTime = datetime.strptime(dateTimeIn, '%d%z%Z')
    return parsedDateTime