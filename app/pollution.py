#!/usr/bin/python
# -*- coding: utf-8 -*-

# ez a szkript elmenti a lekérésben érkezett adatot egy JSON fileba

import time
import csv   

def save_measurement(poll_data):
    # UTC epoch seconds
    new_data = [str(time.time()), str(poll_data)]

    with open(r'/home/pi/flask/app/pollution.txt', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_data)