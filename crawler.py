import bs4.BeautifulSoup
import requests

to_visit = ["espn.com", "cnn.com"]

while to_visit:
    res = requests.get('http://' + to_visit.pop(0))
    if res.status_code == 200:
        result = res.text
        soup = BeautifulSoup(result, 'lxml')
        for a in soup.find_all('a', href=True):
            to_visit.append(a['href'])
