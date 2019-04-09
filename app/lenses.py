import json

def get_lenses():
    with open('/var/www/pici/app/cronjobs/lenses.json', encoding='latin-1') as json_file:  
        content = json.load(json_file)
        
    lenses = content['data']
    lenses = sorted(lenses, key=lambda lens: int(lens['price']))
        
    return lenses, content['lastupdate']