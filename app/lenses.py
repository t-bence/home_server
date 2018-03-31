import json

def get_lenses():
    with open('/home/pi/flask/app/cronjobs/lenses.json') as json_file:  
        content = json.load(json_file)
        
    return content['data'], content['lastupdate']