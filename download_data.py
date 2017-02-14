import urllib.request

# downlaod specific categeory
def download(category):
    webx_loc = 'http://celestrak.com/NORAD/elements/' + category + '.txt'
    disk_loc = 'TLE/' + category + '.txt'
    urllib.request.urlretrieve(webx_loc, disk_loc)

# download category
download("argos")
