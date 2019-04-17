from subprocess import getoutput
import sqlite3

def get_state():
    uptime = getoutput('uptime -p')
    uptime = uptime[3:].replace('s', '') # ez azért kell, mert néha day, néha days...
    uptime = uptime.replace('day', 'd').replace('hour', 'h').replace('minute', 'm').replace(',', '')

    # ping = getoutput('ping -c 1 8.8.8.8 | grep \'bytes from\' | awk \'{print $7 " " $8}\' | cut -d= -f2')
    hdd_usage = getoutput('df -h /home/pi/media | grep \'/home/pi/media\' | awk \'{print $5}\'')[:-1]

    conn = sqlite3.connect(database="/home/pi/bin/cpu_temp.db")
    cur = conn.cursor()
    cur.execute("SELECT cpu FROM cpu_temp ORDER BY timestamp DESC LIMIT 1")
    rows = cur.fetchall()
    cpu_percent = float(rows[0][0])
    conn.commit()
    conn.close()

    totalmem = 1024
    free_mem = round(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024.0/totalmem*100)
    ram_usage = 100 - free_mem

    state = {'hdd_usage': hdd_usage, 'ram_usage': ram_usage, 'cpu': cpu_percent, 'uptime': uptime}
    return state