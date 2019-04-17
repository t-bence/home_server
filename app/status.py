from os import path
from datetime import datetime
from subprocess import getoutput
import csv
import sqlite3


# ping -c 1 8.8.8.8 | grep 'bytes from' | awk '{print $7 " " $8}' | cut -d= -f2

def to_num_array(x):
    return ",".join(str(item) for item in x)

def to_string_array(x):
    return ", ".join('new Date("' + (str(item) + '").toLocaleString()') for item in x)
    # return [0] * x.len()


def get_system_data():
    ram_free = int(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024)
    ram_gpu = int(getoutput('cat /boot/config.txt | grep "gpu_mem"')[8:])
    ram_total = int(int(getoutput('cat /proc/meminfo | grep "MemTotal" | egrep "[0-9.]{4,}" -o'))/1024)
    ram_total = ram_gpu + ram_total
    ram_used = ram_total - ram_free - ram_gpu

    hdd = getoutput('df -BG /home/pi/media | grep /home/pi/media | awk \'{print $3 " " $4}\'')
    [hdd_used, hdd_free] = [int(size[:-1]) for size in hdd.split()]

    date = []
    cpu = []
    temp = []

    conn = sqlite3.connect(database="/home/pi/bin/cpu_temp.db")
    cur = conn.cursor()
    cur.execute("SELECT timestamp, cpu, temp FROM cpu_temp ORDER BY id DESC LIMIT 50")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for r in rows[:-1]:
        date.append("new Date('" + r[0] + "')")
        cpu.append(r[1])
        temp.append(r[2])

    date = ','.join(str(d) for d in date)
    cpu = ','.join(str(c) for c in cpu)
    temp = ','.join(str(c) for c in temp)

    data = []
    ram = {'used': ram_used, 'free': ram_free, 'gpu': ram_gpu}
    hdd = {'used': hdd_used, 'free': hdd_free}
    data = {'ram': ram, 'hdd': hdd, 'date': date, 'temp': temp, 'cpu': cpu}
    
    return data
