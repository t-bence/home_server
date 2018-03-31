#!/usr/bin/python
# -*- coding: utf-8 -*-

# ez a szkript kiszedi a Pentax objektíveket az OptiCam kínálatából es elmenti JSON formatumban
# sokaig tart, ezert a cel: hivja meg egy cron-job naponta egyszer


#####################

from bs4 import BeautifulSoup
import requests
import re
import simplepush_notify
import json
import io
import datetime

LOCAL_ADDRESS = '/home/pi/flask/app/cronjobs/lenses.json'

# website = "D:\\Documents\\projektek\\markmyprofessor-auto\\sajat.html"
website = "http://www.opticam.hu/index.php?site=hasznalt"

# functions

def get_lenses(web_address):
    page = requests.get(web_address)
    status_code = page.status_code

    data = []

    if int(status_code) == 200:
        soup = BeautifulSoup(page.content, 'html.parser')

        pentax = soup.find('span', class_='hasznalt', text=re.compile('Pentax'))
        p = pentax.parent.find_next_sibling('p')

        lenses = p.find_all('span', class_='kerdes')
        prices = p.find_all('span', class_='valasz')

        lenses = [lens.get_text().strip() for lens in lenses]
        prices = [price.get_text().strip() for price in prices]
        
        lens_list = []
        for lens, price in zip(lenses, prices):
            lens_list += [{'name': lens, 'price': price, 'new': False}]
        
        lens_list = sorted(lens_list, key=lambda lens: lens['price'])
        # films = sorted(films, key=lambda film: film['times'])

        
        # compare old and new data
        with open(LOCAL_ADDRESS) as f:
            old_data = json.load(f)
            
        old_data_text = json.dumps(old_data)
        
        new_lenses = False
        for lens in lens_list:
            if lens['name'] not in old_data_text:
            #if True:
                lens['new'] = True
                new_lenses = True
                
        # print lens_list
                
        lastupdate = datetime.datetime.today().strftime("%Y. %m. %d. %H:%M:%S")
        data = {'lastupdate': lastupdate, 'data': lens_list}
        
        # write new data to file
        with io.open(LOCAL_ADDRESS, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
        
        if new_lenses:
            # notify through the app
            simplepush_notify.notify(u'OptiCam', u'Új Pentax objektív')
            return True

    return False


#main logic
get_lenses(website)
