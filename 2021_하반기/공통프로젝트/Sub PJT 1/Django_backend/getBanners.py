from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://www.lottecinema.co.kr/")
soup = BeautifulSoup(html.text, 'html.parser')

url = soup.select('.item img[src]')
print(url)


