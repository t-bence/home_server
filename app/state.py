from subprocess import getoutput

def get_state():
    uptime = getoutput('uptime -p')
    uptime = uptime[3:].replace('days', 'd ').replace('hours', 'h').replace('minutes', 'm').replace(',', '')

    # ping = getoutput('ping -c 1 8.8.8.8 | grep \'bytes from\' | awk \'{print $7 " " $8}\' | cut -d= -f2')
    hdd_usage = getoutput('df -h /home/pi/media | grep \'/dev/sda2\' | awk \'{print $5}\'')[:-1]

    cpu_percent = 15

    totalmem = 1024
    free_mem = round(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024.0/totalmem*100)
    ram_usage = 100 - free_mem

    state = {'hdd_usage': hdd_usage, 'ram_usage': ram_usage, 'cpu': cpu_percent, 'uptime': uptime}
    return state