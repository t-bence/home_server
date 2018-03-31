# simplepush_notify
# ez lehetne egy szep objektum is... majd egyszer

import requests

simplepush_id_file = "/home/pi/bin/simplepush_id"

def get_simplepush_id():
    with open(simplepush_id_file, 'r') as file:
        return file.read()

# notify 
def notify(title, message):
    notif_url = "https://api.simplepush.io/send/" + get_simplepush_id() + \
        "/" + title + "/" + message
    r = requests.get(notif_url)
    return (r.status_code == 200)