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

    return date[-300:], temp[-300:], cpu[-300:]

def to_javascript_array(x):
    return '[' + ",".join(str(item) for item in x) + '];'

if __name__ == "__main__":
    result = parse_temp_log('temp.log')

