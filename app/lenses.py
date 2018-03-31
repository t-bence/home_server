import json

def get_lenses():
    with open('/home/pi/flask/app/cronjobs/lenses.json') as json_file:  
        content = json.load(json_file)
        
    lenses = content['data']
    lenses = sorted(lenses, key=lambda lens: int(lens['price']))
        
    return lenses, content['lastupdate']