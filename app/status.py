from os import path
from datetime import datetime
#from commands import getstatusoutput


def get_system_data():
    data = []
#    LAN_download = getstatusoutput('ifconfig | grep "RX packets"')[1].split("\n")[0].split("(")[1].split("0")[0][0:-1:]
#    CPU_temp = getstatusoutput('vcgencmd measure_temp')[1].split("=")[1].split("'")[0]
#    core_volts = getstatusoutput('vcgencmd measure_volts core')[1].split("=")[1][0:-3:]
#    core_hertz = str(int(getstatusoutput('vcgencmd measure_clock arm')[1].split("=")[1])/1e6)
    LAN_download = "0"
    CPU_temp = "0"
    core_volts = "0"
    core_hertz = "0"

    data.append(('LAN download', LAN_download))
    data.append(('CPU temperature', CPU_temp + ' C'))
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