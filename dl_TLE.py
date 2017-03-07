# import
import urllib.request

def downlaod(category):
    webx_loc = 'http://celestrak.com/NORAD/elements/' + category + '.txt'
    disk_loc = 'TLE/' + category + '.txt'
    urllib.request.urlretrieve(webx_loc, disk_loc)

list_category = [

"tle-new", "stations", "visual",
"1999-025", "iridium-33-debris", "cosmos-2251-debris",
"2012-044", "weather", "noaa",
"goes", "resource", "sarsat",
"dmc", "tdrss", "argos",
"geo", "intelsat", "ses",
"iridium", "iridium-NEXT", "orbcomm",
"globalstar", "amateur", "x-comm",
"other-comm", "gorizont", "raduga",
"molniya", "gps-ops", "glo-ops",
"galileo", "beidou", "sbas",
"nnss", "musson", "science",
"geodetic", "engineering", "education",
"military", "radar", "cubesat",
"other"

]

for element in list_category:
    downlaod(element)
