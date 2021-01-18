import requests
from bs4 import BeautifulSoup

USD_URL = 'https://finance.naver.com/marketindex/'

response = requests.get(USD_URL).text

soup = BeautifulSoup(response, 'html.parser')

USD = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(f'원달러 환율은 {USD.text}입니다')

