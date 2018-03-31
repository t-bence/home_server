#!/usr/bin/python
# -*- coding: utf-8 -*-

# ez a szkript kiszedi a mozimusort a mozik honlapjabol es elmenti JSON formatumban
# sokaig tart, ezert a cel: hivja meg egy cron-job naponta egyszer

from bs4 import BeautifulSoup
import requests
import io
import datetime
import json

websites = {u'Tabán': 'http://tabanartmozi.hu/mozimusor', u'Puskin': 'http://puskinmozi.hu/mozimusor'}


def get_cinema_content(name):
    website = websites[name]
    headers = {'user-agent': 'tx.infinity@gmail.com'}
    page = requests.get(website, headers=headers)
    # print page.status_code
    status_code = page.status_code
    #    print page.headers

    if int(status_code) == 200:
    # if True:
    
        error = False
        
        soup = BeautifulSoup(page.content, 'html.parser')
        # soup = BeautifulSoup(open('puskin.html'), 'html.parser')
        today = soup.find('div', {'class':'active', 'role':'tabpanel'})

        movies = today.find_all('div', {'class':'movie'})
        
        films = []
        for movie in movies:
            h2 = movie.find('h2', {'class':'title'})

            if h2.a.span is not None:
                h2.a.span.clear()
            title = h2.a.get_text().rstrip("\r\n ").strip(" ")
            
            # hours = movie.find_all('div', {'class':'booking-collapse'})
            hours = movie.find_all('a', {'class': 'schedule-time'})
            for hour in hours:
                time = hour.get_text().rstrip("\r\n ").strip("\r\n ")
                time = int(time.replace(":", ""))
                films.append({'title': title, 'times': time})
        return {'name': name, 'films': films}
    else:
        return int(status_code)
        


def get_screenings():
    
    list_Taban = get_cinema_content(u'Tabán')
    list_Puskin = get_cinema_content(u'Puskin')
    
    list = []
    list.append(list_Taban)
    list.append(list_Puskin)
    
    lastupdate = datetime.datetime.today().strftime("%Y. %m. %d. %H:%M:%S")
    
    data = {'lastupdate': lastupdate, 'data': list}
    
    with io.open('/home/pi/flask/app/cronjobs/cinema.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))