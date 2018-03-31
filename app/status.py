from os import path
from datetime import datetime
from subprocess import getoutput


def get_system_data():
    data = []
    LAN_download = getoutput('ifconfig | grep "RX packets"').split("\n")[0].split("(")[1].split(")")[0]
    CPU_temp = getoutput('vcgencmd measure_temp').split("=")[1].split("'")[0]
    core_volts = getoutput('vcgencmd measure_volts core').split("=")[1][0:-3:]
    core_hertz = str(int(getoutput('vcgencmd measure_clock arm').split("=")[1])/1e6)

    data.append(('LAN download', LAN_download))
    data.append(('CPU temperature', CPU_temp + ' &deg;C'))
    data.append(('Core voltage', core_volts + ' V'))
    data.append(('Core frequency', core_hertz + ' MHz'))
    
    
    return data
    
def get_mark_my_prof_data():
    file_path = '/home/pi/bin/markmyprofessor_ratings.txt'
    with open(file_path, 'r') as file:
        num_post = file.read()
    last_post = path.getmtime(file_path) # Unix timestamp
    last_post_text = datetime.fromtimestamp(last_post).strftime('%Y-%m-%d %H:%M:%S')
    return (num_post, last_post_text)