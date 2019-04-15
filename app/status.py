from os import path
from datetime import datetime
from subprocess import getoutput



# ping -c 1 8.8.8.8 | grep 'bytes from' | awk '{print $7 " " $8}' | cut -d= -f2


def get_system_data():
    data = []
    #board_type = getoutput('cat /sys/firmware/devicetree/base/model')
    #try:
    #    # LAN_download = getoutput('ifconfig | grep "RX packets"').split("\n")[0].split("(")[1].split(")")[0]
    #    #LAN_download = getoutput("/sbin/ifconfig enxb827ebb5dd10 | grep 'RX packets' | awk '{print $6,$7}'")[1:-1]
    #except:
    #    LAN_download = "0"
    #CPU_temp = getoutput('vcgencmd measure_temp').split("=")[1].split("'")[0]
    # core_volts = getoutput('vcgencmd measure_volts core').split("=")[1][0:-3:]
    # core_hertz = str(int(float(getoutput('vcgencmd measure_clock arm').split("=")[1])/1e6))
    #uptime = getoutput('uptime -s')
    #kernel = getoutput('uname -r')
    #hostname = getoutput('hostname')
    #total_mem = str(round(int(getoutput('cat /proc/meminfo | grep "MemTotal" | egrep "[0-9.]{4,}" -o'))/1024))
    # free_mem = str(round(int(getoutput('cat /proc/meminfo | grep "MemFree" | egrep "[0-9.]{4,}" -o'))/1024))
    #avail_mem = str(round(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024.0))
    percent_cpu = '14' #getoutput("top -d 0.5 -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4}'")
    # hdd_temp = getoutput("sudo smartctl -a /dev/sda | grep 194 | awk '{print $10}'")
    #net_available = (getoutput("ping -c 1 google.com | grep transmitted | awk '{print $4}'") == '1')


    ################
    ram_free = int(int(getoutput('cat /proc/meminfo | grep "MemAvailable" | egrep "[0-9.]{4,}" -o'))/1024)
    ram_gpu = int(getoutput('cat /boot/config.txt | grep "gpu_mem"')[8:])
    ram_total = int(int(getoutput('cat /proc/meminfo | grep "MemTotal" | egrep "[0-9.]{4,}" -o'))/1024)
    ram_total = ram_gpu + ram_total
    ram_used = ram_total - ram_free - ram_gpu

    hdd = getoutput('df -BG /home/pi/media | grep /home/pi/media | awk \'{print $3 " " $4}\'')
    [hdd_used, hdd_free] = [int(size[:-1]) for size in hdd.split()]

    data = []
    ram = {'used': ram_used, 'free': ram_free, 'gpu': ram_gpu}
    hdd = {'used': hdd_used, 'free': hdd_free}
    data = {'ram': ram, 'hdd': hdd}
    
    

    return data
