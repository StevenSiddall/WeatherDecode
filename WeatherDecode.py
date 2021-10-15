from datetime import datetime
import sys

symbolDict = {
    'MI' : 'Shallow',
    'PR' : 'Partial',
    'BC' : 'Patches',
    'DR' : 'Low Drifting',
    'BL' : 'Blowing',
    'SH' : 'Showers',
    'TS' : 'Thunderstorm',
    'FZ' : 'Freezing',
    'DZ' : 'Drizzle',
    'RA' : 'Rain',
    'SN' : 'Snow',
    'SG' : 'Snow Grains',
    'IC' : 'Ice Crystals',
    'PL' : 'Ice Pellets',
    'GR' : 'Hail',
    'GS' : 'Small Hail and/or Snow Pellets',
    'UP' : 'Unknown Precipitation',
    'BR' : 'Mist',
    'FG' : 'Fog',
    'FU' : 'Smoke',
    'VA' : 'Volcanic Ash',
    'DU' : 'Widespread Dust',
    'SA' : 'Sand',
    'HZ' : 'Haze',
    'PY' : 'Spray',
    'PO' : 'Well-Developed Dust/Sand Whirls',
    'SQ' : 'Squalls',
    'FC' : 'Funnel Cloud Tornado Waterspout',
    'SS' : 'Sandstorm',
    'DS' : 'Duststorm'
}

skyCoverDict = {
    'VV' : 'Vertical Visibility',
    'SKC' : 'Clear',
    'CLR' : 'Clear',
    'FEW' : 'Feq',
    'SCT' : 'Scattered',
    'BKN' : 'Broken',
    'OVC' : 'Overcast'
}

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

def decodeWind(windIn: str):
    gustStr = ''
    if 'G' in windIn:
        # Gust portion is present
        windSplit = windIn.split('G')
        windIn = windSplit[0]
        gustStr = ' with gusts to ' + windSplit[1][:-2] + 'KT'
    else:
        windIn = windIn[:-2]

    if windIn == '00000':
        return 'Calm wind' + gustStr
    return 'Wind from ' + windIn[:3] + ' at ' + windIn[3:] + 'KT' + gustStr

def decodeVariableWind(varWindIn: str):
    varWindSplit = varWindIn.split('V')
    return 'Wind variable from ' + varWindSplit[0] + ' to ' + varWindSplit[1]

def decodeVisibility(visIn: str):
    lessThanStr = ""
    if visIn[0] == 'M':
        lessThanStr = 'less than '
        visIn = visIn[1:]
    return 'Visibility ' + lessThanStr + visIn

def decodeRunwayVisualRange(rvrIn: str):
    rvrSplit = rvrIn.split('/')
    runwayStr = rvrSplit[0][1:]
    modifierStr = ''
    if rvrSplit[1][0] == 'M':
        modifierStr = 'Less than '
        rvrSplit[1] = rvrSplit[1][1:]
    elif rvrSplit[1][0] == 'P':
        modifierStr = 'Greater than '
        rvrSplit[1] = rvrSplit[1][1:]

    if 'V' in rvrSplit[1]:
        # Variable visual range
        varRvrSplit = rvrSplit[1].split('V')
        return 'Runway ' + runwayStr + ': ' + modifierStr + varRvrSplit[0] + 'FT to ' + varRvrSplit[1]
    else:
        return 'Runway ' + runwayStr + ': ' + modifierStr + rvrSplit[1]

def decodePresentWeather(presWeatherIn: str):
    weatherInSplit = presWeatherIn.split()
    returnStr = ''
    for group in weatherInSplit:
        if group[:1] == 'VC':
            group = group[2:]
            resolvedGroup = symbolDict[group] if len(group) == 2 else symbolDict[group[:1]] + ' ' + symbolDict[group[2:3]]
            returnStr += resolvedGroup + 'In the Vicinity' + ', '
            continue

        intensityStr = ''
        if group[0] == '-':
            intensityStr = 'Light '
            group = group[1:]
        elif group[0] == '+':
            intensityStr = 'Heavy '
            group = group[1:]
        else:
            intensityStr = 'Moderate '
        resolvedGroup = symbolDict[group] if len(group) == 2 else symbolDict[group[:2]] + ' ' + symbolDict[group[2:]]
        returnStr += intensityStr + resolvedGroup + ', '
        continue

    return returnStr[:-2]


if __name__ == '__main__':
    # TODO: Get live data
    #input = sys.argv[1]
    #print("Input:", input)

    #inputSplit = input.split()
    #print(inputSplit)

    # TODO: Check basic input requirements

    type = decodeType('METAR:')
    stationID = decodeStationID('KMYF')
    dateTime = decodeDateTime('090253Z')
    wind = decodeWind('21010KT')
    varWind = decodeVariableWind('180V240')
    vis = decodeVisibility('10SM')
    rvr = decodeRunwayVisualRange('R01L/M0600V1000FT')
    presWeather = decodePresentWeather('-FZDZ +FC')
    print("Type:", type)
    print("Station ID:", stationID)
    print("Date and Time:", dateTime)
    print("Wind: ", wind)
    print("Variable wind: ", varWind)
    print("Visibility: ", vis)
    print("Runway Visible Range: ", rvr)
    print("Present Weather: ", presWeather)