# WeatherDecode
Decodes raw weather data in METAR format as specified below

## Format
The following is taken from the U.S. Federal Meteorological Handbook No. 1 — Surface Weather Observations and Reports (September 2005): [Link](https://web.archive.org/web/19990420051036/http://www.ofcm.gov/fmh-1/fmh1.htm)

### METAR/SPECI Code
METAR or SPECI_CCCC\_YYGGggZ\_AUTO or COR\_dddff(f)Gf<sub>m</sub>f<sub>m</sub>(f<sub>m</sub>)KT_d<sub>n</sub>d<sub>n</sub>d<sub>n</sub>Vd<sub>x</sub>d<sub>x</sub>d<sub>x</sub>\_VVVVVSM\_[RD<sub>R</sub>D<sub>R</sub>/V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>FT or RD<sub>R</sub>D<sub>R</sub>/V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>VV<sub>X</sub>V<sub>X</sub>V<sub>X</sub>V<sub>X</sub>FT]\_w'w'\_[N<sub>s</sub>N<sub>s</sub>N<sub>s</sub>h<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or VVh<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or SKC/CLR]\_T'T'/T'<sub>d</sub>T'<sub>d</sub>\_AP<sub>h</sub>P<sub>h</sub>P<sub>h</sub>P<sub>h</sub>\_RMK\_(Automated, Manual, Plain Language)\_(Additive Data and Automated Maintenance Indicators)

### Format and Content
a. Body
1. Type of Report - METAR/SPECI
2. Station Identifier - CCCC
3. Date and Time of Report - YYGGggZ
4. Report Modifier - AUTO/COR
5. Wind - dddff(f)Gf<sub>m</sub>f<sub>m</sub>(f<sub>m</sub>)KT_d<sub>n</sub>d<sub>n</sub>d<sub>n</sub>Vd<sub>x</sub>d<sub>x</sub>d<sub>x</sub>
6. Visibility - VVVVVSM
7. Runway Visible Range - RD<sub>R</sub>D<sub>R</sub>/V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>FT or RD<sub>R</sub>D<sub>R</sub>/V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>VV<sub>X</sub>V<sub>X</sub>V<sub>X</sub>V<sub>X</sub>FT
8. Present Weather - w'w'
9. Sky Condition - N<sub>s</sub>N<sub>s</sub>N<sub>s</sub>h<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or VVh<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or SKC/CLR
10. Temperature and Dew Point - T'T'/T'<sub>d</sub>T'<sub>d</sub>
11. Altimiter - AP<sub>h</sub>P<sub>h</sub>P<sub>h</sub>P<sub>h</sub>

b. Remarks
1. Automated, Manual, and Plain Language
2. Additive and Maintenance Data


The underline character "_" indicates a required space between groups. If a group is not reported, the preceding space is also not reported. In addition to the format given, agencies shall provide for the inclusion of any special Beginning-of-Message, End-of-Message, or End-of-Transmission signals required by their communication system.

### Coding Missing Data in METAR/SPECI
When an element does not occur, or cannot be observed, the corresponding group and preceding space are omitted from that particular report.

### Coding the Body of the METAR/SPECI
#### <u>Type of Report</u> (METAR and SPECI)

#### <u>Station Identifier</u> (CCCC)

#### <u>Date and Time of Report</u> (YYGGggZ)

#### <u>Report Modifier</u> (AUTO/COR)

#### <u>Wind Group</u> (dddff(f)Gf<sub>m</sub>f<sub>m</sub>(f<sub>m</sub>)KT_d<sub>n</sub>d<sub>n</sub>d<sub>n</sub>Vd<sub>x</sub>d<sub>x</sub>d<sub>x</sub>)

#### <u>Visibility Group</u> (VVVVVSM)

#### <u>Runway Visual Range Group</u> (RD<sub>R</sub>D<sub>R</sub>/V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>FT or RD<sub>R</sub>D<sub>R</sub>/V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>VV<sub>X</sub>V<sub>X</sub>V<sub>X</sub>V<sub>X</sub>FT)

#### <u>Present Weather Group</u> (w'w')

#### <u>Sky Condition Group</u> (N<sub>s</sub>N<sub>s</sub>N<sub>s</sub>h<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or VVh<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or SKC/CLR)

#### <u>Termperature/Dew Point Group</u> (T'T'/T'<sub>d</sub>T'<sub>d</sub>)

#### <u>Altimeter</u> (AP<sub>h</sub>P<sub>h</sub>P<sub>h</sub>P<sub>h</sub>)

### Remarks (RMK)
