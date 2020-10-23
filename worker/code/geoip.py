import geoip2.database,json
def getGeoip(ip,filter):#countryIso,countryName
    reader = geoip2.database.Reader('./code/data/GeoLite2-City.mmdb')
    try:
        response = reader.city(ip)
    except Exception as e:
       return json.dumps(str(e))

    data = {}
    filters = set(filter)
    if 'countryName' in filters : 
        data['countryName'] = response.city.name
    if 'countryIso' in filters : 
        data['countryIso'] = response.country.iso_code

    #print(response.country.iso_code)
    #response.country.name
    #response.subdivisions.most_specific.name
    #print(response.subdivisions.most_specific.iso_code)
    #response.city.name
    #response.postal.code
    #response.location.latitude
    #response.location.longitude
    reader.close()
    return json.dumps({ip:data})

if __name__ == '__main__':
    getGeoip('190.113.110.111',null)