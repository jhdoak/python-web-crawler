import bs4.BeautifulSoup
import requests

to_visit = ["http://espn.com", "http://cnn.com"]

while to_visit:
    res = requests.get(to_visit.pop(0))
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')
        for a in soup.find_all('a', href=True):
            to_visit.append(a['href'])
