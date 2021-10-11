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
The type, METAR or SPECI, shall be included inall reports. The type of report shall be separated from elements following it by a space. Whenever SPECI criteria are met a the time of the routine METAR, the type of report shall be METAR.

#### <u>Station Identifier</u> (CCCC)
The station identifier, CCCC, shall be included in all reports to identify the station to which the coded report applies. The station identifier shall consist of four aplhabetic-only characters if the METAR/SPECI is transmitted long-line.

#### <u>Date and Time of Report</u> (YYGGggZ)
The date, YY, and time, GGgg, shall be included in all reports. The time shall be the actual time of the report or when the criteria for a SPECI is met or noted. If the report is a correction to a previously disseminated report, the time of the corrected report shall be the same time used in the report being corrected. The date and time group always ends with a Z indicationg Zulu time (or UTC). For example, METAR KDCA 210855Z would be the 0900 scheduled report from station KDCA taken at 0855 UTC on the 21st of the month.

#### <u>Report Modifier</u> (AUTO/COR)
The report modifer, AUTO, identifies the METAR/SPECI as a fully automated report with no human intervention or oversight. In the event of a corrected METAR or SPECI, the report modifier, COR, shall be substituted in place of AUTO.

#### <u>Wind Group</u> (dddff(f)Gf<sub>m</sub>f<sub>m</sub>(f<sub>m</sub>)KT_d<sub>n</sub>d<sub>n</sub>d<sub>n</sub>Vd<sub>x</sub>d<sub>x</sub>d<sub>x</sub>)
The wind direction, ddd, shall be coded in tens of degrees using three figures. Directions less than 100 degrees shall be preceded with a "0". For example, a wind direction of 90 degrees is coded as "090". The wind speed, ff(f) shall be coded in two or three digits immediately following the wind direction. The wind speed shall eb coded, in whole knots, using the units and tens digits and, if required, the hundreds digit. Speeds of less than 10 knots shall be coded using a leading zero. The wind group shall always end with a KT to indicate that wind speeds are reported in knots. For example, a wind speed of 8 knots shall be coded "08KT"; a wind speed of 112 knots shall be coded as "112KT".

a. Gust. Wind gusts shall be coded in the format, Gf<sub>m</sub>f<sub>m</sub>(f<sub>m</sub>). The wind gust shall be coded in two or three digits immediately following the wind speed. The wind gust shall be coded in whole knots, using the units and tens digits and, if required, the hundreds digit. For example, a wind from due west at 20 knots with gusts to 35 knots would be coded "27020G35KT".

b. Variable Wind Direction (Speeds 6 knots or less). Variable wind direction with wind speed 6 knots or less may be coded as VRB in place of the ddd. For example, if the wind is variable at three knots, it would be coded "VRB03KT".

c. Variable wind Direction (Speeds greater than 6 knots). Variable wind direction with wind speed greater than 6 knots shall be coded in the format, d<sub>m</sub>d<sub>m</sub>d<sub>m</sub>Vd<sub>x</sub>d<sub>x</sub>d<sub>x</sub>. The variable wind direction group shall immediately follow the wind group. The directional variability shall be coded in a clockwise direction. For example, if the wind is variable from 180 degrees to 240 degrees at 10 knots, it would be coded "21010KT 180V240".

d. Calm Wind. Calm wind shall be coded as "00000KT".

#### <u>Visibility Group</u> (VVVVVSM)
The surface visibility, VVVVVSM, shall be coded instatute miles. A space shall be coded between whole numbers and fractions fo reportable visibility values. The visibillity group shall always end with SM to indicate that the visibility is in statute miles. For example, a visibility of one and a half statute miles would be coded "1 1/2SM". Automated stations shall use an M to indicate "less than" when reporting visibility. For example, "M1/4SM" means a visibility of less than one-quarter statute mile.

#### <u>Runway Visual Range Group</u> (RD<sub>R</sub>D<sub>R</sub>/V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>V<sub>R</sub>FT or RD<sub>R</sub>D<sub>R</sub>/V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>V<sub>N</sub>VV<sub>X</sub>V<sub>X</sub>V<sub>X</sub>V<sub>X</sub>FT)

#### <u>Present Weather Group</u> (w'w')

#### <u>Sky Condition Group</u> (N<sub>s</sub>N<sub>s</sub>N<sub>s</sub>h<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or VVh<sub>s</sub>h<sub>s</sub>h<sub>s</sub> or SKC/CLR)

#### <u>Termperature/Dew Point Group</u> (T'T'/T'<sub>d</sub>T'<sub>d</sub>)

#### <u>Altimeter</u> (AP<sub>h</sub>P<sub>h</sub>P<sub>h</sub>P<sub>h</sub>)

### Remarks (RMK)
