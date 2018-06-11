from bs4 import BeautifulSoup
import requests
import os

website = "http://www.markmyprofessor.com/tanar/adatlap/" + os.environ['MARKMYPROFESSOR_ID'] + ".html"
local_file = "markmyprofessor_ratings.txt"


def get_new_number(web_address):
    page = requests.get(website)
    status_code = page.status_code

    soup = BeautifulSoup(page.content, 'html.parser')

    dl = soup.find_all('dl', class_='simpleList')[0]
    dt = dl.find('dt').get_text()
    
    num = int(dt.split(":")[1])
    print(num)
    return (status_code, num)

    
# main logic
if __name__ == "__main__":
    with open(local_file, 'r') as file:
        old = int(file.read())

    (status_code, new) = get_new_number(website)

    # print status_code

    if int(status_code) == 200:
        if (new > old):
            with open(local_file, 'w') as file:
                file.write(str(new))
        else:
            pass


    else:
        with open(local_file, 'w') as file:
            file.write(str(status_code))
