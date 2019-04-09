from os import path
from datetime import datetime
from subprocess import getoutput


def get_system_data():
    data = []
    board_type = getoutput('cat /sys/firmware/devicetree/base/model')
    try:
        # LAN_download = getoutput('ifconfig | grep "RX packets"').split("\n")[0].split("(")[1].split(")")[0]
        LAN_download = getoutput("/sbin/ifconfig enxb827ebb5dd10 | grep 'RX packets' | awk '{print $6,$7}'")[1:-1]
    except:
        LAN_download = "0"
    #CPU_temp = getoutput('vcgencmd measure_temp').split("=")[1].split("'")[0]
    # core_volts = getoutput('vcgencmd measure_volts core').split("=")[1][0:-3:]
    # core_hertz = str(int(float(getoutput('vcgencmd measure_clock arm').split("=")[1])/1e6))
    uptime = getoutput('uptime -s')
    kernel = getoutput('uname -r')
    hostname = getoutput('hostname')
    total_mem = str(round(int(getoutput('cat /proc/meminfo | grep "MemTotal" | egrep "[0-9.]{4,}" -o'))/1024))
    # free_mem = str(round(int(getoutput('cat /proc/meminfo | grep "MemFree" | egrep "[0-9.]{4,}" -o'))/1024))
    avail_mem = str(round(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024.0))
    space = getoutput('df -h /home/pi/media').split()
    total_space = space[8][0:-1] + ' ' + space[8][-1]
    used_space = space[9][0:-1] + ' ' + space[9][-1]
    free_space = space[10][0:-1] + ' ' + space[10][-1]
    percent_space = space[11]
    percent_cpu = getoutput("top -d 0.5 -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4}'")
    # hdd_temp = getoutput("sudo smartctl -a /dev/sda | grep 194 | awk '{print $10}'")
    net_available = (getoutput("ping -c 1 google.com | grep transmitted | awk '{print $4}'") == '1')


    data.append(('Board type', board_type))
    data.append(('Online', 'true' if net_available else 'false'))
    if net_available:
        ping_speed = getoutput("ping -c 1 google.com | grep 'bytes from' | awk '{print $8}'")[5:] + ' ms'
        data.append(('Ping response', ping_speed))
    data.append(('LAN download', LAN_download))
    #data.append(('CPU temperature', CPU_temp + ' &deg;C'))
    data.append(('CPU usage', percent_cpu + '%'))
    # data.append(('Core voltage', core_volts + ' V'))
    # data.append(('Core frequency', core_hertz + ' MHz'))
    data.append(('Running since', uptime))
    data.append(('Kernel version', kernel))
    data.append(('Hostname', hostname))
    data.append(('Total memory', total_mem + ' M'))
    # data.append(('Free memory', free_mem + ' M'))
    data.append(('Available memory', avail_mem + ' M'))
    data.append(('Total HDD space', total_space))
    data.append(('Used HDD space', used_space + ' (' + percent_space + ')'))
    data.append(('Free HDD space', free_space))
    # data.append(('HDD temperature', hdd_temp + ' &deg;C'))
    

    return data
