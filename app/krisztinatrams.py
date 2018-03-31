# -*- coding: utf-8 -*-

import urllib.request, json

jaratok = [(u'Villamosok Móricz Zsigmond körtér felé', 'F00085'), (u'Villamosok Déli Pályaudvar felé', 'F00086'),
    (u'Buszok át a Lánchídon', 'F00083'), (u'Buszok át az Erzsébet-hídon', 'F00084'), (u'Buszok a XII. kerület felé', 'F00087')]

base_url = 'http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/arrivals-and-departures-for-stop.json?stopId=BKK_'

def get_trams(tram_id=-1):
    data = []
    if tram_id == -1:
        
        for jarat in jaratok:
            new = {}
            new['line'] = jarat
            new['arrivals'] = parse_tram_data(jarat[1])
            data.append(new)
            
    else:
        data.append({'line': jaratok[tram_id], 'arrivals': parse_tram_data(jaratok[tram_id][1])})
            
    return data, jaratok

def parse_tram_data(BKK_id):
    url = base_url + BKK_id

    response = urllib.request.urlopen(url)
    output = response.read().decode('utf-8')
    #print output
    data = json.loads(output)
    
    to_mins = lambda t: int((t - data['currentTime']/1000.0)/60.0)

    # print json.dumps(data, indent=4, sort_keys=True)
    trams = data['data']['entry']['stopTimes']
    
    value = []
    
    for tram in trams:
    
        if 'predictedArrivalTime' not in tram:
            continue
        
        arrival = to_mins(tram['predictedArrivalTime'])
        if arrival < 0:
            continue
        
        direction = tram['stopHeadsign']
        
        BKK_id = tram['tripId']
        id = data['data']['references']['trips'][BKK_id]['routeId']
        number = data['data']['references']['routes'][id]['shortName']
        
        value += [{'number': number, 'direction': direction, 'mins': str(arrival)}]
    
    return value