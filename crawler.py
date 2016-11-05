from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

to_visit = ["http://espn.com", "http://cnn.com"]

while to_visit:
    next_to_visit = to_visit.pop(0)
    print(next_to_visit)
    res = requests.get(next_to_visit)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')
        for a in soup.find_all('a', href=True):
            to_visit.append(urljoin(next_to_visit, a['href']))
