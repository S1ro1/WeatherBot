import requests

url = "https://api.opencagedata.com/geocode/v1/json?q="

def convert_to_geocord(location, key):
    request_url = f"{url}{location}&key={key}"
    data = requests.get(request_url).json()
    lat = data["results"][0]["annotations"]["DMS"]["lat"].split("'")[0].replace(" ", "")
    lng = data["results"][0]["annotations"]["DMS"]["lng"].split("'")[0].replace(" ", "")
    lat = dms2dec(lat)
    lng = dms2dec(lng)
    return [lat, lng]


def dms2dec(dms):
    if len(dms) > 5:
        degrees = dms[:3]
    else:
        degrees = dms[:2]

    minutes = int(round(int(dms[-2:])/60*100, 0))
    string = ("".join(degrees))+"."+str(minutes)
    return string

