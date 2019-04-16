# get data from temp.log
from warnings import warn

def parse_temp_log(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except:
        warn("Error reading file {}".format(filename))
        return [0], [0], [0]
    date = []
    temp = []
    cpu = []

    for line in lines:
        ll = line.split(',')
        date.append(ll[0])
        temp.append(float(ll[1][:-2].strip()))
        cpu.append(float(ll[2].strip()))

    return to_string_array(date[-200:]), to_num_array(temp[-200:]), to_num_array(cpu[-200:])

def to_num_array(x):
    return ",".join(str(item) for item in x)

def to_string_array(x):
    return ", ".join('new Date("' + (str(item) + '").toLocaleString()') for item in x)

