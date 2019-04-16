from os import path
from datetime import datetime
from subprocess import getoutput
import csv



# ping -c 1 8.8.8.8 | grep 'bytes from' | awk '{print $7 " " $8}' | cut -d= -f2


def get_system_data():
    ram_free = int(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024)
    ram_gpu = int(getoutput('cat /boot/config.txt | grep "gpu_mem"')[8:])
    ram_total = int(int(getoutput('cat /proc/meminfo | grep "MemTotal" | egrep "[0-9.]{4,}" -o'))/1024)
    ram_total = ram_gpu + ram_total
    ram_used = ram_total - ram_free - ram_gpu

    hdd = getoutput('df -BG /home/pi/media | grep /home/pi/media | awk \'{print $3 " " $4}\'')
    [hdd_used, hdd_free] = [int(size[:-1]) for size in hdd.split()]

    temp_graph = []
    try:
        with open('/home/pi/bin/temp.log', 'r') as f:
            reader = csv.reader(f)
            temp_graph = list(reader)
    except:
        temp_graph = []

    data = []
    ram = {'used': ram_used, 'free': ram_free, 'gpu': ram_gpu}
    hdd = {'used': hdd_used, 'free': hdd_free}
    data = {'ram': ram, 'hdd': hdd, 'temp_graph': temp_graph}
    
    return data
