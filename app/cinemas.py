import json
import datetime as dt
from math import floor

def get_screenings():
    with open('/home/pi/flask/app/cronjobs/cinema.json') as json_file:  
        content = json.load(json_file)
        
    cinemas = []
    
    time = int(dt.datetime.today().strftime("%H%M"))
            
    for cinema in content['data']:
        films = tuple(cinema['films'])
        films = sorted(films, key=lambda film: film['times'])
        for film in films:
            film['past'] = (time > film['times'])
            film['times'] = str(film['times'])[0:2:] + ':' + str(film['times'])[2:4:]

        cinemas.append(
            {'films': films, 'name': cinema['name']}
            )

        
    return (cinemas, content['lastupdate'])